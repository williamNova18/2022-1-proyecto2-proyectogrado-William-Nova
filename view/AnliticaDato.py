from model.EvalEstudiante import EvaluacionEstudiante



def analisis(st, controller):
    opcion = st.radio( "Que analisis quieres hacer?", ('Encontrar Calificacion más alta', "otro") )
    if opcion == 'Encontrar Calificacion más alta':
        if len( controller.evaluaciones ) > 0:
            mejor_calificacion = EvaluacionEstudiante()
            for i in controller.evaluaciones:
                if i.nota > mejor_calificacion.nota:
                    mejor_calificacion.nota = i.nota
            st.subheader( "El estudiante con mejor calificiacion es:" + mejor_calificacion.nombre_autor )
            st.subheader("Id:" + mejor_calificacion.id_estudiante)
            st.subheader("Trabajo:" + mejor_calificacion.nombre_trabajo)
            st.subheader("Trabajo:" + mejor_calificacion.nombre_trabajo)
            st.subheader("Nota: " + str(round(mejor_calificacion.Nota, 1)))
        else:
            st.error( "No han calificado a nadie" )



