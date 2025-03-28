
from flask import Blueprint, request, render_template
from .hlclab import get_lab_from_hlc

gamut_bp = Blueprint('gamut_bp', __name__)

def is_within_gamut(lab):
    # Placeholder – Logik definieren
    return all(-128 <= v <= 127 for v in [lab['a'], lab['b']])

@gamut_bp.route("/tools/gamut", methods=["GET", "POST"])
def gamut_check():
    result = None
    if request.method == "POST":
        h = request.form.get("hue")
        l = request.form.get("lightness")
        c = request.form.get("chroma")
        hlc_code = f"H{int(h):03d}_L{int(l):03d}_C{int(c):03d}"

        lab = get_lab_from_hlc(hlc_code)
        if lab:
            result = {
                "hlc": hlc_code,
                "lab": lab,
                "in_gamut": is_within_gamut(lab)
            }
        else:
            result = {"hlc": hlc_code, "lab": "Nicht gefunden", "in_gamut": False}

    return render_template("gamut_check.html", result=result)
