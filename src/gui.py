from sys import path 
import slint

path.insert(0, 'gui')
gui_style = (
    'cosmic',
    'cosmic-dark',
    'cosmic-light',
    'cupertino',
    'cupertino-dark',
    'cupertino-light',
    'fluent',
    'fluent-dark',
    'fluent-light',
    'material',
    'material-dark',
    'material-light'
)
selected_style = gui_style[-2]

class GUI(slint.load_file('gui/app-window.slint', style=selected_style).MainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)