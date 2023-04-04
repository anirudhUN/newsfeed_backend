from flask import Flask
from api.api import bp as api_bp

app = Flask(__name__)
app.register_blueprint(api_bp)

if __name__ == '__main__':
    app.run(debug=True, port=8000)
