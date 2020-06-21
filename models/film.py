import psycopg2
import sys

sys.path.append('../db')
from sqlrunner import *

class Film:
    def __init__(self, title, price):
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

