import os
import pandas as pd


def extract():

    file_path = "data/sample/drivers.csv"

    df = pd.read_csv(file_path)

    print(f"Extracted {len(df)} drivers")

    return df



def transform(df):

    print("Cleaning driver data...")


    # Remove duplicates
    df = df.drop_duplicates(
        subset=["driver_id"]
    )


    # Remove invalid ratings
    df = df[
        (df["rating"] >= 0) &
        (df["rating"] <= 5)
    ]


    # Standardize text columns
    df["city"] = (
        df["city"]
        .str.strip()
        .str.title()
    )


    df["vehicle_type"] = (
        df["vehicle_type"]
        .str.strip()
        .str.title()
    )


    # Convert joining date
    df["joining_date"] = pd.to_datetime(
        df["joining_date"]
    )


    print(
        f"After transformation: {len(df)} drivers"
    )


    return df



def load(df):

    output_dir = "data/processed"

    os.makedirs(
        output_dir,
        exist_ok=True
    )


    output_file = (
        f"{output_dir}/drivers_clean.csv"
    )


    df.to_csv(
        output_file,
        index=False
    )


    print(
        f"Saved: {output_file}"
    )



def main():

    print("Starting Driver ETL")

    drivers = extract()

    clean_drivers = transform(
        drivers
    )

    load(clean_drivers)

    print(
        "Driver ETL completed"
    )


if __name__ == "__main__":
    main()