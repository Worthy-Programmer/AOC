import AM as amf
import sys

allowed_tiles_y = {}
allowed_tiles_x = {}

vertices = []
AM = []
vertex_dict_y = {}
vertex_dict_x = {}

def main():
    global vertices, AM
    vertices, AM = amf.readAM('./2025/day9/ex1.bin')

    create_vertex_dict()
    create_boundary()
    gen_allowed_tiles_x()

    
    for i in allowed_tiles_x.keys():
        allowed_tiles_x[i] = merge_list(list(allowed_tiles_x[i]))

    for i in allowed_tiles_y.keys():
        allowed_tiles_y[i] = merge_list(list(allowed_tiles_y[i]))
    # fill_inside()


    # print('Vertex [y] = [...x] = ', vertex_dict_y)
    # print('Allowed Tiles = ', allowed_tiles)

    print_map(open('./2025/day9/ex1_map', 'w'))
    # print(allowed_tiles_x)
    print('Max Area = ', find_max_area())

def create_vertex_dict():
    global vertices, vertex_dict_y, vertex_dict_x
    for v in vertices:
        x, y = v
        if y in vertex_dict_y:
            vertex_dict_y[y].append(x)
        else:
            vertex_dict_y[y] = [x]

        if x in vertex_dict_x:
            vertex_dict_x[x].append(y)
        else:
            vertex_dict_x[x] = [y]

    for i in vertex_dict_x.keys():
        vertex_dict_x[i] = merge_list(vertex_dict_x[i])

    for i in vertex_dict_y.keys():
        vertex_dict_y[i] = merge_list(vertex_dict_y[i])

def convention(v1, v2):
    return min((v1,v2), (v2,v1))

def print_map(file = sys.stdout):
    min_y = min(vertex_dict_y.keys())
    min_X = min(vertex_dict_x.keys())

    max_y = max(vertex_dict_y.keys())
    max_X = max(vertex_dict_x.keys())

    for y in range(min_y, max_y + 2):
        for x in range(min_X, max_X + 2):
            if y in vertex_dict_y and  x in vertex_dict_y[y]: print('#', end='' ,file=file)
            elif y in allowed_tiles_y and x in allowed_tiles_y[y]: print('x', end='', file=file)
            # elif in_range(x,y): print('u', end='', file=file)
            else: print('.', end='', file=file)

        print(file=file)
    print(file=file)
    


def gen_allowed_tiles_x():
    for y,l in allowed_tiles_y.items():
        for x in l:
            if x in allowed_tiles_x: allowed_tiles_x[x].add(y)
            else: allowed_tiles_x[x] = {y}

# AI generated: below Using merges
def merge_list(ranges):
    # expects ranges sorted by start
    ranges.sort()
    if len(ranges) <= 2:
        return ranges

    new_l = [ranges[0]]
    i = 0
    cur_end =  ranges[1]


    for i  in range(1, len(ranges)):
        mx = ranges[i]
        if mx <= cur_end + 1:          # overlapping or contiguous
            cur_end = max(cur_end, mx)
        else:
            # n += cur_end - cur_start + 1
            new_l.append(cur_end)
            try:
                cur_end = ranges[i+1]
            except IndexError:
                cur_end = mx

    new_l.append(cur_end)
    return new_l

def create_boundary():
    global vertex_dict_y, allowed_tiles_y, vertex_dict_x, allowed_tiles_x
    
    for y, l in vertex_dict_y.items():
        l = sorted(list(l))
        allowed_tiles_y[y] = set()
    # Only connect if the problem implies these specific indices connect
    # If standard even-odd rule applies (Polygon):
        for i in range(0, len(l), 2):  # Actualy I have to alternate, i put it continuous
            if i+ 1 < len(l):
                for j in range(l[i], l[i+1] +1):
                    allowed_tiles_y[y].add(j)

                # if j in allowed_tiles_x: allowed_tiles_x[j].add(y)
                # else: allowed_tiles_x[j] = {y}


    for x, l in vertex_dict_x.items():
        l = sorted(list(l))
        # allowed_tiles_x[x] = set()
        for i in range(0, len(l), 2):
            for j in range(l[i], l[i + 1] +1):
                # allowed_tiles_x[x].add(j)

                if j in allowed_tiles_y: allowed_tiles_y[j].add(x)
                else: 
                    allowed_tiles_y[j] = {x}
                    # print(allowed_tiles_y)

    


#  No need of this, I can just compare
# def fill_inside():
#     for y, l in allowed_tiles.items():
#         l = sorted(list(l))
#         new_set = set()
#         for i in range(1, len(l)):
#             for j in range(l[i-1], l[i] +1):
#                 new_set.add(j)

#         allowed_tiles[y] = new_set

    # print(allowed_tiles)

def in_range(t):
    dic,y,x1,x2 = t
    #  try:
    #     return min(allowed_tiles_y[y]) <= x <= max(allowed_tiles_y[y]) and min(allowed_tiles_x[x]) <= y <= max(allowed_tiles_x[x])
    #  except KeyError:
    #     #  print(x,y)
    #      return False 

    l = dic[y]
    yes = False
    for k in range(0, len(l), 2):
        if not k+1 < len(l): continue

        m,M = l[k], l[k+1]
        if m <= x1 <= M and m<= x2 <= M:
            yes = True
            break
    return yes

def find_max_area():
    max_area = -1
    for i in range(len(vertices)):
        for j in range(i + 1,  len(vertices)):
            x1, y1 = vertices[i]
            x2, y2 = vertices[j]

            if convention(vertices[i], vertices[j]) == ((2,3), (9,5)):
                    print(list(map(in_range, [ [allowed_tiles_y, y1, x1, x2],   [allowed_tiles_y, y2, x1, x2],  [allowed_tiles_x, x1, y1, y2], [allowed_tiles_x, x2, y1, y2]])))
                    print(x1)
                    print([allowed_tiles_y, y2, x1, x2])
            if all(map(in_range, [ [allowed_tiles_y, y1, x1, x2],   [allowed_tiles_y, y2, x1, x2],  [allowed_tiles_x, x1, y1, y2], [allowed_tiles_x, x2, y1, y2]])):
                area = (abs(x1 - x2) + 1) * ( abs(y1-y2) + 1 )
                max_area = max(max_area, area)


            
            # if in_range(x1, y2) and in_range(x2, y1):
            #     area = (abs(x1 - x2) + 1) * ( abs(y1-y2) + 1 )
            #     max_area = max(max_area, area)

    return max_area

            


main()
# print(merge_list([1,2,3,4, 5,9 , 10, 12]))


