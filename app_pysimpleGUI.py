import PySimpleGUI as sg
from app_database import *
sg.theme('Dark Red')

# ------ Make the Table Data ------
data = rows("employees")
headings = headers_list("classicmodels","employees")

# ------ Window Layout ------
layout = [[sg.Table(values=data, headings=headings, max_col_width=25,
                    # background_color='light blue',
                    auto_size_columns=True,
                    display_row_numbers=True,
                    justification='right',
                    num_rows=30,
                    # alternating_row_color='lightyellow',
                    key='-TABLE-',
                    row_height=35,
                    tooltip='This is a table')],
          [sg.Button('Read'), sg.Button('Double'), sg.Button('Change Colors')],
          [sg.Text('Read = read which rows are selected')],
          [sg.Text('Double = double the amount of data in the table')],
          [sg.Text('Change Colors = Changes the colors of rows 8 and 9')]]

# ------ Create Window ------
window = sg.Window('The Table Element', layout,resizable=True)

# ------ Event Loop ------
while True:
    event, values = window.read()
    print(event, values)
    if event == sg.WIN_CLOSED:
        break
    if event == 'Double':
        for i in range(len(data)):
            data.append(data[i])
        window['-TABLE-'].update(values=data)
    elif event == 'Change Colors':
        window['-TABLE-'].update(row_colors=((8, 'white', 'red'), (9, 'green')))

window.close()