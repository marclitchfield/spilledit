import os
import logging
from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

@app.route('/static/<path:path>')
def send_static(path):
    return send_from_directory('static', path)

@app.route("/")
def index():
    return render_template("index.html")


# setup output logging for gunicorn
handler = logging.StreamHandler()
handler.setLevel(logging.WARNING)
app.logger.addHandler(handler)

# fix gives access to the gunicorn error log facility
app.logger.handlers.extend(logging.getLogger("gunicorn.error").handlers)
