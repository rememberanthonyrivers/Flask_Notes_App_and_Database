# stores all url endpoints for the front end

from flask import Blueprint, render_template, request

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')

@auth.route('/logout')
def logout():
    return '<p>Logout</p>'

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':    #   if the request is a post request...
        email = request.form.get('email')   #   now lets grab our form data and assign them to a var
        firstname = request.form.get('firstName')   #   now lets assign our form data to a var
        password1 = request.form.get('password1')   #   now lets assign our form data to a var
        password2 = request.form.get('password2')   #   now lets assign our form data to a var

        #   below lets use control flow to figure out what to do with the user
        if len(email) < 4:
            pass
        elif len(firstname) < 2:
            pass
        elif password1 != password2:
            pass 
        elif len(password1) < 7:
            pass
        else: 
            #add user to database 
            pass


    return render_template('sign_up.html')