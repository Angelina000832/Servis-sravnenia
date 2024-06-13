from flask import Flask, request, render_template



app = Flask(__name__)

@app.route("/index")
@app.route("/")
def index():
    return render_template('index.html')

@app.route("/fridge")
def fridge ():
    return render_template('fridge.html')

@app.route("/SVCH")
def SVCH ():
    return render_template('SVCH.html')

@app.route("/tele")
def tele ():
    return render_template('tele.html')

@app.route("/coffee")
def coffee ():
    return render_template('coffee.html')

@app.route("/washP")
def washP ():
    return render_template('washP.html')

@app.route("/washM")
def washM ():
    return render_template('washM.html')

@app.route("/sidebar")
def sidebar ():
    return render_template('sidebar.html')



if __name__ == '__main__':
    app.run(debug=True)
