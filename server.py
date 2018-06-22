# server.py
from flask import Flask, render_template, jsonify
from web_scrape import Event

#app = Flask(__name__, static_folder="../static/dist", template_folder="../static")
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/event")
def event():
    event = Event()
    return jsonify(event.event_group_a) 


if __name__ == "__main__":
    app.run()