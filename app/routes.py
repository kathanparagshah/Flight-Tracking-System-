from flask import Blueprint, render_template, request, redirect, url_for, flash

main = Blueprint("main", __name__)

@main.route("/")
def home():
    return render_template("index.html")

@main.route("/track", methods=["POST"])
def track():
    flight_number = request.form.get("flight_number")
    return f"Tracking flight: {flight_number}"
