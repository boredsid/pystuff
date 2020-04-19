import numpy as np

def powerSetGenerator(arr):
    res = []
    res.append(arr)
    for subset in res:
        for elem in subset:
            temp = [x for x in subset if x!=elem]
            res.append(temp)
    return res

def main():
    arr = input("Enter the Set (comma separated): ").split(",")
    s = [*np.unique(powerSetGenerator(arr))]
    print("The Power Set is: " + str(s))

if __name__ == '__main__':
    main()