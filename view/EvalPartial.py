from model.EvalAnteproy import EvaluacionAnteproyecto

""" Este archivo contine las funcionalidades de la vista relacionado con la evaluacion de los anteproyectos"""


def agregar_evaluacion(st, controller):
    # Objecto que modelará el formulario
    evaluacion_obj = EvaluacionAnteproyecto()
    evaluacion_obj.nombre = st.text_input("Nombre estudiante")
    evaluacion_obj.id_estudiante = st.text_input("Id estudiante")
    # TODO
    # Agregar campo para leer el tema y la versión de la evaluación del proyecto
    enviado_btn = st.button("Submit")

    # Cuando se oprime el boton se agrega a la lista
    if enviado_btn:
        controller.agregar_evaluacion(evaluacion_obj)
        st.write("Evaluacion agregada exitosamente")
    # Retorna el controlador pq solo las colecciones se pasan en python por referencia,
    # entonces de esta manera se actualiza el controlador en la vista principal
    return controller


def listar_evaluacion(st, controller):
    """Itera los elementos de evaluacion agregados y los muestra"""
    st.title("Datos guardados... a mejorar la presentacion")
    for evaluacion in controller.evaluaciones:
        st.write(evaluacion.id_estudiante)
        st.write(evaluacion.nombre)
        st.write(evaluacion.tema_proyecto)
        st.write(evaluacion.version_doc)
