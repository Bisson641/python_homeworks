from flask import Blueprint, render_template

index_app = Blueprint("index_app", __name__, url_prefix="/")


@index_app.get("/", endpoint="index")
def index_page():
    return render_template("Index.html")
    return "Welcome to \"Index\" page"



