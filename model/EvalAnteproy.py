import json


class EvaluacionAnteproyecto:

    def __init__(self) -> None:
        super().__init__()
        self.calificacion = []

        # Datos de toda evaluacion
        self.id_estudiante = ""
        self.periodo = ''
        self.nombre_autor = ""
        self.nombre_trabajo = ""
        self.tipo_trabajo = ""
        self.nombre_director = ""
        self.nombre_codirector = "No aplica"
        self.nombre_jurado1 = " "
        self.nombre_jurado2 = " "
        self.nota = 0.0
        self.comentario_final = ""

        # Llamado al método que inicializa la información precargada

    def __str__(self) -> str:
        return json.dumps(self.__dict__)

        # TODO completar con el resto de criterios
