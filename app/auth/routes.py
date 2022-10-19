from flask import Blueprint, render_template, request, redirect, url_for
from .forms import UserCreationForm
from app.models  import User
import requests

auth = Blueprint('auth', __name__, template_folder='auth_templates')

@auth.route('/login2')
def logMeIn():
    return render_template('login2.html')

@auth.route('/signup', methods=["GET", "POST"])
def signUp():

    form = UserCreationForm()
    if request.method == "POST":
        if form.validate():
            username = form.username.data

            print(username)
            
            # user = User(username)
            # user.saveToDB()
            
            url = f'https://pokeapi.co/api/v2/pokemon/{username}'
            requests.get(url)
            response = requests.get(url)
            if response.ok:
                pokemon_dict = {}
                name =  response.json()["name"]
                pokemon_dict[name] = {
                    'image' : response.json()["sprites"]["front_shiny"],
                    'abilities' : response.json()["abilities"][0],
                    'base_exp' : response.json()["base_experience"]
                }
            return render_template('login.html', pokemon_dict=pokemon_dict)
            #I tried to make this kinda self-explanatory but not sure if that would be the case
            #I would split the pokemon app off separately from the IG app for simplicity and keep the poke search aside from auth but it's up to you!

            

        return redirect(url_for('auth.signUp'))

    return render_template('signup.html', form=form)