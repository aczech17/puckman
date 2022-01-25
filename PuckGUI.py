import PySimpleGUI as gui

def win_window():
    layout = [[gui.Text("Brawo! Wygrałeś!")], [gui.Button("OK")]]
    window = gui.Window("Wygrana", layout)
    while True:
        event, values = window.read()
        # End program if user closes window or
        # presses the OK button
        if event == "OK" or event == gui.WIN_CLOSED:
            break
    window.close()


def lose_window():
    layout = [[gui.Text("Przegrałeś")], [gui.Button("OK")]]
    window = gui.Window("Przegrana", layout)
    while True:
        event, values = window.read()
        # End program if user closes window or
        # presses the OK button
        if event == "OK" or event == gui.WIN_CLOSED:
            break
    window.close()
