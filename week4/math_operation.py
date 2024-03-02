def basic_operations(a, b):
    try:
        addition = a + b
        subtraction = a - b
        multiplication = a * b
        division = a / b
        return {
            'addition': addition,
            'subtraction': subtraction,
            'multiplication': multiplication,
            'division': division
        }
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
        return None
    except Exception as e:
        print("Error:", str(e))
        return None

def power_operation(base, exponent, **kwargs):
    try:
        result = base ** exponent
        if 'modulo' in kwargs:
            modulo = kwargs['modulo']
            result = result % modulo
        return result
    except Exception as e:
        print("Error:", str(e))
        return None

def apply_operations(operation_list):
    try:
        results = []
        for operation in operation_list:
            function = operation[0]
            args = operation[1]
            result = function(*args)
            results.append(result)
        return results
    except Exception as e:
        print("Error:", str(e))
        return None