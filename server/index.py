from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
app.config['CORS_HEADERS'] = 'Content-Type'
CORS(app)


@app.route("/", methods=["GET"])
def health_check():
    return "Hello World"


if __name__ == 'main':
    app.run()
