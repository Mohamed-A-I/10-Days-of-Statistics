n = input()
x = sorted(list(map(int, input().split())))

def getMedian(arr):
    siz = len(arr)
    #all quartiles are integers
    return (arr[(siz-1)//2] + arr[siz//2]) // 2

print(getMedian(x[:len(x)//2]))
print(getMedian(x))
print(getMedian(x[-(len(x)//2):]))
