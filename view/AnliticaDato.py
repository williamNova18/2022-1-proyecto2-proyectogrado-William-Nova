from model.EvalEstudiante import EvaluacionEstudiante
import yfinance as yf
import matplotlib.pyplot as plt



def analisis(st, controller):
    opcion = st.radio( "Que analisis quieres hacer?", ('Encontrar Calificacion más alta', 'notas estudiantes') )
    if opcion == 'Encontrar Calificacion más alta':
        if len( controller.evaluaciones ) > 0:
            mejor_calificacion = EvaluacionEstudiante()
            for i in controller.evaluaciones:
                if i.nota > mejor_calificacion.nota:
                    mejor_calificacion = i
            st.subheader( "El estudiante con mejor calificiacion es: " + mejor_calificacion.nombre_autor )
            st.subheader("Id:" + mejor_calificacion.id_estudiante)
            st.subheader("Trabajo:" + mejor_calificacion.nombre_trabajo)
            st.subheader("Trabajo:" + mejor_calificacion.nombre_trabajo)
            st.subheader("Nota: " + str(round(mejor_calificacion.nota, 1)))
        else:
            st.error( "No han calificado a nadie" )
    elif opcion == 'notas estudiantes':
        notas = []
        nombres = []
        for i in controller.evaluaciones:
            if len(i.calificacion) > 0:
                nombres.append(i.nombre_autor)
                notas.append( i.nota )
        print( notas )
        fig = plt.figure(figsize=(10, 5))
        plt.bar(nombres, notas)
        plt.xlabel("Notas de estudiantes")
        plt.ylabel("Nombre estudiantes")
        plt.title("Notas")
        st.pyplot(fig)


