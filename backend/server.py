from flask import Flask, render_template, jsonify
from random import randint

app = Flask(__name__,
            static_folder = "../dist",
            template_folder = "../dist")


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/api/random')
def random_number():
    response = {
        'randomNumber': randint(1, 100)
    }
    return jsonify(response)


if __name__ == "__main__":
    app.run(debug=True)