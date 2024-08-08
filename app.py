from flask import Flask, redirect, flash, url_for, redirect, render_template, request
from config import User
from werkzeug.security import generate_password_hash
from flask_login import LoginManager


app = Flask(__name__)
app.secret_key = "secret"

login_manager = LoginManager()


@login_manager.user_loader
def load_user(user_id):
    return User.get_by_id(user_id)

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        if not request.form["name"] or not request.form["password"] or not request.form["email"]:
            flash("未入力の項目があります")
            return redirect(request.url)
        
        if User.select().where(User.name == request.form["name"]):
            flash("その名前は既に使われています")
            return redirect(request.url)
        if User.select().where(User.email == request.form["email"]):
            flash("そのメールアドレスは既に使われています")
            return redirect(request.url)
        
        User.create(
            name=request.form["name"],
            email=request.form["email"],
            password=generate_password_hash(request.form["password"])
        )
        return render_template("index.html")
    return render_template("register.html")


@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")


@app.route("/login")
def login():
    if request.method == "POST":
        # データの検証
        if not request.form["password"] or not request.form["email"]:
            flash("未入力の項目があります。")
            return redirect(request.url)

        # ここでユーザーを認証し、OKならログインする

        # NGならフラッシュメッセージを設定
        flash("認証に失敗しました")
    return render_template("login.html")


if __name__ == "__main__":
    # DEBUG is SET to TRUE. CHANGE FOR PROD
    app.run(port=8000, debug=True)
