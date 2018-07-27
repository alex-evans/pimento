# server.py
from flask import Flask, render_template, jsonify, request
from web_scrape import Event

#app = Flask(__name__, static_folder="../static/dist", template_folder="../static")
app = Flask(__name__)

@app.route("/")
def index():
    return print("running")


@app.route("/event")
def event():
    event = Event()
    players = {
        "A": event.event_group_a,
        "B": event.event_group_b,
        "C": event.event_group_c,
        "D": event.event_group_d
    }      
    return jsonify(players)


#--------------------------------------------------------------------------
# allows CORS
#--------------------------------------------------------------------------
def add_cors_headers(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    if request.method == 'OPTIONS':
        response.headers['Access-Control-Allow-Methods'] = 'DELETE, GET, POST, PUT'
        headers = request.headers.get('Access-Control-Request-Headers')
        if headers:
            response.headers['Access-Control-Allow-Headers'] = headers
    return response
app.after_request(add_cors_headers)


if __name__ == "__main__":
    app.run()