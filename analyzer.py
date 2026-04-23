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
