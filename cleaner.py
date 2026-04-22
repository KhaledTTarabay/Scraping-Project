import pandas as pd
import html


def clean_data(input_file="raw_data.csv", output_file="clean_data.csv"):
    df = pd.read_csv(input_file)

    df["title"] = df["title"].apply(lambda x: html.unescape(str(x)))
    df["description"] = df["description"].apply(lambda x: html.unescape(str(x)))

    df["view_count"] = (
        pd.to_numeric(df["view_count"], errors="coerce").fillna(0).astype(int)
    )
    df["like_count"] = (
        pd.to_numeric(df["like_count"], errors="coerce").fillna(0).astype(int)
    )
    df["comment_count"] = (
        pd.to_numeric(df["comment_count"], errors="coerce").fillna(0).astype(int)
    )

    df["published_at"] = pd.to_datetime(df["published_at"])

    df["description"] = df["description"].fillna("")

    df = df.drop_duplicates(subset="video_id")

    df.to_csv(output_file, index=False)
    print(f"Cleaned {len(df)} videos -> {output_file}")

    return df
