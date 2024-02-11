#### A very simple gui to simplify using the program.


import PySimpleGUI as gui 

enter_name= 'Enter Gamer Name'

layout=[
    [gui.Text("Enter Gamer IDs:")],
    [gui.Input(enable_events= True, key='-GAMER-')],
    [gui.Text("Select Stats to Scrape:")],
    [gui.Checkbox("KD", key = '-KD-'),gui.Checkbox("Rank", key = '-RANK-')],
    [gui.Button("OK")]
]

window = gui.Window("R6 Stat Scrape", layout)

while True: 
    event, values = window.read()

    if event == gui.WINDOW_CLOSED or event =="OK":
        break 
    

window.close()

print(values)
