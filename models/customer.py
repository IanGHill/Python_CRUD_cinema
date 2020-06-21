import sys

sys.path.append('../db')
sys.path.append('../models')
from sqlrunner import *
from ticket import *

class Customer():
    def __init__(self, name, funds):
        self.id = 0
        self.name = name
        self.funds = funds

    def save(self):
        sql = """
            INSERT INTO customers (name, funds)
            VALUES (%s, %s)
            RETURNING id;
        """
        values = (self.name, self.funds)
        result = Sqlrunner.run(sql, "fetchone", values)
        self.id = result[0]

    def all():
        sql = "SELECT * FROM customers;"
        rows = Sqlrunner.run(sql, "fetchall")

        customer_array = []
        for customer_row in rows:
            fetched_customer = Customer(*customer_row[1:])
            fetched_customer.id = customer_row[0]
            customer_array.append(fetched_customer)
        return customer_array

    def find_by_name(name):
        sql = "SELECT * from customers WHERE name=%s"
        values = (name,)

        customer_row = Sqlrunner.run(sql, "fetchone", values)

        if customer_row is not None:
            fetched_customer = Customer(*customer_row[1:])
            fetched_customer.id = customer_row[0]
            return fetched_customer
        else:
            return customer_row

    def update(self):
        sql = "UPDATE customers SET name=%s, funds=%s WHERE id=%s"
        values = (self.name, self.funds, self.id)
        Sqlrunner.run(sql, "", values)

    def buy_ticket(self, film, screening):
        if self.funds >= film.price:
            if screening.tickets_available > 0:
                self.funds -= film.price
                screening.tickets_available -= 1
                screening.tickets_sold += 1

                self.update()
                screening.update()

                Ticket(film.id, screening.id, self.id).save()

            else:
                print("No tickets available")
        else:
            print("Not enough money")

    def delete_all():
        sql = "DELETE FROM CUSTOMERS"
        SqlRunner.run(sql)

    def delete_all():
        sql = "DELETE FROM CUSTOMERS"
        Sqlrunner.run(sql, "")

