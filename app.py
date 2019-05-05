from flask import Flask, render_template, url_for, redirect
from forms import LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'asdjok;ghapihty38uy5hg9sjhb9e8hbj89wg'

@app.route('/', methods=["POST", "GET"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        print('gg')
        return redirect('lol')
    return render_template('login.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)