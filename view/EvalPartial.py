from model.EvalAnteproy import EvaluacionAnteproyecto
from model.Calificacion import Calificacion
from datetime import datetime

""" Este archivo contine las funcionalidades de la vista relacionado con la evaluacion de los anteproyectos"""


def agregar_evaluacion(st, controller, criterios_controller):
    nota_maxima = 5.0
    nota_minima = 0.0
    mes = int(datetime.today().strftime('%m'))

    comprovador_calificacion = True
    st.title( "Calificar Trabajos" )
    evaluacion_obj = EvaluacionAnteproyecto()
    evaluacion_obj.id_estudiante = st.text_input("Id estudiante")
    if mes < 7:
        evaluacion_obj.periodo = datetime.today().strftime('%Y') + '-' + '1: '
    else:
        evaluacion_obj.periodo = datetime.today().strftime('%Y') + '-' + '2: '
    evaluacion_obj.periodo = st.text_input( "Periodo de evaluacion", value = evaluacion_obj.periodo )
    evaluacion_obj.nombre_autor = st.text_input("Nombre del autor")
    evaluacion_obj.tipo_trabajo = st.radio("Tipo de trabajo", ('Aplicado', 'Investigacion') )
    evaluacion_obj.nombre_trabajo = st.text_input("Nombre del trabajo")
    evaluacion_obj.nombre_director = st.text_input("Nombre del director")
    st.write("El trabajo tiene codirector?")
    coodirector = st.radio( "El trabajo tiene codirector?", ('Si', 'No') )
    if coodirector == 'Si':
        evaluacion_obj.nombre_codirector = st.text_input("Nombre del codirector")
    evaluacion_obj.nombre_jurado1 = st.text_input("Nombre del jurado1" )
    evaluacion_obj.nombre_jurado2 = st.text_input("Nombre del jurado2" )
    lista_calificaciones = []
    criterios = []
    for i in range( len(  criterios_controller.criterios ) ):
        criterios.append(  criterios_controller.criterios[i].identificador )
        lista_calificaciones.append(Calificacion())
        lista_calificaciones[i].numero_jurados = 2
        lista_calificaciones[i].id_criterio = criterios_controller.criterios[i].identificador
        lista_calificaciones[i].ponderacion = criterios_controller.criterios[i].porcentaje_ponderacion
    for j in range( len( lista_calificaciones )  ):
        st.subheader( "Criterio "+ lista_calificaciones[j].id_criterio )
        lista_calificaciones[ j ].nota_jurado1 = st.number_input( "Nota jurado 1:", key = (j + 1) * 10, min_value = nota_minima, max_value = nota_maxima  )
        lista_calificaciones[j].nota_jurado2 = st.number_input( "Nota jurado 2:", key = j, min_value = nota_minima, max_value = nota_maxima )
        lista_calificaciones[j].nota_final = round((lista_calificaciones[ j ].nota_jurado1 + lista_calificaciones[ j ].nota_jurado2) / lista_calificaciones[ j ].numero_jurados, 2)
        lista_calificaciones[j].comentario = st.text_input("Comentario:", key = (j + 1) * 20 )
        evaluacion_obj.nota = (lista_calificaciones[j].nota_final * lista_calificaciones[j].ponderacion) + evaluacion_obj.nota
    evaluacion_obj.comentario_final = st.text_input( "Comentario Final:" )

    enviado_btn = st.button("Send")

    if enviado_btn:
        evaluacion_obj.calificacion = lista_calificaciones
        evaluacion_obj.nota =round( evaluacion_obj.nota, 1 )
        controller.agregar_evaluacion(evaluacion_obj)
        st.success("Evaluacion agregada exitosamente")
    else:
        st.error( "Faltan criterios por calificar!" )



    # Retorna el controlador pq solo las colecciones se pasan en python por referencia,
    # entonces de esta manera se actualiza el controlador en la vista principal
    return controller


def listar_evaluacion(st, controller, criterios_controller ):
    """Itera los elementos de evaluacion agregados y los muestra"""
    st.title("Ver y editar calificaciones")
    ver_editar = st.radio("Que quieres hacer?", ('Ver', 'Editar') )
    estudiantes_nombres = []
    criterios = []
    for estudiantes in controller.evaluaciones:
        estudiantes_nombres.append( estudiantes.nombre_autor )
    for criterio in criterios_controller.criterios:
        criterios.append(criterio.identificador)
    seleccionar_estudiantes = st.selectbox( "seleccioanr estudiante", estudiantes_nombres )
    evaluacion: object
    for evaluacion in controller.evaluaciones:
        if seleccionar_estudiantes == evaluacion.nombre_autor:
            if ver_editar == 'Ver':
                st.subheader( "Id autor: " + evaluacion.id_estudiante )
                st.subheader( "Periodo evaluacion: " + evaluacion.periodo )
                st.subheader("Nombre autor: " + evaluacion.nombre_autor)
                st.subheader("Tipo de trabajo: " + evaluacion.tipo_trabajo)
                st.subheader("Titulo del trabajo: " + evaluacion.nombre_trabajo)
                st.subheader("Nombre director: " + evaluacion.nombre_director)
                st.subheader("Nombre director: " + evaluacion.nombre_codirector)
                st.subheader("Jurado1 : " + evaluacion.nombre_jurado1)
                st.subheader("Jurado2 : " + evaluacion.nombre_jurado2)
                seleccionar_criterio = st.selectbox("Escoger criterio", criterios)
                for i in evaluacion.calificacion:
                    if seleccionar_criterio == i.id_criterio:
                        st.subheader( "Nota jurado 1: " + str(i.nota_jurado1) )
                        st.subheader("Nota jurado 2: " + str(i.nota_jurado2) )
                        st.subheader( "Nota del criterio: " + str(i.nota_final) )
                        st.subheader("Comentario: ")
                        st.write( "" + i.comentario )
                st.subheader("Nota final : " + str(evaluacion.nota) )
                st.subheader("Comentario final : " + evaluacion.comentario_final)
            else:
                evaluacion.id_estudiante = st.text_input("Id estudiante", value = evaluacion.id_estudiante  )
                evaluacion.periodo = st.text_input("Periodo de evaluacion", value = evaluacion.periodo )
                evaluacion.nombre_autor = st.text_input("Nombre del autor", value = evaluacion.nombre_autor)
                if evaluacion.tipo_trabajo == 'Aplicado':
                    evaluacion.tipo_trabajo = st.radio("Tipo de trabajo", ('Aplicado', 'Investigacion') )
                else:
                    evaluacion.tipo_trabajo = st.radio("Tipo de trabajo", ('Aplicado', 'Investigacion') , index = 1 )
                evaluacion.nombre_trabajo = st.text_input("Nombre del trabajo", value = evaluacion.nombre_trabajo )
                evaluacion.nombre_director = st.text_input("Nombre del director", value = evaluacion.nombre_director )
                st.write("codirector?")
                if evaluacion.nombre_codirector == "No aplica":
                    coodirector = st.radio("El trabajo tiene codirector?", ('Si', 'No'), index = 1 )
                else:
                    coodirector = st.radio("El trabajo tiene codirector?", ('Si', 'No'))
                if coodirector == 'Si':
                    evaluacion.nombre_codirector = st.text_input("Nombre del codirector", value = evaluacion.nombre_codirector )
                evaluacion.nombre_jurado1 = st.text_input("Nombre del jurado1", value = evaluacion.nombre_jurado1 )
                evaluacion.nombre_jurado2 = st.text_input("Nombre del jurado2", value = evaluacion.nombre_jurado2 )
                seleccionar_criterio = st.selectbox("Escoger criterio", criterios)
                for i in evaluacion.calificacion:
                    if seleccionar_criterio == i.id_criterio:
                        evaluacion.nota -= (( ( i.nota_jurado1 + i.nota_jurado2 ) / 2 ) * i.ponderacion)
                        i.nota_jurado1 = st.number_input("Nota jurado 1: ", value = i.nota_jurado1)
                        i.nota_jurado2 = st.number_input("Nota jurado 2: ", value = i.nota_jurado2)
                        i.comentario = st.text_input("Comentario ", value = i.comentario)
                        i.nota_final = ( i.nota_jurado1 + i.nota_jurado2 )
                        evaluacion.nota += ((i.nota_final) * i.ponderacion)
                evaluacion.comentario_final = st.text_input( "Comentario final", value = evaluacion.comentario_final )
                enviar_btn = st.button( "Editar" )
                if enviar_btn:
                    st.success( "Cambio realizado" )