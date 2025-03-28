from flask import render_template, request
from app.gamut_tools import hlc_to_lab, is_in_gamut

def init_routes(app):
    @app.route("/")
    def index():
        return render_template("index.html")

    @app.route("/tools/gamut", methods=["GET", "POST"])
    def gamut():
        result = None
        if request.method == "POST":
            h = float(request.form["h"])
            l = float(request.form["l"])
            c = float(request.form["c"])
            lab = hlc_to_lab(h, l, c)
            in_gamut = is_in_gamut(lab)
            result = {"lab": lab, "in_gamut": in_gamut}
        return render_template("gamut.html", result=result)