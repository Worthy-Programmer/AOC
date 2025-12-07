import pprint
filename = './2025/day6/input'

# Exploiting the fact that the operators are only written in the first column of the problem.

def read_file(filename):
    with open(filename) as fh:
        lines = fh.readlines()
        max_len  = max([len(l) for l in lines])
        

        operation_line = lines.pop()
        operation_line += (max_len - len(operation_line)) * ' ' # Extending the length of operation line

        assert len(operation_line) == max_len

        operations = interpret_operation_line(operation_line)
        
        return lines, operations

def interpret_operation_line(l):
    operations = [] # ('*', length before the next operations)

    d = 0
    prev_op = None
    for i in l:
        if i in '*+':
            if prev_op is not None:
                operations.append((prev_op, d))
            prev_op = i
            d = 0
        else: d += 1
    
    operations.append((prev_op, d))

    return operations

def compute(operationt, lines, start):
    op, oplen  = operationt
    op_str = ''
    for i in range(start, start + oplen):
        for line in lines:
            if line[i].isdigit():
                op_str += line[i]
        op_str += op

    op_str = op_str.removesuffix(op)
    # print(op_str)

    try:
        return eval(op_str)
    except:
        print(operationt, start, op_str)

def main():
    lines, operations = read_file(filename)

    # pprint.pp(operations)
    start = 0
    res = 0
    for op_t in operations:
        res += compute(op_t, lines, start)
        start += op_t[1] + 1 # +1 because of the free column break

    print('Result = ',  res)

main()