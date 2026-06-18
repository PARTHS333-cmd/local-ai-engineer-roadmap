from datetime import datetime

def get_current_time():

    return datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S"
    )

def calculator(expression):

    try:

        result = eval(expression)

        return str(result)

    except Exception:

        return "Invalid expression"