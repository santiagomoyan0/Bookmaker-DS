from flask_restful import Resource
from flask import request, jsonify
from .. import db
from main.models import ClienteModel
from main.map import ClienteFiltros


from main.map import ClienteSchema


cliente_schema = ClienteSchema()

class Clientes(Resource):
    def get(self):
        filtros = request.data
        clients = db.session.query(ClienteModel)
        client_filter = ClienteFiltros(clients)
        for key, value in request.get_json().items():
            consulta = client_filter.aplicar_filtro(key, value)
        return cliente_schema.dump(consulta.all(), many = True)

    def post(self):
        client = cliente_schema.load(request.get_json())
        db.session.add(client)
        db.session.commit()
        return cliente_schema.dump(client), 201




class Cliente(Resource):
    def get(self,id):
       client = db.session.query(ClienteModel).get_or_404(id)
       return cliente_schema.dump(client.all(), many = True)



    def put(self, id):
        client = db.session.query(ClienteModel).get_or_404(id)
        datos = request.get_json().items()
        for clave, valor in datos:
            setattr(client, clave, valor)
        db.session.add(client)
        db.session.commit()
        return cliente_schema.dump(client)


    def delete(self, id):
        cliente = db.session.query(ClienteModel).get_or_404(id)
        db.session.delete(cliente)
        db.session.commit()
        return '', 204