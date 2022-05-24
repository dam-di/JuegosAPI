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


    def obtenerProveedores(self):
        response = ResponseModel()
        try:
            self.collection = self.db.get_collection('proveedores')
            listaProveedores = []
            coleccion = self.collection.find({})
            for juego in coleccion:
                listaProveedores.append(juego)

            response.resultOk = True
            response.data = str(listaProveedores)

        except Exception as e:
            print(e)

        return response



    #######################################
    #JUEGOS
    def eliminarJuego(self,_idE):
        response = ResponseModel()

        try:
            self.collection = self.db.get_collection('juegos')
            self.collection.delete_one({'_id':_idE})
            response.resultOk = True
            response.data = 'Juego eliminado con exito'
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


    def actualizarJuego(self, juego):
        response = ResponseModel()
        print(juego['_id'])

        try:
            self.collection = self.db.get_collection('juegos')
            self.collection.update_one({'_id':juego['_id']},{'$set':juego})
            response.resultOk = True
            response.data = 'Juego actualizado con exito'
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