from scraper.youtube_api import search_videos, save_to_csv
from cleaner import clean_data

results = search_videos("alexander the great")

for video in results:
    print(video["title"], "| Views:", video["view_count"])

save_to_csv(results)
clean_data()
