from . import db
class User(db.Model):
    __tablename__="users"
    
    id= db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(255))
    email= db.Column(db.String(50))
    
    def __repr__(self):
        return f'User{self.username}'
    
class Pitch(db.Model):
    id=db.Column(db.Interger,primary_key=True)
    content=db.Column(db.String(255))
    likes=db.Column(db.Integer(4))
    dislikes=db.Column(db.Integer(4))
    
    def __repr__(self):
        return f'Pitch{self.content}'