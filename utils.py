def format_number(value, prefix=''):
    for unit in ['','mil']:
        print(unit)
        print(value)
        if value < 1000:
            return f'{prefix} {value:.2f} {unit}'
        value /= 1000 # Move the division by 1000 outside the if condition
        print(value)
    return f'{prefix} {value:.2f} milhões'

formatted_number = format_number(1234567.89, prefix='$')  
print(formatted_number)