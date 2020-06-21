import sys

sys.path.append('./db')
sys.path.append('./models')
from customer import *
from film import *
from ticket import *
from screening import *
from db_setup import *

DBSetup.set_up_tables()

customer1 = Customer('Grandpa Simpson', 100)
customer1.save()

customer2 = Customer('Marge Simpson', 80)
customer2.save()

customer3 = Customer('Bart Simpson', 60)
customer3.save()

customer4 = Customer('Lisa Simpson', 40)
customer4.save()

customer5 = Customer('Maggie Simpson', 20)
customer5.save()
print(customer5.name)
print(customer5.id)
print(customer5.funds)

customer5.funds = 54
customer5.update()
print(customer5.name)
print(customer5.id)
print(customer5.funds)

print(Customer.all()[0].name)

film1 = Film('Gone With the Wind', 10)
film1.save()

film2 = Film('Mockingjay', 10)
film2.save()

film3 = Film('Lord of the Rings', 8)
film3.save()

film3.title = 'Fellowship of the Ring'
film3.update()

film2.price = 6
film2.update()

screening1 = Screening(film1.id, '18:00', 20, 0)
screening1.save()

screening2 = Screening(film1.id, '20:00', 20, 0)
screening2.save()

screening3 = Screening(film2.id, '18:00', 10, 0)
screening3.save()

screening4 = Screening(film2.id, '20:00', 10, 0)
screening4.save()

screening5 = Screening(film3.id, '21:00', 5, 0)
screening5.save()

screening6 = Screening(film3.id, '22:00', 5, 0)
screening6.save()

screening7 = Screening(film1.id, '23:00', 20, 0)
screening7.save()


ticket1 = Ticket(film1.id, screening1.id, customer1.id)
ticket1.save()

ticket2 = Ticket(film1.id, screening1.id, customer2.id)
ticket2.save()

ticket3 = Ticket(film1.id, screening1.id, customer3.id)
ticket3.save()

ticket4 = Ticket(film2.id, screening3.id, customer1.id)
ticket4.save()

ticket5 = Ticket(film2.id, screening4.id, customer1.id)
ticket5.save()

ticket6 = Ticket(film1.id, screening2.id, customer5.id)
ticket6.save()

ticket7 = Ticket(film3.id, screening5.id, customer1.id)
ticket7.save()

ticket8 = Ticket(film3.id, screening6.id, customer4.id)
ticket8.save()

ticket9 = Ticket(film3.id, screening6.id, customer5.id)
ticket9.save()

ticket10 = Ticket(film1.id, screening7.id, customer5.id)
ticket10.save()

print(f"Before purchase {customer1.name} has £{customer1.funds}, there are {screening1.tickets_available} tickets for {film1.title} available at a price of £{film1.price} each")

customer1.buy_ticket(film1, screening1)

print(f"After purchase {customer1.name} has £{customer1.funds} left and there are {screening1.tickets_available} tickets for {film1.title} remaining")
print(screening1.show_time)
screening1.show_time = '19:00'
screening1.update
print(screening1.show_time)

print(ticket1.customer_id)
ticket1.customer_id = customer2.id
ticket1.update
print(ticket1.customer_id)

# Ticket.delete_all()
# Screening.delete_all()
# Film.delete_all()
# Customer.delete_all()

customers = film1.which_customers()
print([customer.name for customer in customers])
print(film1.how_many_customers())

print(film1.most_popular_screening_using_sql())

