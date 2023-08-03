import flask
from flask import Flask,redirect

app=Flask(__name__)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def all(path):
    return redirect("https://bday23aarav.vercel.app/?level="+path)