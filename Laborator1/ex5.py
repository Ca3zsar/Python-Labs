#Ex5

def spiral(matrix):
    result = ''
    for i in range(len(matrix)//2):
        for k in range(i,len(matrix)-i):
            result += matrix[i][k]
        for k in range(i+1, len(matrix)-i):
            result += matrix[k][len(matrix)-i-1]
        for k in range(len(matrix)-i-2,i-1,-1):
            result += matrix[len(matrix)-i-1][k]
        for k in range(len(matrix)-i-2,i,-1):
            result += matrix[k][i]
    
    if len(matrix) % 2 == 1:
        result += matrix[len(matrix)//2][len(matrix)//2]
    
    return result

test = [
    ['f','i','r','s','t'],
    ['b','_','s','r','_'],
    ['a','y','e','s','p'],
    ['l','_','y','l','y'],
    ['_','n','o','h','t']
]

print(spiral(test))