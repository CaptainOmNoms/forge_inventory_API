from db import db

class SetModel(db.Model):
    __tablename__ = 'sets'
    
    set_id = db.Column(db.Integer, primary_key=True)
    set_name = db.Column(db.String(32))
    description = db.Column(db.String(128))
   
    def __init__(self, name, description):
        self.set_name = name
        self.description = description
        
    def json(self):
        return {
            'id': self.set_id,
            'set_name': self.set_name,
            'description': self.description
        }
        
    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(set_id=_id).first()
        
    @classmethod
    def find_all(cls):
        return cls.query.all()
        
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()    
    
