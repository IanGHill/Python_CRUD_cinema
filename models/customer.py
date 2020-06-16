import psycopg2

class Customer():
    def __init__(self, name, funds):
        self.id = 0
        self.name = name
        self.funds = funds


    def save(self):
        connection = psycopg2.connect(dbname="cinema_db", user="postgres", password="")
        cursor = connection.cursor()
        sql = """
            INSERT INTO customers (name, funds)
            VALUES (%s, %s)
            RETURNING id;
        """
        inserted_values = (self.name, self.funds)
        cursor.execute(sql, inserted_values)
        self.id = cursor.fetchone()[0]
        connection.commit()
        connection.close()

    def get_all_customers():
        connection = psycopg2.connect(dbname="cinema_db", user="postgres", password="")
        cursor = connection.cursor()
        sql = "SELECT * FROM customers;"
        cursor.execute(sql)
        rows = cursor.fetchall()
        connection.close()
        customer_array = []
        for customer_row in rows:
            fetched_customer = Customer(*customer_row[1:])
            fetched_customer.id = customer_row[0]
            customer_array.append(fetched_customer)
        return customer_array
