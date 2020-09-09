from functools import cmp_to_key
arr = [[1,2,3], [3,2,1],[4,2,1], [6,4,3]]
# arr = [[7,9,5,6],[3,9,5],[3,2,9,8],[3,7,4,1],[3,6,4,0],[2,9,5,8],[6,2,5,6],[5,0,2,8],[2,5,7,7],[7,9,9,8],[7,0,4,8],[3,2,8,7],[1,4,9],[7,0,6,2],[2,8,6,8],[4,4,3,4],[3,6,9],[1,2,9],[8,1,2,0],[2,6,6,5]]
indices =[[4,1], [1,1]]


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


def indexSort (arr, indices):
    addZeroPadding(arr)
    max_size = max(len(x) for x in arr)
    for index in range(len(indices)):
        if index == 0:
            # arr.sort(key = lambda x: x[indices[index][0]], reverse=isReverse(indices[index]))
            sort_index =  max_size -1 if indices[index][0] == max_size else indices[index][0]
            arr = sorted(arr, key = lambda x: x[sort_index], reverse=isReverse(indices[index]))
        else:
            print(arr)
            sort_index =  max_size - 1 if indices[index][0] == max_size else indices[index][0]
            primary_sort_index = max_size - 1 if indices[index - 1][0] == max_size else indices[index - 1][0]
            tied_records = tiedRecords(arr, primary_sort_index)
            import pdb; pdb.set_trace()
            arr[tied_records[0]: tied_records[-1] + 1] = sorted(arr[tied_records[0]: tied_records[-1] + 1], key= lambda x: x[sort_index], reverse=isReverse(indices[index]))
            arr[tied_records[-1] + 1: len(arr) + 1] = sorted(arr[tied_records[-1] + 1: len(arr) + 1], key= lambda x: x[sort_index], reverse=isReverse(indices[index]))

            print(arr)
                
            
                
if __name__ == "__main__":
    indexSort(arr, indices)