import os
import pandas as pd
import random


def generate_ratings():

    trips = pd.read_csv(
        "data/sample/trips.csv"
    )

    ratings = []

    comments = [
        "Great ride",
        "Good experience",
        "Driver was polite",
        "Very comfortable",
        "Average service",
        "Could be better"
    ]

    for _, trip in trips.iterrows():

        rating = {
            "rating_id": trip["trip_id"],
            "trip_id": trip["trip_id"],
            "customer_id": trip["customer_id"],
            "driver_id": trip["driver_id"],
            "rating": random.randint(1, 5),
            "comment": random.choice(comments)
        }

        ratings.append(rating)

    return ratings


def save_ratings():

    data = generate_ratings()

    df = pd.DataFrame(data)

    output_dir = "data/sample"

    os.makedirs(
        output_dir,
        exist_ok=True
    )

    output_path = os.path.join(
        output_dir,
        "ratings.csv"
    )

    df.to_csv(
        output_path,
        index=False
    )

    print(f"Generated {len(df)} ratings")
    print(f"File saved at: {output_path}")


if __name__ == "__main__":
    save_ratings()