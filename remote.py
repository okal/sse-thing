import time
from flask import Flask, url_for, render_template, Response

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/remote')
def source():
    def generate():
        while True:
            time.sleep(1)
            yield "event: ping\ndata: {}\n\n".format(time.time())
    return Response(generate(), mimetype="text/event-stream")