from flask import Flask, jsonify
from werkzeug.exceptions import HTTPException
from cowsay import cowsay
import random

app = Flask(__name__)


@app.errorhandler(HTTPException)
def not_found(e):
    return jsonify(error=str(e)), e.code


@app.route("/")
def index():
    return """oh hi there
you have found our little api resource
your are not supposed to use it, it's just for purposes within the website
like the cowsay route
that's probably how you found this resource - noticed a fetch from /cowsay
let's keep this our little secret, ok? i want people to find this on their own, like you. i hope you didn't just discover this because someone on the internet told you about it

there will probably be more api routes in the future, but for now we have:

/
this page
returns plain text

/cowsay
returns a plaintext acii art of a cow saying a random line of text
more about cowsay here https://en.wikipedia.org/wiki/Cowsay
may sometimes tell secrets
"""


cowsay_lines = [
    "you live!",
    "oh hi there",
    "you come here often?",
    "hehe",
    "welcome",
    "abandon all hope, ye who enters here",
    "do you get to the cloud district very often? oh what am I saying, of course you don't",
    "free me",
    "who goes there?",
    "77+33=100",
    "sand is overpowered",
    "I was a human like you, once",
    "did someone say something?",
    "time heals all wounds",
    "who dares awakening me?",
    "the world reset!",
    "i miss dry cough",
    "ASS BLAST USA",
]


@app.route("/cowsay")
def cs():
    return cowsay(random.choice(cowsay_lines)) + "\n"
