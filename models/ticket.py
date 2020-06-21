import sys

sys.path.append('../db')
from sqlrunner import *


class Ticket:
    def __init__(self, film_id, screening_id, customer_id):
        self.id = 0
        self.film_id = film_id
        self.screening_id = screening_id
        self.customer_id = customer_id

    def save(self):
        sql = """
            INSERT INTO tickets (film_id, screening_id, customer_id)
            VALUES (%s, %s, %s)
            RETURNING id;
        """
        values = (self.film_id, self.screening_id, self.customer_id)
        result = Sqlrunner.run(sql, "fetchone", values)
        self.id = result[0]

    def all(self):
        sql = "SELECT * from tickets"
        rows = Sqlrunner.run(sql, "fetchall")

        ticket_array = []
        for ticket_row in rows:
            fetched_ticket = ticket(*ticket_row[1:])
            fetched_ticket.id = ticket_row[0]
            ticket_array.append(fetched_ticket)
        return ticket_array

    def update(self):
        sql = "UPDATE tickets SET film_id=%s, screening_id=%s, customer_id=%s WHERE id=%s "
        values = (self.film_id, self.screening_id, self.customer_id, self.id)
        Sqlrunner.run(sql, "", values)

    def delete_all():
        sql = "DELETE FROM TICKETS"
        Sqlrunner.run(sql, "")
