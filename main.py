import json
from datetime import datetime
from hashlib import sha256

from flask import Flask, request

from DBHandler import DBHandler
from ResponseModel import ResponseModel

app = Flask(__name__)

PASS = "abcd1234"

def checkTokenAuth(tokenSHA256Request, USER, route):

    passSHA256 = sha256(PASS.encode('utf-8')).hexdigest()
    minutes = datetime.now().minute

    tokenString = USER + route + passSHA256 + str(minutes)
    tokenSHA256 = sha256(tokenString.encode('utf-8')).hexdigest()

    print(tokenSHA256Request)
    print(tokenSHA256)

    if tokenSHA256 == tokenSHA256Request:
        print('acceso correcto')
        return True
    else:
        print('acceso denegado')
        return False




@app.route('/juegos', methods=['POST','PUT','DELETE','GET'])
def juegos():
    print(request.json)
    response = ResponseModel()
    tokenSHA256Request = request.authorization['password']
    user = request.authorization['username']
    route = request.json['route']

    if checkTokenAuth(tokenSHA256Request, user, route):
        try:
            if request.method == 'POST':
                response = insertarJuego(request.json['data'])
            elif request.method == 'GET':
                response = obtenerJuegos(request.json['data'])
            elif request.method == 'PUT':
                #response = updateStudent(request.json['data'])
                pass
            elif request.method == 'DELETE':
                pass
                #response = deleteStudent(request.json['data'])


        except Exception as e:
            print(e)
    else:
        response.data = 'NO TIENES ACCESO'

    return json.dumps(response.__dict__)


def deleteStudent(_idE):
    response = DBHandler().eliminarEstudiante(_idE)
    return response


def updateStudent(estudiante):
    response = DBHandler().actualizar(estudiante)
    return response

def obtenerJuegos(_idJ):
    if _idJ == 'all':
        response = DBHandler().obtenerJuegos()
    else:
        response = DBHandler().obtenerEstudiante(_idJ)

    return response

def insertarJuego(juego):
    response = DBHandler().insertarJuego(juego)
    return response





if __name__ == '__main__':
    app.run(debug=True, port=5000, host='localhost')