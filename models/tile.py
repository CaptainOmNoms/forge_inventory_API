from db import db

class TileModel(db.Model):
    __tablename__ = 'tiles'
    
    tile_id = db.Column(db.Integer, primary_key=True)
    size = db.Column(db.String(4))
    height = db.Column(db.String(8))
    name = db.Column(db.String(16))
    quantity = db.Column(db.Integer)
    
    set_name = db.Column(db.String(32), db.ForeignKey('sets.set_name'))
    set = db.relationship('SetModel')
    
    def __init__(self, size, name, height, quantity, set_name):
        self.size = size
        self.name = name
        self.height = height
        self.quantity = quantity
        self.set_name = set_name

    def json(self):
        return {
            'tile_id': self.tile_id,
            'size': self.size,
            'name': self.name,
            'height': self.height,
            'qty': self.quantity,
            'set': self.set_name
        }

    @classmethod
    def find_by_id(cls, tile_id):
        return cls.query.filter_by(tile_id=tile_id).first()

    @classmethod
    def find_by_set(cls, set_name):
        return cls.query.filter_by(set_name=set_name).all()

    @classmethod
    def find_by_set_name_size_height(cls, set_name, name, size, height):
        return cls.query.filter_by(set_name=set_name).filter_by(name=name).filter_by(size=size).filter_by(height=height).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
