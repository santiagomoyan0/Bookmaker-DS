from .. import db
from sqlalchemy.ext.hybrid import hybrid_property

class Cuota(db.Model):
    __tablename__ = "cuota"
    __id = db.Column('id', db.Integer, primary_key= True )
    __probabilidad_local = db.Column('probalididad_local', db.Float)
    __probabilidad_empate = db.Column('probabilidad_empate', db.Float)
    __probabilidad_visitante = db.Column('probabilidad_visitante', db.Float)
    __partido_id = db.Column("partidos_id", db.Integer, db.ForeignKey('partidos.id'))
    partido = db.relationship("Partido", back_populates="cuota")


    def __repr__(self):
        return f'< Cuota:  {self.__id} {self.__probabilidad_local}, {self.__probabilidad_empate}, {self.__probabilidad__visitante}>'



    @hybrid_property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id):
        self.__id = id

    @id.deleter
    def id(self):
        del self.__id

    @hybrid_property
    def probabilidad_local(self):
        return self.__probabilidad_local


    @probabilidad_local.setter
    def probabilidad_local(self, probabilidad_local):
        self.__probabilidad_local = probabilidad_local

    @hybrid_property
    def probabilidad_empate(self):
        return self.__probabilidad_empate



    @probabilidad_empate.setter
    def probabilidad_empate(self, probabilidad_empate):
        self.__probabilidad_empate = probabilidad_empate


    @hybrid_property
    def probabilidad_visitante(self):
        return self.__probabilidad_visitante



    @probabilidad_visitante.setter
    def probabilidad_visitante(self, probabilidad_visitante):
        self.__probabilidad_visitante = probabilidad_visitante