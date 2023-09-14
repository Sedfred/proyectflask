from flask import Flask, render_template,jsonify,request
import numpy as np
from joblib import load
import os

#Cargar el modelo
dt=load('lin_reg.joblib')

#Servidor (backend)
servidorWeb = Flask(__name__)

@servidorWeb.route("/holamundo",methods=['GET'])
def formulario():
    return render_template('pagina_prinpal.html')

@servidorWeb.route('/pagina1', methods=['GET'])
def pagina1():
    return render_template('pagina1.html')

#Envio de datos a través de JSON
@servidorWeb.route('/modelo',methods=['POST'])
def modeloPrediccion():
    #Procesar los datos de entrada
    contenido = request.json
    print(contenido)
    datosEntrada = np.array([
        contenido["OverallQual"],contenido["GarageCars"],contenido["ExterQual"],contenido["BsmtQual"],
        contenido["KitchenQual"],contenido["GrLivArea"],contenido["TotalBsmtSF"],
        contenido["Fireplaces"],contenido["Age"]
    ])
    resultado= dt.predict(datosEntrada.reshape(1,-1))

    return jsonify({'resultado':str(resultado[0])})
    #return render_template('pagina_prinpal.html',resul=resultado)


@servidorWeb.route('/modeloForm',methods=['POST'])
def modeloForm():
    #Procesar los datos de entrada
    contenido = request.form 
    print(contenido)
    datosEntrada = np.array([
        contenido["OverallQual"],contenido["GarageCars"],contenido["ExterQual"],contenido["BsmtQual"],
        contenido["KitchenQual"],contenido["GrLivArea"],contenido["TotalBsmtSF"],
        contenido["Fireplaces"],contenido["Age"]
    ])
    resultado= dt.predict(datosEntrada.reshape(1,-1))

    #return jsonify({'resultado':str(resultado[0])})
    return render_template('resultado.html',resul=round(resultado[0],2))


if __name__ == '__main__':
    servidorWeb.run(debug=False,host='0.0.0.0',port='8080')

