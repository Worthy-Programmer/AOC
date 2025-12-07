import sol1
filename = './2025/day2/ex1'

def split_ranges_by_len(ranges):
    refined_ranges = []
    for lower, upper in ranges:
        temp = [(lower, upper)]
        if len(lower) != len(upper): # Ex: 12 - 1024
            temp = sol1.split_range_by_len(upper, lower)
        refined_ranges.extend(temp)

    return refined_ranges

def resize_bounds(range, n, rep_len):
    lower, upper = range
    if n % rep_len: return None

    repeats = n // rep_len
    
    lpartial,  upartial = lower[:rep_len], upper[:rep_len]
    
    # print('lp', lpartial, upartial, rep_len)

    if lpartial * repeats < lower: lpartial = str(int(lpartial) + 1)
    if upartial * repeats > upper: upartial = str(int(upartial) - 1)

    if upartial < lpartial: return None
    return lpartial, upartial, repeats

def process_ranges(ranges): # Param - ranges with same length (u and l are same length)
    updated_ranges = []
    for r in ranges:
        l, u = r
        n = len(l)
        for rep_len in range(1, n//2 + 1):
            # print(rep_len)
            ran = resize_bounds(r, n, rep_len)
            if ran is not None: updated_ranges.append(ran)
            else: print(( r, n, rep_len), 'is none'),

    return updated_ranges

def find_invalid(ranges):
    inval = []
    for r in ranges:
        if r is None: continue
        l, u, repeats= r
        count = int(u) - int(l) + 1

        for i in range(count):
            value = str(int(l) + i)* repeats
            inval.append(int(value))
    return set(inval)



def main():
    r = sol1.read_file(filename)
    r = split_ranges_by_len(r)
    print('Afer splitting :',  r); print()
    r = process_ranges(r)
    print('After processing:  ', r); print()

    ans = find_invalid(r)
    print('Invalid set: ', find_invalid(r)); print()
    return sum(ans)



if __name__ == '__main__':
    print(main())