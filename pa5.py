"""HW5 Code"""

def gcd(num_1, num_2):
    '''Greatest common divisor'''

    if num_1 >= num_2:
        pass
    else:
        num_1, num_2 = num_2, num_1
    if num_2 == 0:
        return num_1
    return gcd(num_2, num_1 % num_2)


def remove_pairs(string):
    '''Remove u-turns in direction'''

    if 'EW' not in string and 'WE' not in string and \
        'NS' not in string and 'SN' not in string:
        return string
    if 'EW' not in string[0:2] and 'WE' not in string[0:2] \
        and 'NS' not in string[0:2] and 'SN' not in string[0:2]:
        return remove_pairs(string[0]) + remove_pairs(string[1:])
    else:
        return remove_pairs(string[2:])


def bisection_root(func, x_1, x_2):
    '''docstring'''

    if -0.0000001 < func(x_1) < 0.0000001:
        return x_1
    if -0.0000001 < func(x_2) < 0.0000001:
        return x_2
    else:
        new_x = x_1 + abs(x_1-x_2) / 2
        if func(new_x) * func(x_1) > 0:
            return bisection_root(func, new_x, x_2)
        else:
            return bisection_root(func, x_1, new_x)
