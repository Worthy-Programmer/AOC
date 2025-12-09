filename = './2025/day5/input'

fresh_ranges = []
ids = []

def read_file():
    global fresh_ranges
    with open(filename) as fh:
        lines = [l.rstrip('\n') for l in fh]

        # print(lines)
        i = 0
        while i < len(lines) and lines[i].strip():            
            mx, Mx = l.split('-')
            fresh_ranges.append((int(mx), int(Mx)))
            i+= 1
        

        for l in lines[i+1:]:
            l = l.strip()
            if not l: break
            ids.append(int(l))
        
        fresh_ranges.sort()

# def binary_search(id, l, lower, upper):
#     if lower == upper: return lower


#     mid = (lower + upper) //2

#     if id < l[mid]:
#         return binary_search(id, l, lower, mid-1)
#     elif id > l[mid]:
#         return binary_search(id, l, mid, upper)
#     else:
#         return mid
    
def is_fresh(id):
    # min_index = binary_search(id, lmin,0, len(lmin)- 1)
    # print(fresh_ranges[min_index])
    # mx, Mx = fresh_ranges[min_index]
    # return id <= Mx
    # print(list(map(lambda x: x[0] <= id <= x[1], fresh_ranges)))
    return any(map(lambda x: x[0] <= id <= x[1], fresh_ranges))

    

def main():
    read_file()
    # lmin = list(map(lambda x : x[0], fresh_ranges))
    # print(fresh_ranges)
    print(len(list(filter(is_fresh, ids))))

if __name__ == '__main__':
    main()


    

