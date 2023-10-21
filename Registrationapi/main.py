from flask import Flask, render_template, request,redirect,session
import mysql.connector   #using phyMyadmin
import os  #to use session 

app = Flask(__name__)
app.secret_key = os.urandom(24)  #creating a session of 24 long so that the user after login do not have to go to login page again and again unless the user logs out.
 # session is some thing that we use the same thing is being repeated,to avoid that we create session to store it.
 #once the session is expired user is logged out.


conn = mysql.connector.connect(host="Localhost",user='root',database='register and login')#to connect with data base in MySQL
cursor=conn.cursor()                                                 #databse name is register and login

# Login Page
@app.route('/')   #route for login page.
def login():
    return render_template('login.html')

#Register Page
@app.route('/register')
def about():
    return render_template('register.html')

#home page
# this login and registration API uses the idea where only logged in user can go to home page.
# ANy unlogged user cannot go to the home page with direct url entry.
#for home page user have to create account then they can go to home directly. and can also logout 
#and log in later.
@app.route('/home')
def home():
    if 'user_id' in session: #user id will only be sent when the person in logged in and will go to home page
        return render_template('home.html')
    else:
        return redirect('/') # if user_id is not in session then will be redirected to login.

#Login validation   -  if user email and password is in database then take to home page if not then redirect to login page
#in login page one can login if already created a account if not then create account option is available
@app.route('/login_validation', methods=['POST'])
def login_validation():
    email=request.form.get('email')
    password = request.form.get('password')
    cursor.execute("""SELECT * FROM `users` WHERE `email` LIKE '{}' AND `password` LIKE '{}'"""
                   .format(email,password))
    users = cursor.fetchall()      #email and password is assigned to users table

    if len(users)>0:
        session['user_id'] = users[0][0]   #this is list where the fisrt element of the first user_d is returning
        return redirect('/home')#if the usre_id is present in the database after register and go to home page
    else:
        return redirect('/')   #if the user_id is not present in the database then login with the correct email and password or create account
    
@app.route('/add_user', methods=['POST'])
def add_user():
    name = request.form.get('uname')
    email = request.form.get('uemail')
    password = request.form.get('upassword')

# inserting the name , email and password when registering in the table
    cursor.execute("""INSERT INTO `users` (`user_id`, `name`, `email`, `password`) VALUES
                   (NULL, '{}', '{}', '{}')""".format(name, email, password))
    conn.commit()  #to maintain dat integrity in database, like the transaction.

    cursor.execute("SELECT * FROM `users` WHERE `email` LIKE '%{}%'".format(email)) #email is unique
    myuser = cursor.fetchall()  #fetch the email from the table
    session['user_id'] = myuser[0][0]     #if email matches 
    return redirect('/home')            # then take to home page

#log out 
@app.route('/logout')
def logout():
    session.pop('user_id')  #after clicking on log out user can log out and the session for the user is expired.
    return redirect('/')   #will be redirected to login page again, after login session is again created for th user.

if __name__=='__main__':
    app.run(debug=True)
#THANK YOU!