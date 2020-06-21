import psycopg2

class DBSetup:
    def __init__(self):
        pass

    def set_up_tables():
        connection = psycopg2.connect(dbname="cinema_db", user="postgres", password="")
        cursor = connection.cursor()

        cursor.execute("DROP TABLE IF EXISTS tickets")
        cursor.execute("DROP TABLE IF EXISTS screenings")
        cursor.execute("DROP TABLE IF EXISTS customers")
        cursor.execute("DROP TABLE IF EXISTS films")

        cursor.execute("""
          CREATE TABLE customers (
            id SERIAL PRIMARY KEY,
            name VARCHAR(255),
            funds FlOAT(3)
          )
        """)
        connection.commit()

        cursor.execute("""
          CREATE TABLE films (
            id SERIAL PRIMARY KEY,
            title VARCHAR(255),
            price FlOAT(3)
          )
        """)
        connection.commit()

        cursor.execute("""
          CREATE TABLE screenings (
            id SERIAL PRIMARY KEY,
            film_id INT REFERENCES films(id) ON DELETE CASCADE,
            tickets_available INT,
            tickets_sold INT,
            show_time VARCHAR (255)
          )
        """)
        connection.commit()

        cursor.execute("""
          CREATE TABLE tickets (
            id SERIAL PRIMARY KEY,
            film_id INT REFERENCES films(id) ON DELETE CASCADE,
            customer_id INT REFERENCES customers(id) ON DELETE CASCADE,
            screening_id INT REFERENCES screenings(id) ON DELETE CASCADE
          )
        """)
        connection.commit()

        connection.close()
