from flask import Flask, render_template, redirect
# from pymongo import MongoClient

# client = MongoClient('localhost', 27017)

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, port=5001)