from main.models import ClienteModel



class ClienteFiltros():


    def __init__(self, clientes):
        self.__clientes = clientes
        self.__dict_filters = {"id": self.__filtro_por_id,
                       "nombre": self.__filtro_por_nombre,
                       "apellido": self.__filtro_por_apellido,
                       "email": self.__filtro_por_email
                       }



    def __filtro_por_id(self, value):
        return self.__clientes.filter(ClienteModel.id == int(value))


    def __filtro_por_nombre(self, value):
        return self.__clientes.filter(ClienteModel.nombre.like('%' + value + '%'))



    def __filtro_por_apellido(self, value):
        return self.__clientes.filter(ClienteModel.apellido.like('%' + value + '%'))


    def __filtro_por_email(self, value):
        return self.__clientes.filter(ClienteModel.email.like('%' + value + '%'))



    def aplicar_filtro(self, key, value):
        return self.__dict_filters[key](value)



