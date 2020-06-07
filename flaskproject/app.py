from flaskproject import app, db
from flask import render_template, redirect,request,url_for,flash,abort
from flask_login import login_user,login_required,logout_user
from flaskproject.models import User
from flaskproject.forms import LoginForm, RegistrationForm

# home page
@app.route('/')
def home():
    return render_template('home.html')


# User entry home page 
@app.route('/entry')
# Login required to enter user home page
@login_required
def user_entry():
    return render_template('entry.html')


# User logout
@app.route('/logout')
# Login required to logout
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))



# User login view
@app.route('/login',methods=['GET','POST'])
def login():

    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        # Verifying password and checks if user excist
        if user.check_password(form.password.data) and user is not None:

            login_user(user)
            # saves request before login as next
            next = request.args.get('next')

            if next == None or not next[0] == '/':
                next = url_for('user_entry')
            
            return redirect(next)
    return render_template('login.html',form=form)


# Register view
@app.route('/register',methods=['GET','POST'])
def register():

    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email=form.email.data,password=form.password.data)

        db.session.add(user)
        db.session.commit()
        return redirect(url_for('login'))

    return render_template('register.html',form=form)

if __name__== '__main__':
    app.run(debug=True)