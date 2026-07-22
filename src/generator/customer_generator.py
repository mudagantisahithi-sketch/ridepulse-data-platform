import os
import pandas as pd
from faker import Faker
import random


fake = Faker()


def generate_customers(number_of_customers=1000):

    customers = []

    cities = [
        "Hyderabad",
        "Bangalore",
        "Pune",
        "Chennai",
        "Mumbai",
        "Delhi"
    ]

    for customer_id in range(1, number_of_customers + 1):

        customer = {
            "customer_id": customer_id,
            "first_name": fake.first_name(),
            "last_name": fake.last_name(),
            "email": fake.email(),
            "phone": fake.phone_number(),
            "city": random.choice(cities),
            "signup_date": fake.date_between(
                start_date="-2y",
                end_date="today"
            )
        }

        customers.append(customer)

    return customers


def save_customers():

    # Generate customer data
    data = generate_customers()

    # Convert to DataFrame
    df = pd.DataFrame(data)

    # Create output folder if it does not exist
    output_dir = "data/sample"
    os.makedirs(output_dir, exist_ok=True)

    # File path
    output_path = os.path.join(output_dir, "customers.csv")

    # Save CSV
    df.to_csv(
        output_path,
        index=False
    )

    print(f"Generated {len(df)} customers")
    print(f"File saved at: {output_path}")


if __name__ == "__main__":
    save_customers()