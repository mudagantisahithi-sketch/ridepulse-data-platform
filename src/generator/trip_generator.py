import os
import pandas as pd
import random
from faker import Faker


fake = Faker()


def generate_trips(number_of_trips=5000):

    # Read existing customer and driver data
    customers = pd.read_csv(
        "data/sample/customers.csv"
    )

    drivers = pd.read_csv(
        "data/sample/drivers.csv"
    )

    trips = []

    locations = [
        "Hitech City",
        "Gachibowli",
        "Banjara Hills",
        "Whitefield",
        "Koramangala",
        "Indiranagar",
        "Andheri",
        "Connaught Place"
    ]

    payment_methods = [
        "Cash",
        "Card",
        "UPI"
    ]

    statuses = [
        "Completed",
        "Completed",
        "Completed",
        "Cancelled"
    ]


    for trip_id in range(1, number_of_trips + 1):

        customer = customers.sample(1).iloc[0]
        driver = drivers.sample(1).iloc[0]

        distance = round(
            random.uniform(2, 30),
            2
        )

        fare = round(
            distance * random.uniform(15, 25),
            2
        )


        trip = {

            "trip_id": trip_id,

            "customer_id": customer["customer_id"],

            "driver_id": driver["driver_id"],

            "pickup_location": random.choice(locations),

            "drop_location": random.choice(locations),

            "distance_km": distance,

            "fare_amount": fare,

            "payment_method": random.choice(payment_methods),

            "trip_status": random.choice(statuses),

            "trip_timestamp": fake.date_time_between(
                start_date="-1y",
                end_date="now"
            )
        }

        trips.append(trip)


    return trips



def save_trips():

    data = generate_trips()

    df = pd.DataFrame(data)


    output_dir = "data/sample"

    os.makedirs(
        output_dir,
        exist_ok=True
    )


    output_path = os.path.join(
        output_dir,
        "trips.csv"
    )


    df.to_csv(
        output_path,
        index=False
    )


    print(f"Generated {len(df)} trips")
    print(f"File saved at: {output_path}")



if __name__ == "__main__":
    save_trips()