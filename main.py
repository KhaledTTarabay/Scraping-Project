from scraper.youtube_api import search_videos, save_to_csv
from cleaner import clean_data
from analyzer import analyze, channel_analysis, best_time_to_post

searchWord = input("Enter the niche you wanna scrape: ")

results = search_videos(searchWord)

for video in results:
    print(video["title"], "| Views:", video["view_count"])

save_to_csv(results)
clean_data()
analyze()
channel_analysis()
best_time_to_post()
