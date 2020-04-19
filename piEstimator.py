import random

def estimate_pi(n,mode=0):
    circle_count = 0
    total_count = 0
    for _ in range(int( n/(1 + mode) )):
        x = random.uniform(0,1)
        y = random.uniform(0,1)
        dist = x**2 + y**2
        if dist <= 1:
            circle_count += 1
        total_count += 1
    return 4 * circle_count/total_count

def main():
    try:
        N = int(eval(input("Enter the Number of Points to Use: ")))
        print("The estimated Value of Pi is :" + str(estimate_pi(N)))
    except:
        print("Error, Please Check the Input!")

if __name__ == '__main__':
    main()
