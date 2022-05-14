import streamlit as st
from streamlit_option_menu import option_menu

from controller.EvalController import EvaluadorController
from view.AboutPartial import consultar_instrucciones
from view.EvalPartial import listar_evaluacion, agregar_evaluacion
from view.PruebaPartial import probar_streamlit


class MainView:
    def __init__(self) -> None:
        super().__init__()

        # Estretagia para manejar el "estado" del controllador y del modelo entre cada cambio de ventana
        if 'main_view' not in st.session_state:
            self.menu_actual = "About"

            # Conexión con el controlador
            self.controller = EvaluadorController()

            st.session_state['main_view'] = self
        else:

            # Al exisir en la sesión entonces se actualizan los valores
            self.menu_actual = st.session_state.main_view.menu_actual
            self.controller = st.session_state.main_view.controller

        self._dibujar_layout()

    def _dibujar_layout(self):
        # Set page title, icon, layout wide (more used space in central area) and sidebar initial state
        st.set_page_config(page_title="Análisis mercado energía", page_icon='', layout="wide",
                           initial_sidebar_state="expanded")
        # Defines the number of available columns del area principal
        self.col1, self.col2, self.col3 = st.columns([1, 1, 1])

        # Define lo que abrá en la barra de menu
        with st.sidebar:
            self.menu_actual = option_menu("Menu", ["About", 'PruebaStreamlit', 'EvaluarAvances', 'ListarEvaluaciones'],
                                           icons=['house', 'gear'], menu_icon="cast", default_index=1)

    def controlar_menu(self):
        """TODO poner aqui su codigo de interaccion"""
        if self.menu_actual == "About":
            texto = consultar_instrucciones()
            st.write(texto)
        elif self.menu_actual == "PruebaStreamlit":
            probar_streamlit(st)
        elif self.menu_actual == "EvaluarAvances":
            agregar_evaluacion(st, self.controller)
        elif self.menu_actual == "ListarEvaluaciones":
            listar_evaluacion(st, self.controller)


# Main call
if __name__ == "__main__":
    main = MainView()
    main.controlar_menu()
