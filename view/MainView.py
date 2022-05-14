import streamlit as st
from PIL import Image
from streamlit_option_menu import option_menu
from controller.EvalController import EvaluadorController
from controller.CriterioController import CriterioController
from controller.ActaController import ActaController
from view.AboutPartial import consultar_instrucciones
from view.Evaluar import listar_evaluacion, agregar_evaluacion
from view.ConfigurarCriterios import seleccionar_opcion
from view.CrearActa import crearActa
from view.InicilizarActa import  agregar_datos
from view.InformacionActas import listar_actas
from view.AnliticaDato import analisis




class MainView:
    def __init__(self) -> None:
        self.criterios = []
        super().__init__()

        # Estretagia para manejar el "estado" del controllador y del modelo entre cada cambio de ventana
        if 'main_view' not in st.session_state:
            self.menu_actual = "About"

            # Conexión con el controlador
            self.controller = EvaluadorController()
            self.criterios_controller = CriterioController()
            self.actas_controller = ActaController()

            st.session_state['main_view'] = self
        else:

            # Al exisir en la sesión entonces se actualizan los valores
            self.menu_actual = st.session_state.main_view.menu_actual
            self.controller = st.session_state.main_view.controller
            self.criterios_controller = st.session_state.main_view.criterios_controller
            self.actas_controller = st.session_state.main_view.actas_controller

        self._dibujar_layout()

    def _dibujar_layout(self):
        img = Image.open( "C:\\Users\\willi\\Downloads\\streamlit_example_app-main\\streamlit_example_app-main\\view\\puj_logo_vertical_azul_copia.png" )
        # Set page title, icon, layout wide (more used space in central area) and sidebar initial state
        st.set_page_config  (page_title="Calificar trabajos finales", page_icon = img, layout="wide",
                           initial_sidebar_state="expanded")
        # Defines the number of available columns del area principal
        self.col1, self.col2, self.col3, self.col4, self.col5, self.col6, self.col7, self.col8 = st.columns([1, 1, 1, 1, 1, 1, 1, 1])

        # Define lo que abrá en la barra de menu
        with st.sidebar:
            self.menu_actual = option_menu("Menu", ["About", 'Inicilizar datos actas' , 'Criterios', 'Evaluar nuevo trabajo', 'Calificaciones', 'Acta', 'Resumen actas', 'Estadisticas'],
                                           icons=['house', 'house' , 'card-list', 'clipboard', 'clipboard-check'], menu_icon="cast", default_index=1)

    def controlar_menu(self):
        if self.menu_actual == "About":
            texto = consultar_instrucciones()
            st.write(texto)
        elif self.menu_actual == "Inicilizar datos actas":
            agregar_datos(st, self.controller, self.criterios_controller)
        elif self.menu_actual == "Criterios":
            seleccionar_opcion(st, self.criterios_controller)
        elif self.menu_actual == "Evaluar nuevo trabajo":
            agregar_evaluacion(st, self.controller, self.criterios_controller)
        elif self.menu_actual == "Calificaciones":
            listar_evaluacion(st, self.controller, self.criterios_controller)
        elif self.menu_actual == "Acta":
            crearActa(st, self.actas_controller, self.controller)
        elif self.menu_actual == "Resumen actas":
            listar_actas( st, self.criterios_controller, self.actas_controller )
        elif self.menu_actual == 'Estadisticas' :
            analisis( st, self.controller, self.criterios_controller )




# Main call

if __name__ == "__main__":
    main = MainView()
    main.controlar_menu()