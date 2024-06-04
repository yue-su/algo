def matrixMultiply(a, b):

    res = []

    for i in range(len(a)):
        temp = []
        for j in range(len(b[0])):
            sum = 0
            for k in range(len(a[0])):
                sum += a[i][k] * b[k][j]
            temp.append(sum)
        res.append(temp)
    
    print(res)
    return res



a = [[]]
b = [[]]
print(matrixMultiply(a,b) == [[]] or matrixMultiply(a,b) == [[None]])

a = [[5]]
b = [[10]]
print(matrixMultiply(a,b) == [[50]])

a = [
  [1, 2],
  [3, 4]]
b = [
  [5, 6],
  [7, 8]]
print(matrixMultiply(a,b) == [
  [19,22],
  [43,50]])

a = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]]
b = [
  [10, 20, 30],
  [40, 50, 60],
  [70, 80, 90]]
print(matrixMultiply(a,b) == [
  [300,360,420],
  [660,810,960],
  [1020,1260,1500]])

a = [[1, 2, 3]]
b = [
  [4],
  [5],
  [6]]
print(matrixMultiply(a,b) == [[32]])

a = [
  [1, 2, 3],
  [4, 5, 6]]
b = [
  [10, 20],
  [30, 40],
  [50, 60]]
print(matrixMultiply(a,b) == [
  [220,280],
  [490,640]])