from datetime import datetime


def loger_decorator(old_function):

    def addition_to_the_func(*args, **kwargs):
        log_date = datetime.now().strftime('%m/%d/%Y, %H:%M:%S')
        function_name = old_function.__name__
        output_data = old_function(*args, **kwargs)
        result = f'Called function: {function_name} \n' \
            f'Date and time of the call: {log_date} \n' \
            f'Entered data: {args} and {kwargs} \n' \
            f'Final values of the {function_name} function: {output_data} \n'

        with open('logs.txt', 'a') as f:
            f.write(result)

        return output_data

    return addition_to_the_func
