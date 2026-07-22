import os
import pandas as pd


def extract():

    file_path = "data/sample/payments.csv"

    df = pd.read_csv(file_path)

    print(f"Extracted {len(df)} payments")

    return df



def transform(df):

    print("Cleaning payment data...")


    # Remove duplicate payments
    df = df.drop_duplicates(
        subset=["payment_id"]
    )


    # Remove invalid amounts
    df = df[
        df["amount"] > 0
    ]


    # Standardize payment method
    df["payment_method"] = (
        df["payment_method"]
        .str.strip()
        .str.upper()
    )


    # Standardize payment status
    df["payment_status"] = (
        df["payment_status"]
        .str.strip()
        .str.upper()
    )


    # Convert timestamp
    df["payment_time"] = pd.to_datetime(
        df["payment_time"]
    )


    print(
        f"After transformation: {len(df)} payments"
    )


    return df



def load(df):

    output_dir = "data/processed"

    os.makedirs(
        output_dir,
        exist_ok=True
    )


    output_file = (
        f"{output_dir}/payments_clean.csv"
    )


    df.to_csv(
        output_file,
        index=False
    )


    print(
        f"Saved: {output_file}"
    )



def main():

    print("Starting Payment ETL")

    payments = extract()

    clean_payments = transform(
        payments
    )

    load(clean_payments)

    print(
        "Payment ETL completed"
    )


if __name__ == "__main__":
    main()