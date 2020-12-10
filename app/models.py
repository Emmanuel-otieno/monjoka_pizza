from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager
from datetime import datetime
from . import db

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(UserMixin,db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255),index =True)
    firstname = db.Column(db.String(255))
    lastname = db.Column(db.String(255))
    email = db.Column(db.String(255),unique = True,index = True)
    pass_secure = db.Column(db.String(255))
    date_joined = db.Column(db.DateTime,default=datetime.utcnow)

    pizzas = db.relationship('Pizza',backref = 'user',lazy = "dynamic")


    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self,password):
        self.pass_secure = generate_password_hash(password)

    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)

    def __repr__(self):
        return f'User {self.username}'


class Pitch(db.Model):
    __tablename__ = 'orders'

    id = db.Column(db.Integer,primary_key = True)
    pitch_content = db.Column(db.String(255))
    category = db.Column(db.String)
    posted = db.Column(db.DateTime,default=datetime.utcnow)
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))
   
    comments = db.relationship('Comment',backref =  'pitch_id',lazy = "dynamic")

    def save_order(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_orders(cls,category):
        orders = Pitch.query.filter_by(category=category).all()
        return orders

    @classmethod
    def get_order(cls,id):
        order = Pitch.query.filter_by(id=id).first()

        return order              
