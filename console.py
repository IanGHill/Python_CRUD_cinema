import sys

sys.path.append('./db')
sys.path.append('./models')
from customer import *
from film import *
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
