The_names_list = ["john", "marta", "james", "Morgan", "Adam", "Maria", "huang"]

The_Names = "Names".center(48, "*")
format_to_the_right = "{:>48}\n" * len(The_names_list)
all_lines_nf = f'{The_Names}\n{format_to_the_right}'
print_text = all_lines_nf.format(*The_names_list)
print(print_text)