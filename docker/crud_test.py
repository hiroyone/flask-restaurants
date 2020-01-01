# Reminder to test CRUD operations to the created database

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Restaurant, Base, MenuItem

engine = create_engine('sqlite:///restaurantmenu.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()

## Read
# Retrieve Menu for all
items = session.query(MenuItem).all()
print(items)
for item in items:
    print(item.name)
    print(item.description)
    print('\n')

# Read first Menu
item = session.query(MenuItem).first()
print(item.name)
print(item.description)
print('\n')

# Update menus
veggieBurgers = session.query(MenuItem).filter_by(name='Veggie Burger')
print('List all veggie burgers')
for veggieBurger in veggieBurgers:
    print(veggieBurger.restaurant.name)
    print(veggieBurger.id)
    print(veggieBurger.price)
    print('\n')

urbanVeggieBurger = session.query(MenuItem).filter_by(id=9).one()
if urbanVeggieBurger.price == '$2.99':
    None
else:
    urbanVeggieBurger.price = '$2.99'
session.add(urbanVeggieBurger)
session.commit()

## Delete menu
spinach = session.query(MenuItem).filter_by(name='Spinach Ice Cream').first()
NoneType = type(None)
if type(spinach) is NoneType:
    None
else:
    session.delete(spinach)
    session.commit()


