def escape_table(escape_element, name):
    if 11 < len(name) < 20:
        tab_number = 3
    elif len(name) < 10 or len(name) == 11:
        tab_number = 4
    elif len(name) > 20:
        tab_number = 1
    else:
        tab_number = 0
    return f"|\t{escape_element}\t|\t{name}" + "\t" * tab_number + "|"

if __name__ == "main":
    print("Escape sequences table:")
    print("-" * 37)
    escape_table(r'\a', 'Bell (alert)')
    escape_table(r'\b', 'Backspace')
    escape_table(r'\n', 'New line')
    escape_table(r'\t', 'Horizontal tab')
    escape_table(r'\\', 'Backslach \\')
    escape_table(r'\"', 'Double quotation mark \"')
    escape_table(r'\'', 'Single quotation mark \'')
    print("-" * 37)