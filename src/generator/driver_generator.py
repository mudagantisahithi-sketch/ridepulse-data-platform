import os
import pandas as pd
from faker import Faker
import random


fake = Faker()


def generate_drivers(number_of_drivers=500):

    drivers = []

    cities = [
        "Hyderabad",
        "Bangalore",
        "Pune",
        "Chennai",
        "Mumbai",
        "Delhi"
    ]

    vehicle_types = [
        "Sedan",
        "SUV",
        "Hatchback",
        "Bike"
    ]

    for driver_id in range(1, number_of_drivers + 1):

        driver = {
            "driver_id": driver_id,
            "first_name": fake.first_name(),
            "last_name": fake.last_name(),
            "email": fake.email(),
            "phone": fake.phone_number(),
            "city": random.choice(cities),
            "vehicle_type": random.choice(vehicle_types),
            "rating": round(random.uniform(3.5, 5.0), 1),
            "joining_date": fake.date_between(
                start_date="-5y",
                end_date="today"
            )
        }

        drivers.append(driver)

    return drivers


def save_drivers():

    data = generate_drivers()

    df = pd.DataFrame(data)

    output_dir = "data/sample"

    os.makedirs(output_dir, exist_ok=True)

    output_path = os.path.join(
        output_dir,
        "drivers.csv"
    )

    df.to_csv(
        output_path,
        index=False
    )

    print(f"Generated {len(df)} drivers")
    print(f"File saved at: {output_path}")


if __name__ == "__main__":
    save_drivers()