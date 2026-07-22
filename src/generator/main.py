from customer_generator import save_customers
from driver_generator import save_drivers
from trip_generator import save_trips
from payments_generator import save_payments
from rating_generator import save_ratings


def main():

    print("Starting RidePulse Data Generation")

    save_customers()
    save_drivers()
    save_trips()
    save_payments()
    save_ratings()

    print("RidePulse dataset generation completed!")


if __name__ == "__main__":
    main()