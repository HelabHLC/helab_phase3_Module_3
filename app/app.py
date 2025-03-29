from flask import Flask, render_template, request
from colormath.color_objects import LabColor, sRGBColor
from colormath.color_conversions import convert_color

app = Flask(__name__)

def is_in_srgb_gamut(l, a, b):
    lab = LabColor(l, a, b)
    rgb = convert_color(lab, sRGBColor)

    if (0.0 <= rgb.rgb_r <= 1.0 and
        0.0 <= rgb.rgb_g <= 1.0 and
        0.0 <= rgb.rgb_b <= 1.0):
        r = int(rgb.rgb_r * 255)
        g = int(rgb.rgb_g * 255)
        b = int(rgb.rgb_b * 255)
        hex_color = f"{r:02X}{g:02X}{b:02X}"
        return True, hex_color, r, g, b
    else:
        return False, None, None, None, None

@app.route("/tools/gamut", methods=["GET", "POST"])
def gamut():
    if request.method == "POST":
        h = request.form["h"]
        l = request.form["l"]
        c = request.form["c"]

        # Dummy-Konvertierung HLC → Lab
        if __name__ == "__main__":
    app.run(debug=True)

        # Hier ersetzt du später mit echten HLC→Lab-Werten
        lab_l = float(l)
        lab_a = float(c)
        lab_b = 0.0

        hlc_string = f"H{h}_L{l}_C{c}"

        in_gamut, hex_color, r, g, b = is_in_srgb_gamut(lab_l, lab_a, lab_b)

        return render_template(
            "gamut.html",
            h=h, l=l, c=c,
            lab_l=lab_l, lab_a=lab_a, lab_b=lab_b,
            rgb_r=r, rgb_g=g, rgb_b=b,
            hex=hex_color,
            hlc_string=hlc_string,
            in_gamut=in_gamut
        )

    return render_template("gamut.html")

