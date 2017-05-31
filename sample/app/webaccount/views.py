from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_required, login_user, LoginManager, logout_user
from werkzeug.security import generate_password_hash, check_password_hash

from .forms import LoginForm
# from ..models import Account
from .. import db
from .forms import LoginForm, RegisterForm

w = Blueprint('webaccount', __name__, template_folder='app/templates', static_folder='app/static')

webaccount_login_manager = LoginManager()
webaccount_login_manager.blueprint_login_views = '/webaccount/login'
webaccount_login_manager.login_view ='/webaccount/login'

@w.record_once
def on_load(state):
    webaccount_login_manager.init_app(state.app)

@webaccount_login_manager.user_loader
def load_user(user_id):
    # return Account.query.get(int(user_id))
    pass

@w.route('/login', methods=['GET', 'POST'])
def webaccount_login():
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
    return render_template('webaccount-login.html', form=form)


@w.route('/logout/')
@login_required
def logout():
    pass

@w.route('/home')
# @login_required
def home():
    return render_template('webaccount-index.html')

# check if login_required is successfull
@w.route('/success')
@login_required
def success():
    return '<h1>Success</h1>'
