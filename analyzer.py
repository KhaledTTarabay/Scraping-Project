import pandas as pd
from collections import Counter
import re

STOPWORDS = {
    "the",
    "a",
    "an",
    "and",
    "or",
    "but",
    "in",
    "on",
    "at",
    "to",
    "for",
    "of",
    "with",
    "is",
    "it",
    "this",
    "that",
    "was",
    "are",
    "be",
    "as",
    "by",
    "from",
    "his",
    "her",
    "he",
    "she",
    "they",
    "we",
    "you",
    "i",
}


def extract_keywords(text):
    words = re.findall(r"\b[a-z]{4,}\b", text.lower())
    return [w for w in words if w not in STOPWORDS]


def analyze(input_file="clean_data.csv", output_file="analysis.csv"):
    df = pd.read_csv(input_file)

    all_keywords = []
    for title in df["title"]:
        all_keywords.extend(extract_keywords(title))

    keyword_counts = Counter(all_keywords)
    keyword_df = pd.DataFrame(
        keyword_counts.most_common(30), columns=["keyword", "frequency"]
    )

    def avg_views_for_keyword(keyword):
        mask = df["title"].str.lower().str.contains(keyword)
        return df[mask]["view_count"].mean()

    keyword_df["avg_views"] = keyword_df["keyword"].apply(avg_views_for_keyword)
    keyword_df["avg_views"] = keyword_df["avg_views"].fillna(0).astype(int)

    keyword_df.to_csv(output_file, index=False)
    print(f"Top keywords saved -> {output_file}")
    return keyword_df


def channel_analysis(input_file="clean_data.csv", output_file="channel_analysis.csv"):
    df = pd.read_csv(input_file)

    channel_df = (
        df.groupby("channel")
        .agg(
            video_count=("video_id", "count"),
            total_views=("view_count", "sum"),
            avg_views=("view_count", "mean"),
            avg_likes=("like_count", "mean"),
        )
        .reset_index()
    )

    channel_df = channel_df.sort_values("total_views", ascending=False)
    channel_df["avg_views"] = channel_df["avg_views"].astype(int)
    channel_df["avg_likes"] = channel_df["avg_likes"].astype(int)

    channel_df.to_csv(output_file, index=False)
    print(f"Channel analysis saved {output_file}")
    return channel_df


def best_time_to_post(input_file="clean_data.csv", output_file="time_analysis.csv"):
    df = pd.read_csv(input_file)

    df["published_at"] = pd.to_datetime(df["published_at"])
    df["hour"] = df["published_at"].dt.hour
    df["day_of_week"] = df["published_at"].dt.day_name()

    hour_df = (
        df.groupby("hour")
        .agg(video_count=("video_id", "count"), avg_views=("view_count", "mean"))
        .reset_index()
    )
    hour_df["avg_views"] = hour_df["avg_views"].astype(int)

    day_df = (
        df.groupby("day_of_week")
        .agg(video_count=("video_id", "count"), avg_views=("view_count", "mean"))
        .reset_index()
    )
    day_df["avg_views"] = day_df["avg_views"].astype(int)

    hour_df.to_csv(output_file, index=False)
    print(f"Time analysis saved {output_file}")
    return hour_df, day_df
