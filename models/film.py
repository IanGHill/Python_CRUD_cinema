import sys

sys.path.append('../db')
sys.path.append('../models')
from sqlrunner import *
from customer import *
from screening import *

class Film:
    def __init__(self, title, price):
        self.id = 0
        self.title = title
        self.price = price

    def save(self):
        sql = """
            INSERT INTO films (title, price)
            VALUES (%s, %s)
            RETURNING id;
        """
        values = (self.title, self.price)
        result = Sqlrunner.run(sql, "fetchone", values)
        self.id = result[0]
        
    def all(self):
        sql = "SELECT * from films"
        rows = Sqlrunner.run(sql, "fetchall")

        film_array = []
        for film_row in rows:
            fetched_film = Film(*film_row[1:])
            fetched_film.id = film_row[0]
            film_array.append(fetched_film)
        return film_array

    def find_by_name(name):
        sql = "SELECT * from films WHERE name=%s"
        values = (name,)
        
        film_row = Sqlrunner.run(sql, "fetchone", values)

        if film_row is not None:
            fetched_film = Film(*film_row[1:])
            fetched_film.id = film_row[0]
            return fetched_film
        else:
            return film_row


    def update(self):
        sql = "UPDATE films SET title=%s, price=%s WHERE id=%s "
        values = (self.title, self.price, self.id)
        Sqlrunner.run(sql, "", values)

    def delete_all():
        sql = "DELETE FROM FILMS"
        Sqlrunner.run(sql, "")

    def which_customers(self):
        sql = """
            SELECT customers.* FROM tickets
            INNER JOIN customers
            ON
            tickets.customer_id = customers.id
            WHERE
            tickets.film_id = %s
            """
        values = (self.id,)
        customers = Sqlrunner.run(sql, "fetchall", values)
        customer_array = []
        for customer in customers:
            fetched_customer = Customer(*customer[1:])
            fetched_customer.id = customer[0]
            customer_array.append(fetched_customer)
        return customer_array

    def how_many_customers(self):
        sql = "SELECT COUNT(*) FROM tickets WHERE tickets.film_id = %s"
        values = (self.id,)
        return Sqlrunner.run(sql, "fetchone", values)[0]

    def most_popular_screening_using_sql(self):
        sql = """SELECT id, film_id, show_time, tickets_available, tickets_sold
                FROM screenings
                WHERE
                film_id = %s
                ORDER BY
                tickets_sold DESC
                """
        values = (self.id,)
        result = Sqlrunner.run(sql, "fetchone", values)

        print(result)
        if result is not None:
            screening = Screening(*result[1:])
            screening.id = result[0]
            return screening.show_time
        else:
            return "No screenings for this film"


