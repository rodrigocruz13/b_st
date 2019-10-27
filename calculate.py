#!/usr/bin/python3

import os
import sys


def clear_screen():
    # clear the screen
    """
    Purpose:   Function that clear the screen according to the OS
    Arguments: - None.
    Returns:   - Nothing.
    """

    if (sys.platform != 'linux'):
        # For Windows
        os.system('cls')
    else:
        # For Linux/OS X
        os.system('clear')


def print_menu(size):
    # Print a menu and reads data from the user
    """
    Purpose:   Print a menu to read two values: user and units.
    Arguments: - size: Number of ids of the data file 'out.txt'
    Returns:   - list (lst): list with the two read values (user-id and units)
    """

    user = -1
    user_id = 1
    while (user <= 0 or user > size):
        bar = '-' * 60
        print('\n\t', bar)
        print('\t  Type q to quit')
        user_id = input('\t  Type the id of the user:\t')
        if (user_id == 'q' or user_id == 'Q'):
            clear_screen()
            exit(1)

        try:
            user = int(user_id)
        except BaseException:
            pass

        no_color = '\x1b[0m  '
        yellow_color = '\x1b[1;33;40m'

        if (user <= 0 or user >= size):
            msg = yellow_color + '\tThat id doesnt exist' + no_color
            print('\t  {}'.format(msg))

    un = -5
    units = 5
    while (un < 1 or un > 50000):
        units = input("\t  # of units to get id {}'s" ' cost:\t'.format(user))
        if (units == 'q' or units == 'Q'):
            clear_screen()
            exit(1)

        try:
            un = int(units)
        except BaseException:
            pass

        if (un < 1 or un >= 50000):
            msg = yellow_color + '\tThat value can not be estimated' + no_color
            print('\t  {}'.format(msg))

    return ([user, un])


def load_data_from_file(name):
    # Loads the file and returns a list
    """
    Purpose:   Gets a list from a text file with the "name" provided.
    Arguments: - name (str): Name of the text file.
    Returns:   - data_list: list of lists with this data structure:
                 user_id: list with the ids of each user
                 fields[5]: list with the cost of producing 50000 units
                 fields[4]: list with the cost of producing 5000 units
                 fields[3]: list with the cost of producing 500 units
                 fields[2]: list with the cost of producing 50 units
                 fields[1]: list with the cost of producing 5 units
    """

    data = []
    f = open(name, 'r')
    i = 0
    for line in f:

        fields = line.rstrip().split(',')
        temp = []
        if (i != 0):
            temp.append(int(fields[0]))
            temp.append(float(fields[5]))
            temp.append(float(fields[4]))
            temp.append(float(fields[3]))
            temp.append(float(fields[2]))
            temp.append(float(fields[1]))
            data.append(temp)
        i += 1

    f.close()
    return (data)


def generate_equations(data):
    # Generates the slope (m) and the y intersection (b) for all 4 ranges
    """
    Purpose:   Gets the slope (m) and the y intersection (b) for all 4 ranges.
    Arguments: - data (lst): list with values to calculate the equations.
    Returns:   - equations: list of five lists with this data structure:
                [values[0]: user_id
                m0: slope for range 0
                b0: y intersection for range 0
                m1: slope for range 1
                b1: y intersection for range 1
                m2: slope for range 2
                b2: y intersection for range 2
                m3: slope for range 3
                b3: y intersection for range 3
    """
    equations = []

    for values in data:
        m0 = (values[2] - values[1]) / (50 - 5)
        b0 = (values[1] - m0 * 5)
        m1 = (values[3] - values[2]) / (500 - 50)
        b1 = (values[2] - m1 * 50)
        m2 = (values[4] - values[3]) / (5000 - 500)
        b2 = (values[3] - m2 * 500)
        m3 = (values[5] - values[4]) / (50000 - 5000)
        b3 = (values[4] - m3 * 5000)
        equations.append([values[0], m0, b0, m1, b1, m2, b2, m3, b3])

    return (equations)


def estimate_value(op, equations):
    # Generates the quote for u units and user op[0]
    """
    Purpose:   Estimate the cost value of producing u units.
    Arguments: - op (lst): list with two arguments.
                 user_id: op[0]. user id
                 units: [op[1] number of untis to estimate
               - equations: list of five lists with this data structure:
                [values[0]: user_id
                m0: slope for range 0
                b0: y intersection for range 0
                m1: slope for range 1
                b1: y intersection for range 1
                m2: slope for range 2
                b2: y intersection for range 2
                m3: slope for range 3
                b3: y intersection for range 3
    Returns: The estimated cost of producting u units for user user_id
    """

    user_id = op[0]
    value = op[1]

    for lists in equations:
        if(user_id == lists[0]):
            if(value >= 0 and value < 50):
                m = lists[1]
                b = lists[2]
                break

            elif(value >= 50 and value < 500):
                m = lists[3]
                b = lists[4]
                break

            elif(value >= 500 and value < 5000):
                m = lists[5]
                b = lists[6]
                break

            elif(value >= 5000 and value <= 50000):
                m = lists[7]
                b = lists[8]
                break

    return (m * value + b)


def print_results(op, estimated):
    # print the results of estimating
    """
    Purpose:   Show the results of estimating a cost of producing op[1] un
               for user op[0].
    Arguments:  - op (lst): list with two arguments.
                 user_id: op[0]. user id
                 units: [op[1] number of untis to estimate
                - estimated (float): value estimated
    """

    no_color = '\x1b[0m  '
    green_color = ' \x1b[1;32;40m'

    print('\t\tId [{:d}] will quote {}u for{}US$ {:6.3f}{}'.format(
        op[0], op[1], green_color, estimated, no_color))


def find_smaller(op, equations):
    # find the 15 first smaller bidders
    """
    Purpose:   find the 15 first smaller bidders for producing u units
    Arguments:  - op (lst): list with two arguments.
                 user_id: op[0]. user id
                 units: [op[1] number of untis to estimate
                - equations: list of five lists with this data structure:
                [user_id, m0, b0, m1, b1, m2, b2, m3, b3]
                user_id: list_of the ids
                m0: slope for line 0 in range 0
                b0: y intersection for line 0 in range 0
                m1: slope for line 1 in range 1
                b1: y intersection for line 1 in range 1
                m2: slope for line 2 in range 2
                b2: y intersection for line 2 in range 2
                m3: slope for line 3 in range 3
                b3: y intersection for line 3 in range 3
    Returns: The estimated cost of producting u units for user user_id
    """

    user = 1
    quotations = []
    for lists in equations:
        new_op = [user, op[1]]
        estimated = estimate_value(new_op, equations)

        if (estimated >= 0):
            temp = []
            temp = [estimated, user]
            quotations.append(temp)
        user += 1

    quotations.sort()
    print('\t\t15 cheapest quotations of {}u:'.format(op[1]))

    no_color = '\x1b[0m  '
    green_color = ' \x1b[1;32;40m'
    yellow_color = ' \033[0m 1;33;40m'

    i = 0
    cont = 0
    while(cont < 15):
        line = quotations[i]
        value = float(line[0])
        if(value > 0):
            user = int(line[1])
            print('\t\t{:2d}\tUser:\t{:d}\t{}US${:6.3f}{}'.format(
                cont + 1, user, green_color, value, no_color))
            cont += 1
        i += 1
