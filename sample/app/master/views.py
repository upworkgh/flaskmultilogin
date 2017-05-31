from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_required, login_user, LoginManager, logout_user
from werkzeug.security import generate_password_hash, check_password_hash

# from ..models import Account
from .. import db
from .forms import LoginForm, RegisterForm, WebAccountRegisterForm

m = Blueprint('Master', __name__, template_folder='app/templates', static_folder='app/static')

master_login_manager = LoginManager()
master_login_manager.blueprint_login_views = '/master/login'
master_login_manager.login_view ='/master/login'

@m.record_once
def on_load(state):
    master_login_manager.init_app(state.app)

@master_login_manager.user_loader
def load_user(user_id):
    # return Account.query.get(int(user_id))
    pass

@m.route('/sign-up', methods=['GET', 'POST'])
def signup():
    form = RegisterForm()
    if form.validate_on_submit():
        '''
        Sample: 

        hashed_password = generate_password_hash(form.password.data, method='sha256')
        new_account = Account(email=form.email.data, password=hashed_password)
        db.session.add(new_account)
        db.session.commit()
        return redirect(url_for('.master_login'))
        '''
    return render_template('master-signup.html', form=form)

@m.route('/login', methods=['GET', 'POST'])
def master_login():
    form = LoginForm()
    if form.validate_on_submit():
        '''
        Sample: 

        user = Account.query.filter_by(email=form.email.data).first_or_404()
        if user:
            if check_password_hash(user.password, form.password.data):
                login_user(user, remember=form.remember.data)
                return redirect(url_for('.home'))
        return '<h1>Invalid email or password</h1>'
        '''
    return render_template('master-login.html', form=form)

@m.route('/webaccount-sign-up', methods=['GET', 'POST'])
def webaccount_signup():
    form = RegisterForm()
    if form.validate_on_submit():
        '''
        Sample: 

        hashed_password = generate_password_hash(form.password.data, method='sha256')
        new_account = Account(email=form.email.data, password=hashed_password)
        db.session.add(new_account)
        db.session.commit()
        return redirect(url_for('.master_login'))
        '''
    return redirect(url_for(home))

@m.route('/logout/')
@login_required
def logout():
    pass

@m.route('/home')
# @login_required
def home():
    form = WebAccountRegisterForm()
    return render_template('master-index.html', form=form)
