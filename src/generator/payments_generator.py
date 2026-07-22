import os
import pandas as pd
import random
from faker import Faker


fake = Faker()


def generate_payments():

    trips = pd.read_csv(
        "data/sample/trips.csv"
    )

    payments = []

    payment_methods = [
        "Cash",
        "Card",
        "UPI"
    ]

    payment_statuses = [
        "SUCCESS",
        "SUCCESS",
        "SUCCESS",
        "FAILED"
    ]

    for _, trip in trips.iterrows():

        payment = {

            "payment_id": trip["trip_id"],

            "trip_id": trip["trip_id"],

            "amount": trip["fare_amount"],

            "payment_method": random.choice(
                payment_methods
            ),

            "payment_status": random.choice(
                payment_statuses
            ),

            "payment_time": fake.date_time_between(
                start_date="-1y",
                end_date="now"
            )
        }

        payments.append(payment)


    return payments



def save_payments():

    data = generate_payments()

    df = pd.DataFrame(data)


    output_dir = "data/sample"

    os.makedirs(
        output_dir,
        exist_ok=True
    )


    output_path = os.path.join(
        output_dir,
        "payments.csv"
    )


    df.to_csv(
        output_path,
        index=False
    )


    print(f"Generated {len(df)} payments")
    print(f"File saved at: {output_path}")



if __name__ == "__main__":
    save_payments()