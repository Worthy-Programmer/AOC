matrix = []
filename = './2025/day6/input'

def read_file(filename):
    global matrix
    with open(filename) as fh:
        rows = fh.readlines()
        matrix = [row.split() for row in rows]
       

def compute(col_no):
    col = [matrix[i][col_no] for i in range(len(matrix))]
    operator = col.pop()
    operation_str = operator.join(col)
    # print(col)

    return eval(operation_str)


def main():
    read_file(filename)
    
    result = 0
    for i in range(len(matrix[0])):
        sol = compute(i)
        # print(sol)
        result += sol

    print('Result = ', result)

main() 
    

