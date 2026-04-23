# Scrape-To-Dashboard

A data pipeline that collects Youtube video data via the Youtube Data API v3, cleans it, analyzes the keyword performance, and visualizes insights in an interactive dashboard.

## Pipeline
1. scraper/youtube_api.py - collect videos by niche keyword
2. cleaner.py - clean and normalize raw data
3. analyzer.py - extracts keyword frequency and average views
4. dashboard.py - visualize insights with Streamlit + Plotly

## Setup
1. Clone the repo
2. set up a virtual environment: python -m venv .venv
3. activate: .venv\scripts\activate
4. install dependencies: pip install -r requirements.txt
5. create a .env file with your Youtube API key
6. run: python main.py
7. launch dashboard: streamlit run dashboard.py

## Libraries used
- Pandas, Streamlit, Plotly
- Youtube Data API v3

### Future Versions: 
Planning to add multiplatform scraping and analysis