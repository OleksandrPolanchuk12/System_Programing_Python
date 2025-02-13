import sys
import math

def taylor_series_exp(x):
    result = 0
    for n in range(300000):
        result += x + 1 * (n+2)
    return result

def main():
    A = float(sys.argv[1])
    B = float(sys.argv[2])
    steps = float(sys.argv[3])

    step_size = (B - A) / steps 

    terms = 1  
        
    for i in range(1,int(step_size)):  
        x = A + terms * step_size
        result = taylor_series_exp(x)
        print(f"{terms}  x = ({x}) result = {result}")
        terms+=1

if __name__ == "__main__":
    main()
