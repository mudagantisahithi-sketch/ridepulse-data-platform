from customer_etl import main as customer_etl
from driver_etl import main as driver_etl
from trip_etl import main as trip_etl
from payment_etl import main as payment_etl
from rating_etl import main as rating_etl


def main():

    print("================================")
    print("Starting RidePulse ETL Pipeline")
    print("================================")


    print("\n1. Customer ETL")
    customer_etl()


    print("\n2. Driver ETL")
    driver_etl()


    print("\n3. Trip ETL")
    trip_etl()


    print("\n4. Payment ETL")
    payment_etl()


    print("\n5. Rating ETL")
    rating_etl()


    print("\n================================")
    print("RidePulse ETL Pipeline Completed")
    print("================================")


if __name__ == "__main__":
    main()