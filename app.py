import os

from flask import Flask
from flask_restful import Api
from resources.set import Set, SetList
from resources.tile import NewTile, Tile, TileList, TileSet
from db import db

app = Flask(__name__)

app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['PROPAGATE_EXCEPTIONS'] = True

api = Api(app)

api.add_resource(Set, '/set/<string:name>')
api.add_resource(SetList, '/sets')

api.add_resource(NewTile, '/tile')
api.add_resource(Tile, '/tile/<int:tile_id>')
api.add_resource(TileList, '/tiles')
api.add_resource(TileSet, '/tiles/<string:set_name>')

@app.before_first_request
def create_tables():
    db.create_all()

db.init_app(app)

if __name__ == '__main__':
    app.run(port=5000)




