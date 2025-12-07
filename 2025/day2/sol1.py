filename = './2025/day2/ex1'

def read_file(filename):
    with open(filename) as fh:
        s = fh.read()
        ranges = [i.strip().split('-') for i in s.split(',')]
        return ranges
        

def refine_range(ranges):
    '''
    1. Seperates different digit numbers so 95- 115 => 95 - 99 and 100 - 115
    2. Ignores odd no. of  digits
    3. Changes bound to minimum and maximum bound => 10 - 23 => 11 - 22
    4. Only stores the first half numbers => 11 - 22 => 1 - 2
    
    :param ranges: [[from, to], ...]

    Returns refined_ranges
    '''
    refined_ranges = []
    for lower, upper in ranges:
        temp = [(lower, upper)]
        if len(lower) != len(upper): # Ex: 12 - 1024
            temp = split_range_by_len(upper, lower)
        refined_ranges.extend(temp)
    
    refined_ranges = filter_even_digits(refined_ranges)
    print('After Filter: ', refined_ranges)
    refined_ranges = [resize_bounds(*range) for range in refined_ranges]
    print('After Resize ', refined_ranges)

    return refined_ranges


def split_range_by_len(upper, lower):
    temp = []
    diff = len(upper) - len(lower) # 2
    temp.append((lower, pow10l(len(lower)))) # 12 - 99

    for i in range(diff - 1):
        temp.append((pow10(len(lower) + i), pow10l(len(lower) + i + 1)))

    temp.append((pow10(len(upper) - 1), upper))
    return temp

def filter_even_digits(ranges):
    temp = []
    for range in ranges:
        if range is None: continue
        if len(range[0]) % 2 == 0: 
            temp.append(range)
    return temp

def resize_bounds(lower, upper): # 10 - 23 => 11 - 22
    length = len(lower)
    l_half, u_half = lower[:length//2], upper[:length//2]
    if l_half * 2 < lower: l_half = str(int(l_half) + 1)
    if u_half * 2 > upper: u_half = str(int(u_half) - 1)

    return (l_half, u_half) if l_half <= u_half else None

def compute_invalid(ranges):
    s = 0
    for r in ranges:
        if r is None: continue
        l, u = r
        count = int(u) - int(l) + 1

        for i in range(count):
            value = str(int(l) + i)*2
            s += int(value)

    return s
    

def pow10l(n):
    return str(pow(10, n) - 1)


def pow10(n):
    return str(pow(10, n))


def main():
    range = refine_range(read_file(filename))
    invalids = compute_invalid(range)
    return invalids

if __name__ == '__main__':
    print(main())