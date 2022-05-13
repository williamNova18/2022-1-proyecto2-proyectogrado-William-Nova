import json


class Criterio:

    def __int__(self) -> None:
        self.identificador = ""
        self.descripcion = ""
        self.porcentaje_ponderacion = None

    def __init__(self, identificador, descripcion, porcentaje_ponderacion):
        self.identificador = identificador
        self.descripcion = descripcion
        self.porcentaje_ponderacion = porcentaje_ponderacion

    def __str__(self) -> str:
        return json.dump(self.__dict__)
