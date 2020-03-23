from flask import Flask, request, render_template

app = Flask(__name__) 

@app.route('/index')
def index():
    return render_template("index.html")

@app.route('/termos-de-uso')
def termo():
    return render_template("termos_de_uso.html")

@app.route('/form-1')
def form_1():
    return render_template("questionario_1.html")

@app.route('/form-2')
def form_2():
    return render_template("questionario_2.html")

@app.route('/form-3')
def form_3():
    return render_template("questionario_3.html")

@app.route('/form-4')
def form4():
    return render_template("questionario_4.html")

@app.route('/resultado-final')
def resultado():
    return render_template("resultado.html")

if __name__ == '__main__':
    app.run(debug=True) 