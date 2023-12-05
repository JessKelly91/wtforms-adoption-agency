from models import db, Pet
from app import app

#Create all tables
with app.app_context():
    db.drop_all()
    db.create_all()

    Pet.query.delete()

    Woofly = Pet(name="Woofly", species="dog", age=3, photo_url="https://www.akc.org/wp-content/uploads/2017/11/Entlebucher-Mountain-Dog-outdoors-standing-in-a-field.jpg")

    Meowser = Pet(name="Meowser", species="cat", age=2, photo_url="https://www.shutterstock.com/image-photo/looking-me-please-random-candid-600w-372320605.jpg")
    
    Spike = Pet(name="Spike", species="porcupine", age=5, photo_url="https://lindsaywildlife.org/wp-content/uploads/2016/10/Penelope-For-Her-Page-scaled.jpg")

    db.session.add_all([Woofly, Meowser, Spike])
    db.session.commit()