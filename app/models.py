from . import db
import datetime

class UserProfile(db.Model):
    u_id = db.Column(db.Integer, primary_key=True)
    f_name = db.Column(db.String(80),nullable = False)
    l_name = db.Column(db.String(80),nullable = False)
    gender = db.Column(db.String(10),nullable = False)
    age = db.Column(db.Integer,nullable = False)
    image = db.Column(db.String(50),nullable = False)
    profile_added_on = db.Column(db.DateTime, nullable = False)

    def __init__(self,u_id,f_name,l_name,gender,age,image,profile_added_on):
        self.u_id = u_id
        self.f_name = f_name
        self.l_name = l_name
        self.gender = gender
        self.age = age
        self.image = image
        self.profile_added_on = profile_added_on
        
    
    def __repr__(self):
        return '<User %r %r>' % self.f_name %self.l_name