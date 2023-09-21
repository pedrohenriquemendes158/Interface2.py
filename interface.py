import PySimpleGUI as sg

sg.theme('BlueMono')

layout = [[sg.Text("Qual seu nome?")],
          [sg.Input(key='INPUT')],
          [sg.Text(size=(20,1), key='-OUTPUT-')],
          [sg.Text("Digite uma mensagem")],
          [sg.Input(key='INPUT2')],
          [sg.Text(size=(40,1), key='-OUTPUT-')],
          [sg.Button('Ok'), sg.Button('Quit')]
          ]

window = sg.Window('Trabalho', layout)


while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED or event == 'Quit':
        break

    if event == 'Ok':
        layout2 = [
            [sg.Text(values['INPUT'] +',' + ' ' + values['INPUT2'])],
            [sg.Text(size=(40,1), key='-OUTPUT-')],
            [ sg.Button('Quit')],
        ]
        window2 = sg.Window('Trab', layout2)
        event, values = window2.read()

        if event == sg.WINDOW_CLOSED or event == 'Quit':
            break

window.close()