import os

from flask import Flask
from flask_restful import Api
from resources.set import Set, SetList
from resources.tile import NewTile, Tile, TileList, TileSet

app = Flask(__name__)

app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

api = Api(app)

api.add_resources(Set, '/set/<string:name>')
api.add_resources(SetList, '/sets')

api.add_resources(NewTile, '/tile')
api.add_resources(Tile, '/tile/<int:tile_id>')
api.add_resources(TileList, '/tiles')
api.add_resources(TileSet, '/tiles/<int:set_id>')


if __name__ == '__main__':
    from db import db
    db.init_app(app)
    
    if app.config['DEBUG']:
        @app.before_first_request
        def create_tables():
            db.create_all()

    app.run(port=5000)




