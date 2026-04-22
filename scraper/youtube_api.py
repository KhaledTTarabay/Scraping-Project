from googleapiclient.discovery import build
from dotenv import load_dotenv
import os
import csv

load_dotenv()

api_key = os.getenv("YOUTUBE_API_KEY")


def get_youtube_client():
    return build("youtube", "v3", developerKey=api_key)


def search_videos(niche, max_results=50):
    youtube = get_youtube_client()

    request = youtube.search().list(
        q=niche,
        part="snippet",
        type="video",
        maxResults=max_results,
        order="viewCount",
    )

    response = request.execute()

    videos = []

    for item in response["items"]:
        video = {
            "title": item["snippet"]["title"],
            "description": item["snippet"]["description"],
            "channel": item["snippet"]["channelTitle"],
            "published_at": item["snippet"]["publishedAt"],
            "video_id": item["id"]["videoId"],
        }
        videos.append(video)

    youtube = get_youtube_client()
    video_ids = [v["video_id"] for v in videos]
    stats = get_video_stats(youtube, video_ids)

    for video in videos:
        vid_stats = stats.get(video["video_id"], {})
        video["view_count"] = vid_stats.get("view_count", 0)
        video["like_count"] = vid_stats.get("like_count", 0)
        video["comment_count"] = vid_stats.get("comment_count", 0)

    return videos


def get_video_stats(youtube, video_ids):
    request = youtube.videos().list(part="statistics", id=",".join(video_ids))
    response = request.execute()

    stats = {}
    for item in response["items"]:
        stats[item["id"]] = {
            "view_count": item["statistics"].get("viewCount", 0),
            "like_count": item["statistics"].get("likeCount", 0),
            "comment_count": item["statistics"].get("commentCount", 0),
        }
    return stats


def save_to_csv(videos, filename="raw_data.csv"):
    keys = [
        "title",
        "description",
        "channel",
        "published_at",
        "video_id",
        "view_count",
        "like_count",
        "comment_count",
    ]

    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=keys)
        writer.writeheader()
        writer.writerows(videos)

    print(f"Saved {len(videos)} to {filename}")
