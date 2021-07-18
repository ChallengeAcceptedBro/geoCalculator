from flask import Flask

app = Flask(__name__)

from geo_blueprint import geo_blueprint
app.register_blueprint(geo_blueprint, url_prefix='/geo')


@app.route('/')
def index():
     return 'Привет всем'


if __name__ == '__main__':
    app.run(debug=True)
