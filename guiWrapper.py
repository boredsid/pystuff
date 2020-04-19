import importlib
import builtins
import PySimpleGUI as sg

module_to_import = 'powerSet' # name of the python script to wrap with GUI
called_module = importlib.import_module(module_to_import)

_input = input

sg.theme('GreenTan')
layout = [  [sg.Text('Program Output: \n')],
            [sg.Output(size=(88,20))],
            [sg.Button('Run Program'), sg.Button('Exit')] ]
window = sg.Window('Run Your Python Program on GUI!', layout)

def custom_input(prompt_input):
    text_input = sg.PopupGetText(prompt_input,'Input Prompt')
    return text_input

builtins.input = custom_input

while True:
    event, values = window.read()
    if event in (None, 'Exit'):   # if user closes window or clicks cancel
        break
    if event == 'Run Program':  # is user clicks Run Program
        called_module.main()

window.close()
