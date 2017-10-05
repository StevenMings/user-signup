from flask import Flask, request, redirect, render_template
import cgi
import os

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/')
def index():
    return render_template('signup.html')


@app.route('/validate-signup', methods=['POST'])
def validate_signup():

    username = request.form['username']
    password = request.form['password']
    verify = request.form['verify']
    email = request.form['email']

    username_error = ""
    password_error = ""
    verify_error = ""
    email_error = ""

# Username
    if len(username) > 20 or len(username) < 3:
        username_error = "Username value out of range (Between 3 - 20 Characters Only)"

    if " " in username:
        username_error = "Spaces are not allowed"

    if len(username) == 0:
        username_error = "This cannot be blank!"


    
# Password
    if len(password) > 20 or len(password) < 3:
        password_error = "Password value out of range (Between 3 - 20 Characters Only)"

    if " " in password:
        password_error = "Spaces are not allowed"

    if len(password) == 0:
        password_error = "The Password cannot be blank!"

    
# Password Verify    
    if password != verify:
        verify_error = "The passwords Do not match!"

    if len(verify) > 20 or len(verify) < 3:
        verify_error = "Password value out of range (Between 3 - 20 Characters Only)"

    if " " in verify:
        verify_error = "Spaces are not allowed"

    if len(verify) == 0:
        verify_error = "The Password be blank!"

    
#Email
    if not email =="":
        if "@" not in email:
            email_error = "E-mail address needs one '@'"
        if "." not in email:
            email_error = "E-mail address needs one '.'"
        if " " in email:
            email_error = "Spaces are not allowed"
        if len(email) > 20 or len(email) < 3:
            email_error = "E-mail value out of range (Between 3 - 20 Characters Only)"

        
        
    if not username_error and not password_error and not verify_error and not email_error:
        return redirect('/valid-signup?username={0}'.format(username))
    else:
        return render_template('signup.html', username_error=username_error, username=username, password_error=password_error, verify_error=verify_error, email_error=email_error, email=email)

@app.route('/valid-signup')
def valid_signup():
    username = request.args.get('username')
    return '<h1>Thanks For Signing Up, {0}! </h1>'.format(username)


app.run()