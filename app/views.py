import os
from flask import session,render_template, request, redirect, url_for, jsonify,flash
SECRET_KEY="secretkeysecretkeytwice2"
from random import randint
from werkzeug.utils import secure_filename
from app.models import UserProfile
from sqlalchemy.sql import exists
from datetime import *
from app import app,db
from flask_wtf.file import FileField, FileRequired
import time




@app.route('/profile/',methods = ['GET'])
def add_profile_GET():
    return render_template('profileform.html',form=form)
    
@app.route('/profile/',methods = ['POST'])
def add_profile_POST():
    form = ProfileForm(csrf_enabled=False)
    if request.method == 'POST':
        if form.validate_on_submit():
            f_name = request.form['f_name'].strip()
            l_name = request.form['l_name'].strip()
            gender = request.form['gender']
            age = request.form['age']
            image = request.files['image']
            bio = request.form['bio'].strip()
            while True:
                u_id = randint(0000,9999)
                if not db.session.query(exists().where(UserProfile.u_id == str(u_id))).scalar():
                    break
            filename = secure_filename(image.filename)
            image.save(os.path.join('app/static/uploads', filename))
            created_on = datetime.now()
            user_profile = UserProfile(u_id,f_name,l_name,gender,age,filename,created_on)
            db.session.add(user_profile)
            db.session.commit()
            flash("User Successfully Added", category='success')
            return redirect('/profiles')
    return render_template('profileform.html',form=form)
    
    
@app.route('/profiles', methods=["GET", "POST"])
def profiles():
  users = db.session.query(UserProfile).all()
  userlst=[]
  for user in users:
    userlst.append({'username':UserProfile.f_name+' '+UserProfile.l_name,'userid':UserProfile.u_id})
    if request.method == 'POST' and request.headers['Content-Type']== 'application/json':
        return jsonify(users=userlst)

@app.route('/profile/<u_id>', methods=['GET'])
def ind_profile(u_id):
  user = UserProfile.query.filter_by(u_id=u_id).first()
  if not user:
      flash("User not found" , category="error")
  else:
      image = '/static/uploads/' + user.image
      user = {'id':user.u_id,'image':image, 'username':user.f_name+' '+user.l_name,'first_name':user.f_name, 'last_name':user.l_name,'age':user.age, 'gender':user.gender,'bio':user.bio,'created_on':times(user.created_on)}
      return render_template('profile.html', user=user)
  return redirect(url_for("profiles"))    


@app.route('/profile/<userid>', methods=['POST'])
def indv_profile(u_id):
  user = UserProfile.query.filter_by(u_id=u_id).first()
  if not user:
      flash("User not found" , category="error")
  else:
      image = '/static/uploads/' + user.image
      if request.method == 'POST' and request.headers['Content-Type']== 'application/json':
            return jsonify(u_id=user.u_id, image=image,username=user.username, sex=user.sex, age=user.age,created_on=user.created_on)
      else:
            user = {'id':user.u_id,'image':image, 'username':user.f_name+' '+user.l_name,'first_name':user.f_name, 'last_name':user.l_name,'age':user.age, 'gender':user.gender,'bio':user.bio,'created_on':times(user.created_on)}
            return render_template('profile.html', user=user)
  return redirect(url_for("profiles"))
  
  
@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=600'
    return response
    
def times(entry):
    day = time.strftime("%a")
    month = time.strftime("%b")
    year = time.strftime("%Y")
    return day + " " + month + " " + year

@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port="8080")
