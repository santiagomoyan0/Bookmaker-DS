from flask_restful import Resource
from flask import request, jsonify
from .. import db
from main.models import EmpresaModel
from main.map import EmpresaSchema
from main.services import EmpresaService

empresa_schema = EmpresaSchema()
empresa_service = EmpresaService()

class Empresa(Resource):
    def get(self, id):
        empresa = db.session.query(EmpresaModel).get_or_404(id)
        return empresa_schema.dump(empresa), 201

    def delete(self, id):
        empresa = db.session.query(EmpresaModel).get_or_404(id)
        db.session.delete(empresa)
        db.session.commit()
        return '', 204

    def put(self, id):
        empresa = db.session.query(EmpresaModel).get_or_404(id)
        data = request.get_json().items()
        for key, value in data:
            setattr(empresa, key, value)
        db.session.add(empresa)
        db.session.commit()
        return empresa_schema.dump(empresa), 201


class Empresas(Resource):
    def get(self):
        empresas = db.session.query(EmpresaModel).all()
        return empresa_schema.dump(empresas, many=True)

    def post(self):
        empresa = empresa_schema.load(request.get_json())
        db.session.add(empresa)
        db.session.commit()
        return empresa_schema.dump(empresa), 201
