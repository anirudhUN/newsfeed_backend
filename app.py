from flask import Flask
from flask_cors import CORS
from api.api import bp as api_bp

app = Flask(__name__)
CORS(app, origins='http://localhost:3000', methods=['GET', 'POST'], allow_headers=['Content-Type'])
app.register_blueprint(api_bp)

if __name__ == '__main__':
    app.run(debug=True, port=8000)
 