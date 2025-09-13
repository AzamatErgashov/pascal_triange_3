# Numrows = 0

# res = [[1]]

# for i in range(Numrows-1):
#     temp = [0] + res[-1] + [0]
#     row = []
#     for item in range(len(res[-1])+1):
#         print(item)
#         row.append(temp[item] + temp[item + 1])
#     res.append(row)
# print(res)

# second solve code

def generative_row(prev):
    next_ = [1]

    for i in range(len(prev-1)):
        next_.append(prev[i] + prev[i+1])
    
    next_.append(1)

def generative(n):
    row = [1]
    result = [row]
    for i in range(n-1):
        row = generative_row(row)
        result.append(row)
    return result

    