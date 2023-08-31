from flask import Flask, render_template, jsonify,request
import numpy as np
from joblib import load
import os 

#cargar modelo
dt=load('dt1.joblib')

#Generar el servidor (Back-End)

servidorWeb = Flask(__name__)

@servidorWeb.route("/holamundo",methods=['GET'])

def holamundo():
        return render_template("pagina1.html")

#envio de datos a traves de JSON

@servidorWeb.route("/modelo",methods=['POST'])
def modeloPrediccon():
        contenido=request.json
        print(contenido)
        return jsonify({'resultado':"Hola"})


if __name__ == "__main__":
        servidorWeb.run(debug=False,host="0.0.0.0",port="8080")

