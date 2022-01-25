FILE_NAME = "Calculation history.txt"


def open_history():
    file = open(FILE_NAME, 'a')
    return file


def append_line(file, string):
    file.write(string + '\n')
    return
