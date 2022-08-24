from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/<x>')
@app.route('/<x>/<y>')
@app.route('/<x>/<y>/<color1>')
@app.route('/<x>/<y>/<color1>/<color2>')
def render_checkerboard(x=8, y=8, color1='darkcyan', color2='gainsboro'):
    return render_template('index.html', cols=int(x), rows=int(y), clr1 = color1, clr2 = color2)

if __name__ == '__main__':
    app.run(debug=True)