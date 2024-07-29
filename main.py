from database.database_interface import DatabaseInterface
from models.album import Album
from models.person import Person
from models.listener import Listener

pete = Listener("pete", "pete@help.com", "06/02/1999", "jst chilin")

db = DatabaseInterface("csv")

db.add_object(pete)
test = db.get_object(Listener, 1)
print(test)