import os
import pandas as pd


def extract():

    file_path = "data/sample/customers.csv"

    df = pd.read_csv(file_path)

    print(f"Extracted {len(df)} customers")

    return df



def transform(df):

    print("Cleaning customer data...")


    # Remove duplicate customers
    df = df.drop_duplicates(
        subset=["customer_id"]
    )


    # Remove missing emails
    df = df[
        df["email"].notna()
    ]


    # Standardize city names
    df["city"] = (
        df["city"]
        .str.strip()
        .str.title()
    )


    # Convert signup date
    df["signup_date"] = pd.to_datetime(
        df["signup_date"]
    )


    print(
        f"After transformation: {len(df)} customers"
    )


    return df



def load(df):

    output_dir = "data/processed"

    os.makedirs(
        output_dir,
        exist_ok=True
    )


    output_file = (
        f"{output_dir}/customers_clean.csv"
    )


    df.to_csv(
        output_file,
        index=False
    )


    print(
        f"Saved: {output_file}"
    )



def main():

    print("Starting Customer ETL")

    customers = extract()

    clean_customers = transform(
        customers
    )

    load(clean_customers)

    print(
        "Customer ETL completed"
    )


if __name__ == "__main__":
    main()