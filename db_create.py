from app import db
from models import BlogPost

# create the database and the db tables
db.create_all()

# insert
db.session.add(BlogPost("Good", "I\'m doing good"))
db.session.add(BlogPost("well", "I\'m doing well"))

# commit the changes
db.session.commit()
