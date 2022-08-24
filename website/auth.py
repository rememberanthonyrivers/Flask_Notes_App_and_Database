# stores all url endpoints for the front end

from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User    #   this module is imported to use the internal User method    
from werkzeug.security import generate_password_hash, check_password_hash   #   imported to secure a password 
from . import db 
from flask_login import login_user, logout_user, login_required, current_user

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])

def login():

    if request.method == 'POST':    #if were signing in lets get the email and password from the form 
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()

        if user:
            if check_password_hash(user.password, password):
                flash('Successfull Login!', category='success')
                login_user(user, remember=True)

                return redirect(url_for('views.home'))

            else:
                flash('Incorrect password, Lets try again.', category='error')

        else:
            flash('Email not valid.', category='error')

    return render_template('login.html',user=current_user)


@auth.route('/logout')

@login_required

def logout():

    logout_user()

    return redirect(url_for('auth.login'))
    

@auth.route('/sign-up', methods=['GET', 'POST'])

def sign_up():

    if request.method == 'POST':    #   if the request is a post request...
        
        email = request.form.get('email')   #   now lets grab our form data and assign them to a var
        first_name = request.form.get('firstName')   #   now lets assign our form data to a var
        password1 = request.form.get('password1')   #   now lets assign our form data to a var
        password2 = request.form.get('password2')   #   now lets assign our form data to a var

        user = User.query.filter_by(email=email).first()

        #   below lets use control flow to figure out what to do with the user
        if user:
            flash('Account already exists.', category='error')
        elif len(email) < 4:
            flash('Email must be greater than 3 characters.', category='error')   
        elif len(first_name) < 2:
            flash('First name must be greater than 1 characters.')  
        elif password1 != password2:
            flash('Passwords don\'t match.' , category='error')         
        elif len(password1) < 7:
            flash('Password must be at least 7 characters.' ,category='error')        
        else:
            new_user = User(email=email, first_name=first_name, password=generate_password_hash(password1, method='sha256'))    # new instance of user 
            db.session.add(new_user)
            db.session.commit()
            login_user(user, remember=True)  
            flash('Account created!')
            #add user to database
            return redirect(url_for('views.home')) #once the account is created this method redirects the user to the homepage 

    return render_template('sign_up.html', user=current_user)