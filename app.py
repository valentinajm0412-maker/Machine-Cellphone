from flask import Flask, render_template, request
import LinearRegressionCelular

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/LRegressionCelular/', methods=['GET', 'POST'])
def LRegressionCelular():
    calcularValorResult = None
    if request.method == 'POST':
        anios = float(request.form['anios'])
        calcularValorResult = LinearRegressionCelular.calcularValor(anios)
    return render_template('tempLinearRegressionCelular.html', result=calcularValorResult)

if __name__ == '__main__':
    app.run(debug=True)