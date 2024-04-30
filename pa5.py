"""HW5 Code"""

def gcd(a, b):
  '''Greatest common divisor'''
  
  if a >= b:
    pass 
  else:
    a, b = b, a #swap values if a < b
  if b == 0:
    return a #base case
  return gcd(b, a % b)

def remove_pairs(string):
  '''Remove u-turns in direction'''
  
  if 'EW' not in string and 'WE' not in string and \
  'NS' not in string and 'SN' not in string:
    return string
  if 'EW' not in string[0:2] and 'WE' not in string[0:2] and \
  'NS' not in string[0:2] and 'SN' not in string[0:2]:
    return remove_pairs(string[0]) + remove_pairs(string[1:])
  else:
    return remove_pairs(string[2:])
  
def bisection_root(func, x1, x2):
  '''find root of function using bisection method'''
  
  if (-0.001 < func(x1) < 0.001):
    return round(x1,2)
  elif (-0.001 < func(x2) < 0.001):
    return round(x2,2)
  else:
    new_x = x1 + abs(x1-x2)/2
    if (func(new_x) * func(x1)) > 0:
      return bisection_root(func, new_x, x2)
    else:
      return bisection_root(func, x1, new_x)
