from flask import Flask, render_template, redirect, flash
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet
from forms import PetForm

app = Flask(__name__)

app.debug = True
app.config ['SECRET_KEY'] = 'petadoptionsecretkey'
app.config ['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
toolbar = DebugToolbarExtension(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adopt'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

with app.app_context():
    connect_db(app)
    db.create_all()

@app.route('/')
def show_pet_homepage():
    """Show list of pets for adoption"""
    pets = Pet.query.order_by(Pet.species, Pet.name).all()

    return render_template('homepage.html', pets=pets)

@app.route('/add', methods=["GET", "POST"])
def add_pet():
    """Show + handle add pet form"""
    form = PetForm()

    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        age = form.age.data
        photo_url = form.photo_url.data
        notes = form.notes.data

        new_pet = Pet(name=name, species=species, age=age, photo_url=photo_url, notes=notes)

        db.session.add(new_pet)
        db.session.commit()

        flash(f"{new_pet.name} added.")

        return redirect('/')
    else:
        return render_template('add_pet_form.html', form=form)
    
@app.route('/<int:pet_id>')
def show_pet_detail_page(pet_id):
    """Show the pet detail page"""
    pet = Pet.query.get_or_404(pet_id)

    return render_template('pet_detail.html', pet=pet)

@app.route("/<int:pet_id>/edit", methods=["GET", "POST"])
def edit_pet(pet_id):
    """Show and handle edit pet form"""

    pet = Pet.query.get_or_404(pet_id)
    form = PetForm(obj=pet)

    if form.validate_on_submit():
        pet.name = form.name.data
        pet.species = form.species.data
        pet.age = form.age.data
        pet.notes = form.notes.data

        db.session.commit()

        flash(f"{pet.name} updated.")

        return redirect(f"/{pet.id}")
    
    else:
        return render_template("edit_pet_form.html", form=form)
