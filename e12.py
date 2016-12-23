from math import *

def divisors_triangle_number(limit):
    triangle = [1, ]
    divisors = []

    while len(divisors) <= limit:
        triangle.append(len(triangle)*(len(triangle)+1)/2)
        
        divisors = [1, triangle[-1]]
        for i in range(2, int(sqrt(triangle[-1]))+1):
            if triangle[-1] % i == 0:
                divisors.insert(len(divisors)/2, i) 
                
                if i*i != triangle[-1]:
                    divisors.insert(len(divisors)/2+1, triangle[-1]/i)
                
    return triangle[-1], len(triangle)

if __name__ == "__main__":
    res, number = divisors_triangle_number(500)

    print res
    print number
