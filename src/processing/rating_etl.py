import os
import pandas as pd


def extract():

    file_path = "data/sample/ratings.csv"

    df = pd.read_csv(file_path)

    print(f"Extracted {len(df)} ratings")

    return df



def transform(df):

    print("Cleaning rating data...")


    # Remove duplicate ratings
    df = df.drop_duplicates(
        subset=["rating_id"]
    )


    # Validate rating range
    df = df[
        (df["rating"] >= 1) &
        (df["rating"] <= 5)
    ]


    # Clean comments
    df["comment"] = (
        df["comment"]
        .fillna("No comment")
        .str.strip()
    )


    print(
        f"After transformation: {len(df)} ratings"
    )


    return df



def load(df):

    output_dir = "data/processed"

    os.makedirs(
        output_dir,
        exist_ok=True
    )


    output_file = (
        f"{output_dir}/ratings_clean.csv"
    )


    df.to_csv(
        output_file,
        index=False
    )


    print(
        f"Saved: {output_file}"
    )



def main():

    print("Starting Rating ETL")

    ratings = extract()

    clean_ratings = transform(
        ratings
    )

    load(clean_ratings)

    print(
        "Rating ETL completed"
    )


if __name__ == "__main__":
    main()