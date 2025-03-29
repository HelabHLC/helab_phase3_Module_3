from flask import Flask, render_template, request
import json
import os

app = Flask(__name__)

# Pfad zur JSON-Datei mit allen HLC → LAB Werten
with open(os.path.join("data", "hlc_lab_full_reference.json"), "r", encoding="utf-8") as f:
    hlc_data = json.load(f)

# Näherungsweise ICC-Gamut-Grenzen
lab_thresholds = {
    "TextileRGB_FOGRA58.icc": {"a_min": -60, "a_max": 60, "b_min": -40, "b_max": 60},
    "PSOcoated_v3.icc": {"a_min": -50, "a_max": 70, "b_min": -60, "b_max": 50},
    "ISOcoated_v2_300_eci.icc": {"a_min": -55, "a_max": 65, "b_min": -50, "b_max": 55},
    "PSO_Uncoated_ISO12647_eci.icc": {"a_min": -40, "a_max": 50, "b_min": -35, "b_max": 45},
    "PSOuncoated_v3_FOGRA52.icc": {"a_min": -38, "a_max": 42, "b_min": -30, "b_max": 40},
    "ISOcoated_v2_eci.icc": {"a_min": -55, "a_max": 65, "b_min": -50, "b_max": 55},
}

def check_lab_in_gamut(lab, limits):
    _, a, b = lab
    return limits["a_min"] <= a <= limits["a_max"] and limits["b_min"] <= b <= limits["b_max"]

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/tools/gamut", methods=["GET", "POST"])
def gamut_tool():
    result = None
    status = ""
    selected_profile = "TextileRGB_FOGRA58.icc"

    if request.method == "POST":
        h = request.form.get("h")
        l = request.form.get("l")
        c = request.form.get("c")
        selected_profile = request.form.get("icc_profile")

        hlc_key = f"H{h.zfill(3)}_L{l.zfill(3)}_C{c.zfill(3)}"
        lab = hlc_data.get(hlc_key)

        if lab:
            limits = lab_thresholds.get(selected_profile)
            if limits:
                in_gamut = check_lab_in_gamut(lab, limits)
                status = "✅ Innerhalb des Gamut" if in_gamut else "❌ Außerhalb des Gamut"
                result = {"hlc": hlc_key, "lab": lab, "status": status}
            else:
                status = "⚠️ Profilgrenzen nicht definiert."
        else:
            status = "❌ HLC-Farbwert nicht gefunden."

    return render_template("gamut.html", result=result, status=status, profiles=lab_thresholds.keys(), selected_profile=selected_profile)

if __name__ == "__main__":
    app.run(debug=True)
