from flask import Flask, render_template, jsonify
from flask_cors import CORS
from random import randint

app = Flask(__name__,
            static_folder = "./dist",
            template_folder = "./dist")

CORS(app, resources={r'/*': {'origins': '*'}})

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/api/tweet', methods=['GET'])
def tweet():
    response = {
        'tweet': randint(1, 100)
    }
    return jsonify(response)


if __name__ == "__main__":
    app.run(debug=True)