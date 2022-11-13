import os

import flask
import openai
from flask import Flask, request
from markupsafe import Markup

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")


def generate_completions(prompt: str, n: int):
    return openai.Completion.create(
        model="text-davinci-002",
        prompt="Write a poem about {}\n".format(prompt),
        temperature=0.60,
        max_tokens=1000,
        top_p=1,
        frequency_penalty=1,
        presence_penalty=1,
        n=n
    )


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return flask.render_template('index.html')
    if request.method == 'POST':
        prompt = request.form['prompt']
        n = int(request.form.get('n', 5))
        completions = generate_completions(prompt=prompt, n=n)
        results = [Markup(c['text']) for c in completions['choices']]
        return flask.render_template('index.html', prompt=prompt, results=results)


if __name__ == '__main__':
    app.run()
