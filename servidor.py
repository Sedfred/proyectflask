from flask import Flask, render_template,jsonify,request
import numpy as np
from joblib import load
import os

#Cargar el modelo
dt=load('dt1.joblib')

#Servidor (backend)
servidorWeb = Flask(__name__)

@servidorWeb.route("/holamundo",methods=['GET'])
def formulario():
    return render_template('pagina1.html')

#Envio de datos a través de JSON
@servidorWeb.route('/modelo',methods=['POST'])
def modeloPrediccion():
    #Procesar los datos de entrada
    contenido = request.json
    print(contenido)
    datosEntrada = np.array([
        .88, 0, 2.6, 0.098, 25, 67, .9968,
        contenido["pH"],contenido["alcohol"],contenido["sulphates"],
    ])
    resultado= dt.predict(datosEntrada.reshape(1,-1))

    return jsonify({'resultado':str(resultado[0])})


if __name__ == '__main__':
    servidorWeb.run(debug=False,host='0.0.0.0',port='8080')

