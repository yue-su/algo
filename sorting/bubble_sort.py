def sort(arr):

    n = len(arr)
    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]

    return arr


def sort2(arr):

    def bubble(start, index):
        if start == len(arr) - index - 1:
            return
        if arr[start] > arr[start + 1]:
            arr[start],arr[start+1] = arr[start+1],arr[start]
        bubble(start + 1, index)
    
    def helper(index):
        if index == len(arr):
            return arr
        
        bubble(0, index)
        return helper(index + 1)

    return helper(0)


print(sort2([4,5,3,7,1,8]))
print(sort2([4,5,3,7,1,8,1,3]))
print(sort2([]))
print(sort2([1]))

        
        

        
            
