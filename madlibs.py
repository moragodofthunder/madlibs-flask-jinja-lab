"""A madlib game that compliments its users."""

from random import choice, sample

from flask import Flask, render_template, request

# "__name__" is a special Python variable for the name of the current module.
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    "awesome",
    "terrific",
    "fantastic",
    "neato",
    "fantabulous",
    "wowza",
    "oh-so-not-meh",
    "brilliant",
    "ducky",
    "coolio",
    "incredible",
    "wonderful",
    "smashing",
    "lovely",
]


@app.route("/")
def start_here():
    """Display homepage."""

    return "Hi! This is the home page."


@app.route("/hello")
def say_hello():
    """Say hello to user."""

    return render_template("hello.html")


@app.route("/compliment")
def greet_person():
    """Greet user asking if they want to play game."""

    player = request.args.get("person")

    # compliment = choice(AWESOMENESS)

    return render_template("compliment.html", person=player)

@app.route("/game")
def show_madlib_form():
    """Show MadLib form if user wants to play game."""

    play_choice = request.args.get("play")

    if play_choice == "no":
        return render_template("goodbye.html")
    else:
        return render_template("game.html")

@app.route("/madlib")
def show_madlib():

    subject = request.args.get("person")
    color = request.args.get("colors")
    noun = request.args.get("nouns")
    adverb = request.args.get("adverb")
    
    TOWNS = ["Berlin", "Budapest", "London", "Paris",
    "Prague", "Sao Paulo", "Krakow", "Honolulu"]

    BODYPARTS = ["arm", "leg", "head", "face", "butt", "back"]

    towns = sample(TOWNS, 1)
    bodyparts = sample(BODYPARTS, 1)

    return render_template("madlib.html", subject=subject, color=color, 
    noun=noun, adverb=adverb, towns=towns, bodyparts=bodyparts)


if __name__ == "__main__":
    # Setting debug=True gives us error messages in the browser and also
    # "reloads" our web app if we change the code.

    app.run(debug=True, host="0.0.0.0")
