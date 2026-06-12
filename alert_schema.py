from flask import Blueprint, send_file
import os

gis_bp = Blueprint("gis", __name__, url_prefix="/api/gis")

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../gis"))


@gis_bp.route("/rivers.geojson")
def rivers():
    return send_file(os.path.join(BASE_DIR, "rivers.geojson"))


@gis_bp.route("/districts.geojson")
def districts():
    return send_file(os.path.join(BASE_DIR, "districts.geojson"))


@gis_bp.route("/basins.geojson")
def basins():
    return send_file(os.path.join(BASE_DIR, "basins.geojson"))