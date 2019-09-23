from flask import Flask, render_template, flash, redirect
from config import Config
import forms

app = Flask(__name__)
app.config.from_object(Config)

@app.route('/')
def index():
    return 'No main page yet!'

@app.route('/setup', methods=['GET', 'POST'])
def setup():
    form = forms.SetupForm()
    if form.validate_on_submit():
        flash('Field Setup')
        return redirect('/')

    print("rendering form")
    return render_template('setup.jinja', title='Setup',form=form)