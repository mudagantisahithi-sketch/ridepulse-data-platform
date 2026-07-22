# RidePulse Data Model

## Overview

This document describes the initial data model design for the RidePulse ride-sharing analytics platform.

The model contains customer, driver, trip, payment, and rating entities.

---

# Entity 1: Customers

Table: customers

| Column | Data Type | Description |
|--------|-----------|-------------|
| customer_id | Integer | Unique customer identifier |
| first_name | String | Customer first name |
| last_name | String | Customer last name |
| email | String | Customer email |
| phone | String | Customer phone number |
| city | String | Customer city |
| signup_date | Date | Registration date |

---

# Entity 2: Drivers

Table: drivers

| Column | Data Type | Description |
|--------|-----------|-------------|
| driver_id | Integer | Unique driver identifier |
| first_name | String | Driver name |
| city | String | Driver operating city |
| vehicle_type | String | Vehicle category |
| rating | Float | Driver rating |
| joining_date | Date | Driver joining date |

---

# Entity 3: Trips

Table: trips

| Column | Data Type | Description |
|--------|-----------|-------------|
| trip_id | Integer | Unique trip identifier |
| customer_id | Integer | Customer reference |
| driver_id | Integer | Driver reference |
| pickup_location | String | Trip starting location |
| drop_location | String | Trip destination |
| distance_km | Float | Distance travelled |
| fare_amount | Float | Trip cost |
| payment_method | String | Payment type |
| trip_status | String | Completed/Cancelled |
| trip_timestamp | Timestamp | Trip time |

---

# Entity 4: Payments

Table: payments

| Column | Data Type | Description |
|--------|-----------|-------------|
| payment_id | Integer | Payment identifier |
| trip_id | Integer | Related trip |
| amount | Float | Payment amount |
| payment_method | String | Cash/Card/UPI |
| payment_status | String | Success/Failed |
| payment_time | Timestamp | Payment time |

---

# Entity 5: Ratings

Table: ratings

| Column | Data Type | Description |
|--------|-----------|-------------|
| rating_id | Integer | Rating identifier |
| trip_id | Integer | Related trip |
| customer_id | Integer | Customer |
| driver_id | Integer | Driver |
| rating | Integer | Rating value |
| comment | String | Customer feedback |