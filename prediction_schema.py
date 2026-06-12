from flask import Blueprint, render_template

hydro_bp = Blueprint("hydro", __name__)

@hydro_bp.route("/hydrodynamic-view")
def hydrodynamic_view():
    return render_template("hydrodynamic_view.html")