import os
from jinja2 import Template
import requests
from bs4 import BeautifulSoup
from flask import (
    Flask,
    make_response,
    request,
    redirect,
    url_for
)
import utils

API_KEY = os.environ["VOICERSS_API_KEY"]
app = Flask(__name__)
INDEX_PATH = os.path.join(utils.STATIC_PATH, 'index.html')
with open(INDEX_PATH) as f:
    INDEX_TEMPLATE = Template(f.read())


@app.route('/')
def home():
    content = INDEX_TEMPLATE.render({
        "speech_response": False,
        "text": ""
    })
    return make_response(content)


@app.route('/text')
def play_text():
    text = request.args.get('text')
    voice = utils.speech({
        'key': API_KEY,
        'hl': 'en-us',
        'src': text,
        'r': '0',
        'c': 'mp3',
        'f': '44khz_16bit_stereo',
        'ssml': 'false',
        'b64': 'true'
    })
    content = INDEX_TEMPLATE.render({
        "speech_response": voice['response'],
        "text": text
    })
    return make_response(content)


@app.route('/article')
def play_article():
    url = request.args.get('url')
    content = requests.get(url).text
    soup = BeautifulSoup(content)
    article_body = utils.fetch_article_body(soup)
    return redirect(url_for('play_text', text=article_body))

if __name__ == "__main__":
    app.run()
