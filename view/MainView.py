import streamlit as st
from PIL import Image
from streamlit_option_menu import option_menu
from controller.EvalController import EvaluadorController
from controller.CriterioController import CriterioController
from controller.ActaController import ActaController
from view.AboutPartial import consultar_instrucciones
from view.EvalPartial import listar_evaluacion, agregar_evaluacion
from view.PruebaPartial import seleccionar_opcion
from view.CrearActa import crearActa



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
        img = Image.open( "C:\\Users\\willi\\OneDrive\\Escritorio\\streamlit_example_app-main (1)\\streamlit_example_app-main\\view\\puj_logo_vertical_azul_copia.png" )
        # Set page title, icon, layout wide (more used space in central area) and sidebar initial state
        st.set_page_config  (page_title="Calificar trabajos finales", page_icon = img, layout="wide",
                           initial_sidebar_state="expanded")
        # Defines the number of available columns del area principal
        self.col1, self.col2, self.col3 = st.columns([1, 1, 1])

        # Define lo que abrá en la barra de menu
        with st.sidebar:
            self.menu_actual = option_menu("Menu", ["About", 'Criterios', 'Evaluar nuevo trabajo', 'Calificaciones', 'Acta'],
                                           icons=['house', 'card-list', 'clipboard', 'clipboard-check'], menu_icon="cast", default_index=1)

    def controlar_menu(self):
        """TODO poner aqui su codigo de interaccion"""
        if self.menu_actual == "About":
            texto = consultar_instrucciones()
            st.write(texto)
        elif self.menu_actual == "Criterios":
            seleccionar_opcion(st, self.criterios_controller)
        elif self.menu_actual == "Evaluar nuevo trabajo":
            agregar_evaluacion(st, self.controller, self.criterios_controller)
        elif self.menu_actual == "Calificaciones":
            listar_evaluacion(st, self.controller, self.criterios_controller)
        elif self.menu_actual == "Acta":
            crearActa(st, self.actas_controller, self.controller)



# Main call

if __name__ == "__main__":
    main = MainView()
    main.controlar_menu()