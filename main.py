#!/usr/bin/python3

if __name__ == '__main__':

    clear_screen = __import__('calculate').clear_screen
    load_data_from_file = __import__('calculate').load_data_from_file
    print_menu = __import__('calculate').print_menu
    generate_equations = __import__('calculate').generate_equations
    estimate_value = __import__('calculate').estimate_value
    print_results = __import__('calculate').print_results
    find_smaller = __import__('calculate').find_smaller

    clear_screen()
    data = load_data_from_file('out.txt')
    equations = generate_equations(data)

    opt = [None, None]
    while (opt[0] != 'q' or opt[0] == 'Q' or opt[1] != 'q' or opt[1] == 'Q'):
        op = print_menu(len(equations))
        value = estimate_value(op, equations)
        print_results(op, value)
        find_smaller(op, equations)
