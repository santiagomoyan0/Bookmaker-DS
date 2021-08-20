from main import db

class Cliente(db.Model):

    __id = db.Column(db.Integer, primary_key=True)
    __apellido = db.Column(db.String(50), nullable=False)
    __nombre = db.Column(db.String(50), nullable=False)
    __mail = db.Column(db.String(120), nullable=False)


    def __init__(self):
        pass

    def __repr__(self):
        return f'<Cliente: {self.__id} {self.__mail} >'

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id):
        self.__id = id

    @id.deleter
    def id(self):
        del self.__id

    @property
    def apellido(self):
        return self.__apellido

    @apellido.setter
    def apellido(self, apellido):
        self.__apellido = apellido

    @apellido.deleter
    def apellido(self):
        del self.__apellido

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre

    @nombre.deleter
    def nombre(self):
        del self.__nombre

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email):
        self.__email = email

    @email.deleter
    def email(self):
        del self.__email
