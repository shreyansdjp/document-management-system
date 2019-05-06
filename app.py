from flask import Flask, render_template, url_for, redirect, request, jsonify, session
from forms import LoginForm, RegistrationForm
from helpers import logged_in
from flask_cors import cross_origin

app = Flask(__name__)
app.config["SECRET_KEY"] = "asdjok;ghapihty38uy5hg9sjhb9e8hbj89wg"

@app.route("/", methods=["POST", "GET"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        print(form.email.data)
        return redirect(url_for("dashboard"))
    return render_template("login.html", form=form)


@app.route("/signup", methods=["POST", "GET"])
def signup():
    form = RegistrationForm()
    if form.validate_on_submit():
        print(form.first_name.data)
        return redirect(url_for("dashboard"))
    return render_template("signup.html", form=form)


@app.route("/dashboard")
@logged_in
def dashboard():
    return render_template("dashboard.html", title="Dashboard")


@app.route('/new/document')
def new_document():
    return redirect(url_for('doc', id=2))


@app.route("/doc/<id>")
def doc(id):
    return render_template("doc.html", title="")


@app.route("/profile")
def profile():
    return render_template("profile.html", title="Profile")
    

@app.route("/document/<id>", methods=["POST", "GET"])
@cross_origin(supports_credentials=True)
def document(id):
    if request.method == "GET":
        print(id)
    elif request.method == "POST":
        print(request.get_json())


if __name__ == "__main__":
    app.run(debug=True)