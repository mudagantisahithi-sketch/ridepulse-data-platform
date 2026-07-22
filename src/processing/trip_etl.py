import os
import pandas as pd


def extract():

    file_path = "data/sample/trips.csv"

    df = pd.read_csv(file_path)

    print(f"Extracted {len(df)} trips")

    return df



def transform(df):

    print("Starting transformation...")


    # Remove duplicate trips
    df = df.drop_duplicates(
        subset=["trip_id"]
    )


    # Convert data types
    df["customer_id"] = df["customer_id"].astype(int)

    df["driver_id"] = df["driver_id"].astype(int)

    df["distance_km"] = df["distance_km"].astype(float)

    df["fare_amount"] = df["fare_amount"].astype(float)


    # Create new business column
    df["fare_per_km"] = (
        df["fare_amount"] /
        df["distance_km"]
    )


    # Round values
    df["fare_per_km"] = df["fare_per_km"].round(2)


    # Remove invalid records

    df = df[
        df["distance_km"] > 0
    ]

    df = df[
        df["fare_amount"] > 0
    ]


    print(
        f"After transformation: {len(df)} trips"
    )


    return df



def load(df):

    output_dir = "data/processed"

    os.makedirs(
        output_dir,
        exist_ok=True
    )


    output_file = (
        f"{output_dir}/trips_clean.csv"
    )


    df.to_csv(
        output_file,
        index=False
    )


    print(
        f"Saved cleaned data: {output_file}"
    )



def main():

    print("Starting Trip ETL Pipeline")

    trips = extract()

    clean_trips = transform(trips)

    load(clean_trips)

    print("Trip ETL completed successfully")


if __name__ == "__main__":
    main()