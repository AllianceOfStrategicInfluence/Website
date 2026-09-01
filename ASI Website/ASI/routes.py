from flask import Blueprint, current_app, send_from_directory, render_template, request

main = Blueprint("main", __name__, url_prefix="/")

@main.route("/")
def home():
    return render_template(
        "home.jinja",
    )

@main.route("/about")
def about():
    return render_template(
        "about.jinja",
        goFundMeLink="https://gofund.me/e5486df03",
        #history of ASI and depts and mission and socials
    )

@main.route("/leadership")
def leadership():
    return render_template(
        "about.jinja",
        # leadership and dept leaders
    )