import sys

from db.db_setup import DBSetup
from models.customer import Customer

sys.path.append('./db')
sys.path.append('./models')
# from customer import *
# from db_setup import *

DBSetup.set_up_tables()

neil = Customer("Neil", 35.50)
neil.save()
print(neil.name)
print(neil.id)
print(neil.funds)
