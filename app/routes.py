from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm

def generate_sidenav_list():

    items = []

    items.append({"type":"link", "name": "Index", "url": url_for("index"), "contents": f"""<span class="material-symbols-outlined sidebar-symbols">home</span>Index"""})
    items.append({"type":"link", "name": "Patients", "url": url_for("index"), "contents": f"""<span class="material-symbols-outlined sidebar-symbols">group</span>Patients"""})
    items.append({"type":"link", "name": "Add Stroke", "url": url_for("addstroke"), "contents": f"""<span class="material-symbols-outlined sidebar-symbols">person_add</span>Add Stroke"""})
    items.append({"type":"link", "name": "Reports", "url": url_for("index"), "contents": f"""<span class="material-symbols-outlined sidebar-symbols" style="font-size: 22px">monitoring</span>Reports"""})

    return items

@app.route('/')
@app.route('/index')
def index():
    items = generate_sidenav_list()
    selected = 'Index'
    user = {'username': 'Zoe', 'fullname': 'Zoe Yang'}
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
    return render_template('index.html', title='Home', user=user, posts=posts, items = items, selected = selected)

@app.route('/login', methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect('/index')
    return render_template('login.html', title='Sign In', form=form)

@app.route('/demographics', methods = ['GET', 'POST'])
def demographics():
    items = generate_sidenav_list()
    selected = 'Demographics'
    return render_template('demographics.html', title = 'Demographics', items = items, selected = selected)

@app.route('/addstroke', methods = ['GET', 'POST'])
def addstroke():
    items = generate_sidenav_list()
    selected = 'Add Stroke'
    user = {'username': 'Zoe', 'fullname': 'Zoe Yang'}
    
    return render_template('addstroke.html', title=selected, user=user, items = items, selected = selected)

