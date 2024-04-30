"""HW5 Code"""

def gcd(a, b):
  if a >= b:
    continue
  else:
    a, b = b, a #swap values if a < b
  if b == 0:
    return a #base case
  while b!= 0:
    gcd(a,b) = gcd(b, a % b) 
    return a 

  
  
