from flask import Blueprint, jsonify, render_template

blueprint = Blueprint("home", __name__)


@blueprint.get(
    rule="/",
    endpoint="index",
)
def index():
    return render_template("home/index.html")


@blueprint.route(
    rule="/about",
    endpoint="about",
    methods=["GET", "POST"],
)
def ping():
    value = {
        "message": "Pong!",
    }
    return jsonify(value)
