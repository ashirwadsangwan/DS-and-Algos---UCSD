def maxPairProd(numbers):
    maxProd = 0
    for i in range(len(numbers)):
        for j in range(i+1,len(numbers)):
            
            maxProd = max(maxProd, (numbers[i] * numbers[j]))
    
    return maxProd

if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    print(maxPairProd(arr))