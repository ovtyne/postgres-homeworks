"""Скрипт для заполнения данными таблиц в БД Postgres."""
import csv
import psycopg2

with psycopg2.connect(host='localhost', database='north', user='ovto', password='password') as conn:
    with conn.cursor() as cur:

        with open('north_data/customers_data.csv') as csvfile:
            next(csvfile)
            reader = csv.reader(csvfile)
            for row in reader:
                cur.execute('INSERT INTO customers VALUES (%s, %s, %s)', row)

        with open('north_data/employees_data.csv') as csvfile:
            next(csvfile)
            reader = csv.reader(csvfile)
            for row in reader:
                cur.execute('INSERT INTO employees VALUES (%s, %s, %s, %s, %s, %s)', row)

        with open('north_data/orders_data.csv') as csvfile:
            next(csvfile)
            reader = csv.reader(csvfile)
            for row in reader:
                cur.execute('INSERT INTO orders VALUES (%s, %s, %s, %s, %s)', row)

