from flask import render_template, flash, redirect, url_for, request
from flask_login import login_user, logout_user, current_user, login_required
from werkzeug.urls import url_parse
from app import app, db, metrics, Counter
from app.forms import LoginForm, RegistrationForm, EditProfileForm, AlimentsForm
from app.models import User, Aliment
from datetime import datetime

metrics.info('app_info', 'Application info', version='1.0.3')

@app.before_request
def before_request():
    if current_user.is_authenticated:
        current_user.last_seen = datetime.utcnow()
        db.session.commit()



@app.route('/')
@app.route('/index')
@login_required
def index():
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', title='Home', posts=posts)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route('/user/<username>')
@login_required
def user(username):
    user = User.query.filter_by(username=username).first_or_404()
    user_aliments = user.aliments.order_by(Aliment.aliment_name)
    return render_template('user.html', user=user, user_aliments=user_aliments)

@app.route('/delete_aliment/<int:aliment_id>', methods=['POST'])
@login_required
def delete_aliment(aliment_id):
    aliment_to_delete = Aliment.query.get(aliment_id)
    db.session.delete(aliment_to_delete)
    db.session.commit()
    flash('Congratulations, you deleted an aliment !')
    return redirect(url_for('user', username=current_user.username))



@app.route('/edit_profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
    form = EditProfileForm()
    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.about_me = form.about_me.data
        db.session.commit()
        flash('Your changes have been saved.')
        return redirect(url_for('edit_profile'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.about_me.data = current_user.about_me
    return render_template('edit_profile.html', title='Edit Profile',
                           form=form)




aliments_added = Counter('aliments_added', 'Number of aliments added')
@app.route('/newaliment', methods=['GET', 'POST'])
@login_required
def newaliment():
    form = AlimentsForm()
    if form.validate_on_submit():
        aliment = Aliment(aliment_name = form.aliment_name.data, description = form.description.data, author=current_user )
        db.session.add(aliment)
        db.session.commit()
        aliments_added.inc()
        print ("")
        flash('Congratulations, you added a new aliment !')
        return redirect(url_for('newaliment'))
    return render_template('newAliment.html', title='NewAliment', form=form)

@app.route('/explorealiments', methods=['GET', 'POST'])
def explorealiments():
    get_aliments = Aliment.query.order_by(Aliment.id)
    return render_template('aliments.html', title='explorealiments', get_aliments=get_aliments)
