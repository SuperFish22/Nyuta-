from threading import Thread
import sqlite3
from flask import Flask, render_template, request

temp = {
    
}

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():

    return render_template('index.html', **temp)


def ServerStart():
    print("Start server")
    app.run(host ="0.0.0.0", port=5000)

if __name__ == "__main__":
    ServerStart()