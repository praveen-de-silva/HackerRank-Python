cube = lambda x: x**3

def fibonacci(n):
    if n<=0:
        return []
    elif n==1:
        return [0]
    elif n==2:
        return [0, 1]
    else:
        fibList = [0, 1]
        nElements = 2

        while True:
            fibList.append(fibList[-2]+fibList[-1])
            nElements += 1

            if nElements==n:
                return fibList

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))