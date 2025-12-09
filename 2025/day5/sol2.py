import sol1
from pprint import pp

sol1.filename = './2025/day5/input'

# def exclusive_bounds(ranges): # Assuming, ranges are sorted
#     for i in range(1, len(ranges)):
#         # curr_min, prev_max = ranges[i][0], ranges[i-1][1]
#         if ranges[i][0] <= ranges[i-1][1]:
#             ranges[i] = ( ranges[i-1][1] + 1, ranges[i][1] )
    
def no_of_fresh_ids(ranges): # Assuming, ranges are sorted 
    # THis is WRONG!!
    # Ex: (1, 4), (3, 2) => 
    n = 0
    prev_Mx = -1
    for mx, Mx in ranges:
        if prev_Mx >= mx:
            mx = prev_Mx + 1

        if mx <= Mx:
            n += Mx - mx + 1

        # prev_Mx = Mx This is wrong!! (1,5) (2,4) => prev_Mx should be max(5,4)
        prev_Mx = max(prev_Mx, Mx)


    return n

# AI generated: below Using merges
# def no_of_fresh_ids(ranges):
#     # expects ranges sorted by start
#     if not ranges:
#         return 0

#     n = 0
#     cur_start, cur_end = ranges[0]

#     for mx, Mx in ranges[1:]:
#         if mx <= cur_end + 1:          # overlapping or contiguous
#             cur_end = max(cur_end, Mx)
#         else:
#             n += cur_end - cur_start + 1
#             cur_start, cur_end = mx, Mx

#     n += cur_end - cur_start + 1
#     return n

def main():
    sol1.read_file()
    sol1.fresh_ranges.sort()
    # exclusive_bounds(sol1.fresh_ranges)

    # print('After exclusive bounds: ')
    pp(sol1.fresh_ranges)
    print(no_of_fresh_ids(sol1.fresh_ranges))

if __name__ == '__main__':
    main()
