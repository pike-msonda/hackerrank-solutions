from functools import cmp_to_key
# arr = [[7,9,5,6],[3,9,5],[3,2,9,8],[3,7,4,1],[3,6,4,0],[2,9,5,8],[6,2,5,6],[5,0,2,8],[2,5,7,7],[7,9,9,8],[7,0,4,8],[3,2,8,7],[1,4,9],[7,0,6,2],[2,8,6,8],[4,4,3,4],[3,6,9],[1,2,9],[8,1,2,0],[2,6,6,5]]


def addZeroPadding(arr):
    max_size = max(len(x) for x in arr)
    [x.extend([0 for _ in range(max_size - len(x))]) for x in arr]


def isReverse(index):
    if (index[-1] != 0):
        return True
    return False

def tiedRecords(arr, index):
    # import pdb; pdb.set_trace()
    for i in range(len(arr)):
        if i != len(arr) - 1 :
            if arr[i][index] == arr[i + 1][index]:
                return [i, i + 1]
        return [i, i]


def sort(arr, currIndex, prevIndex):
    priArr = []
    otherArr = []
    val = prevIndex[0]
    for i in range(len(arr)):
        if len(otherArr) == 0:
            otherArr.append(arr[i])
        else:
            if arr[i- 1][val] == arr[i][val]:
                otherArr.append(arr[i])
            else:
                otherArr.sort(key = lambda x: x[currIndex[0]], reverse=isReverse(currIndex))
                priArr = priArr + otherArr
                otherArr = []
    return priArr


def indexSort (arr, indices):
    addZeroPadding(arr)
    for index in range(len(indices)):
        if index == 0: #primary sort
            arr.sort(key = lambda x: x[indices[index][0]], reverse=isReverse(indices[index]))
        else:
            arr = sort(arr, indices[index], indices[index  - 1])
    print(arr)
                
            
arr = [[1,2,1], [3,3,1],[4,2,3], [6,4,3]]
indices =[[1,0], [2,1]]
              
if __name__ == "__main__":
    indexSort(arr, indices)