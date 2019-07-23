from  flask_restful import Resource, reqparse
from models.set import SetModel

class Set(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('description',
                        type=str,
                        required=True,
                        help="Just a short description of this set"
    )
    
    
    def get(self, name):
        set = SetModel.find_by_name(name)
        
        if set:
            return set.json()
        return {'message': 'Set not found'}, 404
        
    def post(self, name):
        data = self.parser.parse_args()
        
        if SetModel.find_by_name(name):
            return {'message': "A set with name '{}' already exists.".format(name)}, 400
        
        set = SetModel(name, data['description'])
        
        try:
            set.save_to_db()
        except:
            return{'message': "An error occurred while creating the set '{}'.".format(name)}, 500
        
        return set.json(), 201
        
    def delete(self, name):
        set = SetModel.find_by_name(name)
        if set:
            set.delete_from_db()
            return {'message': 'Set deleted'}
            
        return {'message': 'Set not found'}, 404
        
    def put(self, name):
        data = self.parser.parse_args()
        
        set = SetModel.find_by_name(name)
        
        if set:
            set.description = data['description']
        else:
            set = SetModel(name, data['description'])
            
        set.save_to_db()
        return set.json(), 201  
        
        
class SetList(Resource):
    def get(self):
        return {'sets': [set.json() for set in SetModel.query.all()]}
