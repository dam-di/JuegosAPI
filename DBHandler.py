from pymongo import MongoClient

from ResponseModel import ResponseModel


class DBHandler(object):
    def __init__(self):
        self.db = self.conectar()
        self.collection = self.db.get_collection('juegos')


    def conectar(self):
        client = MongoClient(
            #host = 'infsalinas.sytes.net:10450',
            host = '192.168.1.100:10450',
            serverSelectionTimeoutMS = 3000,
            username = 'profe2',
            password = 'abcd1234',
            authSource = 'profe2'
        )
        db = client.get_database('profe2')
        return db


    #######################################
    #ESTUDIANTES
    def eliminarEstudiante(self,_idE):
        response = ResponseModel()

        try:
            self.collection = self.db.get_collection('estudiantes')
            self.collection.delete_one({'_id':_idE})
            response.resultOk = True
            response.data = 'Estudiante eliminado con exito'
        except Exception as e:
            print(e)

        return response

    def obtenerEstudiante(self,_idE):
        response = ResponseModel()
        try:
            self.collection = self.db.get_collection('estudiantes')
            estudiante = self.collection.find_one({'_id':_idE})
            response.resultOk = True
            response.data = str(estudiante)
        except Exception as e:
            print(e)

        return response


    def actualizar(self, estudiante):
        response = ResponseModel()
        print(estudiante['Nombre'])

        try:
            self.collection = self.db.get_collection('estudiantes')
            self.collection.update_one({'_id':estudiante['_id']},{'$set':estudiante})
            response.resultOk = True
            response.data = 'Estudiante actualizado con exito'
        except Exception as e:
            print(e)

        return response

    # obtenerLista (en los videos)
    def obtenerJuegos(self):
        response = ResponseModel()
        try:
            self.collection = self.db.get_collection('juegos')
            listaJuegos = []
            coleccion = self.collection.find({})
            for juego in coleccion:
                listaJuegos.append(juego)

            response.resultOk = True
            response.data = str(listaJuegos)

        except Exception as e:
            print(e)

        return response

    def insertarJuego(self, juego):
        response = ResponseModel()
        try:
            self.collection = self.db.get_collection('juegos')
            self.collection.insert_one(juego)
            response.resultOk = True
            response.data = 'Juego insertado con exito'
        except Exception as e:
            print(e)

        return response