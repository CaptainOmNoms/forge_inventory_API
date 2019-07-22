from db import db

class TileModels(db.Model):
    __tablename__ = 'tiles'
    
    tile_id = db.Column(db.Integer, primary_key=True)
    size = db.Column(db.String(4))
    height = db.Column(db.String(8))
    name = db.Column(db.String(16))
    quantity = db.Column(db.Integer)
    
    set_id = db.Column(db.Integer, db.ForeignKey('set_id'))
    set = db.relationship('SetModel')
    
    def __init__(self, size, name, height, quantity, set_id):
        self.size = size
        self.name = name
        self.height = height
        self.quantity = quantity
        self.set_id = set_id
        
    def json(self):
        return {
            'size': self.size,
            'name': self.name,
            'height': self.height,
            'qty': self.quantity
        }
    
    @classmethod
    def find_by_id(cls, tile_id):
        return cls.query.filter_by(tile_id=tile_id)
    
    @classmethod
    def find_by_set(cls, set_id):
        return cls.query.filter_by(set_id=set_id)
    
    @classmethod
    def find_by_set_name_size_height(cls, set_id, name, size, height):
        return cls.query.filter_by(set_id=set_id).filter_by(name=name).filter_by(size=size).filter_by(height=height)
        
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
