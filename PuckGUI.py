import PySimpleGUI as gui

def win_window():
    layout = [[gui.Text("Brawo! Wygrałeś talon na kurwę i balon!")], [gui.Button("OK")]]
    window = gui.Window("Wygrana", layout)
    while True:
        event, values = window.read()
        # End program if user closes window or
        # presses the OK button
        if event == "OK" or event == gui.WIN_CLOSED:
            break
    window.close()