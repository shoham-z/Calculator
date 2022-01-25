OPERATIONS = ['+', '-', '*', 'X', 'x', '/', ':', '^', '%']


def add(num1, num2):
    """
        adds two numbers and return the answer
        :params:
            num1 - the first number
            num2 - the second number
        :returns:
            num1+num2
        """
    result = num1 + num2
    if result.is_integer():
        return int(result)
    return result


def sub(num1, num2):
    """
        subtracts two numbers and return the answer
        :params:
            num1 - the first number
            num2 - the second number
        :returns:
            num1-num2
        """
    result = num1 - num2
    if result.is_integer():
        return int(result)
    return result


def multiply(num1, num2):
    """
        multiplies two numbers and return the answer
        :params:
            num1 - the first number
            num2 - the second number
        :returns:
            num1*num2
        """
    if num1 == 0 or num2 == 0:
        return 0
    else:
        result = num1 * num2
        if result.is_integer():
            return int(result)
        return num1 * num2


def divide(num1, num2):
    """

    :param num1: the dividend
    :param num2:the divisor
    :return:
    """
    if num2 == 0:
        return "CANT DIVIDE BY ZERO"
    result = num1/num2
    if result.is_integer():
        return int(result)
    return result


def power(num1, num2):
    """
    computes the value num1^num2 and returns it
    :param num1:
    :param num2:
    :return: num1^num2
    """
    result = 0
    if num1 == 1:
        result = 1
    else:
        if num2 == 0:
            result = 1
        elif num2 == 1:
            result = num1
        else:
            result = num1 ** num2
    if result.is_integer():
        return int(result)
    return result


def percent(num):
    """
    takes a number and pretty much divides it by 100. including rounding
    :param num: the number to return % of
    :return: the value
    """
    result = num / 100
    if result.is_integer():
        return int(result)
    return result


def find_operation(question):
    for arg in question:
        if arg in OPERATIONS:
            operation = OPERATIONS[OPERATIONS.index(arg)]
            return question.find(arg)
    return -1


def calculate(question):
    """
    This is the main function of the calculating process
    :param question: The calculation to solve
    :return: the solution\result of the calculation
    """
    solution = 0
    if question == '':
        return None, False
    else:
        operation_index = find_operation(question)
        if operation_index > 0:
            first_number = question[:operation_index]
            operation = question[operation_index]
            second_number = question[operation_index + 1:]
            if '%' in first_number:
                first_number = percent(first_number)
            if '%' in second_number:
                second_number = percent(second_number)
            if first_number != '' and second_number != '':
                if operation == OPERATIONS[0]:
                    solution = add(float(first_number), float(second_number))
                elif operation == OPERATIONS[1]:
                    solution = sub(float(first_number), float(second_number))
                elif operation in OPERATIONS[2:5]:
                    solution = multiply(float(first_number), float(second_number))
                elif operation in OPERATIONS[5:7]:
                    solution = divide(float(first_number), float(second_number))
                elif operation == OPERATIONS[7]:
                    solution = power(float(first_number), float(second_number))
                exercise = str(first_number) + ' ' + str(operation) + ' ' + str(second_number) + ' = ' + str(solution)
                return exercise, False
            return 'INVALID SYNTAX', True
        elif operation_index == -1:
            if question.isdigit():
                return question, False
            else:
                return operation_index, True
        else:
            return "Something else went wrong in the program", True
