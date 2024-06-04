def sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        
        arr[i],arr[min_index] = arr[min_index],arr[i]

    return arr

def sort2(arr):

    def find_min(min_index, start):
        if start == len(arr):
            return min_index
        
        if arr[start] < arr[min_index]:
            min_index = start
            
        return find_min(min_index, start + 1)


    def helper(index):
        if index == len(arr):
            return arr
        
        min_index = find_min(index, index+1)
        arr[index], arr[min_index] = arr[min_index], arr[index]
        return helper(index + 1)

    return helper(0)


print(sort([4,5,3,7,1,8]))
print(sort([4,5,3,7,1,8,1,3]))
print(sort([]))
print(sort([1]))
print(sort2([4,5,3,7,1,8]))
print(sort2([4,5,3,7,1,8,1,3]))
print(sort2([]))
print(sort2([1]))