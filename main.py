import PySimpleGUI as sg
import Calculator as calc
import Files as file


NUMBERS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
OPERATIONS = ['+', '-', '*', '/', '^', '%']


def main():
    bigger_font = ("Arial", 12)
    sg.set_options(font=bigger_font)
    sg.theme('DarkAmber')  # Add a touch of color
    # All the stuff inside your window.
    layout = [[sg.Multiline(reroute_stdout=True, autoscroll=True, size=(20,4))],
              [sg.Button(button_text='7', size=2), sg.Button(button_text='8', size=2),
               sg.Button(button_text='9', size=2), sg.Button(button_text='+', size=2),
               sg.Button(button_text='C', size=2)],
              [sg.Button(button_text='4', size=2), sg.Button(button_text='5', size=2),
               sg.Button(button_text='6', size=2), sg.Button(button_text='-', size=2),
               sg.Button(button_text='%', size=2)],
              [sg.Button(button_text='1', size=2), sg.Button(button_text='2', size=2),
               sg.Button(button_text='3', size=2), sg.Button(button_text='*', size=2),
               sg.Button(button_text='^', size=2)],
              [sg.Button(button_text='0', size=10), sg.Button(button_text='/', size=2),
               sg.Button(button_text='⌫', size=2)],
              [sg.Button('=', font=("Arial", 18)), sg.Button('Close')]]

    # Create the Window
    window = sg.Window('Calculator', layout)
    history = file.open_history()
    exercise = ''
    # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Close':  # if user closes window or clicks cancel
            break
        if event in NUMBERS or event in OPERATIONS[:-1]:
            print(event, end='')
            exercise = exercise + event
        elif event == '⌫':
            window[0].update(value='', append=False)
            exercise = exercise[:-1]
            print(exercise, end='')
        elif event == 'C':
            window[0].update(value='', append=False)
            exercise = ''
        else:
            calculation = exercise.split('\n')[-1]
            exercise, operation_not_supported = calc.calculate(calculation)
            if operation_not_supported:
                print('\n' + exercise)
                exercise = ''
            elif exercise is None:
                pass
            else:
                lst = exercise.split(' ')
                result = lst[-1]
                print('\n' + result)
                file.append_line(history, exercise)
                exercise = ''

    history.close()
    window.close()


if __name__ == '__main__':
    main()
