import sys

sys.path.append('../db')
from sqlrunner import *

class Screening:
    def __init__(self, film_id, show_time, tickets_available, tickets_sold):
        self.id = 0
        self.film_id = film_id
        self.show_time = show_time
        self.tickets_available = tickets_available
        self.tickets_sold = tickets_sold

    def save(self):
        sql = """
            INSERT INTO screenings (film_id, show_time, tickets_available, tickets_sold)
            VALUES (%s, %s, %s, %s)
            RETURNING id;
        """
        values = (self.film_id, self.show_time, self.tickets_available, self.tickets_sold)
        result = Sqlrunner.run(sql, "fetchone", values)
        self.id = result[0]
        
    def all(self):
        sql = "SELECT * from screenings"
        rows = Sqlrunner.run(sql, "fetchall")

        screening_array = []
        for screening_row in rows:
            fetched_screening = Screening(*screening_row[1:])
            fetched_screening.id = screening_row[0]
            screening_array.append(fetched_screening)
        return screening_array

    def update(self):
        sql = "UPDATE screenings SET film_id=%s, show_time=%s, tickets_available=%s, tickets_sold=%s WHERE id=%s "
        values = (self.film_id, self.show_time, self.tickets_available, self.tickets_sold, self.id)
        Sqlrunner.run(sql, "", values)

    def delete_all():
        sql = "DELETE FROM SCREENINGS"
        Sqlrunner.run(sql, "")


