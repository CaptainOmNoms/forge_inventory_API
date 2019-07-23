from flask_restful import Resource, reqparse
from models.tile import TileModel

class Tile(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('size',
                        type=str,
                        required=True,
                        help="You need to specify the size of this tile"
    )
    parser.add_argument('name',
                        type=str,
                        required=True,
                        help="You need to specify the name of this tile"
    )
    parser.add_argument('height',
                        type=str,
                        required=True,
                        help="You need to specify the height of this tile"
    )
    parser.add_argument('quantity',
                        type=int,
                        required=True,
                        help="How many do you have?"
    )
    parser.add_argument('set_name',
                        type=str,
                        required=True,
                        help="Every tile belongs to a set."
    )
    
    def get(self, tile_id):
        tile = TileModel.find_by_id(tile_id)
        
        if tile:
            return tile.json()
        return {'message': 'Tile not found'}, 404
        
    def put(self, tile_id):
        data = Tile.parser.parse_args()
        
        tile = TileModel.find_by_id(tile_id)
        
        if tile:
            tile.name = data['name']            
            tile.size = data['size']
            tile.height = data['height']
            tile.quantity = data['quantity']
        else:
            tile = TileModel(**data)
        
        tile.save_to_db()
        return tile.json()
            
    def delete(self, tile_id):
        tile = TileModel.find_by_id(tile_id)
        
        if tile:
            tile.delete_from_db()
            return {'message': 'Tile deleted'}
        
        return {'message': 'Tile not found'}, 404
        

class NewTile(Resource):
    def post(self):
        data = Tile.parser.parse_args()
        
        if TileModel.find_by_set_name_size_height(data['set_name'], data['name'], data['size'], data['height']):
            return {'message': 'That tile already exists'}, 400
            
        tile = TileModel(**data)
        
        try:
            tile.save_to_db()
        except:
            return {'message': 'An error occurred while creating that tile'}, 500
        
        return tile.json(), 201

        
class TileList(Resource):
    def get(self):
        return {'tiles': [tile.json() for tile in TileModel.query.all()]}
        
       
class TileSet(Resource):
    def get(self, set_name):
        return {'tiles': [tile.json() for tile in TileModel.find_by_set(set_name)]}
        
         
