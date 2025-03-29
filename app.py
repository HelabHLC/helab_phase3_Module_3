
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/tools/farbnamen')
def farbnamen():
    return "<h2>Modul 1 – Farbnamen → LAB (kommt bald)</h2>"

@app.route('/tools/lab-to-hlc')
def lab_to_hlc():
    return "<h2>Modul 2 – LAB → HLC (kommt bald)</h2>"

@app.route('/tools/gamut')
def gamut_tool():
    return "<h2>Modul 3 – Gamut Check</h2>"

@app.route('/tools/icc-grid')
def icc_grid():
    return "<h2>Modul 4 – ICC-Grid (coming soon)</h2>"

@app.route('/tools/util')
def tools():
    return "<h2>Tools (Delta-E, Export etc.)</h2>"

if __name__ == '__main__':
    app.run(debug=True)
