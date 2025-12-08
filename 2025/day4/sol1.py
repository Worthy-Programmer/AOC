
max_coord = ()
paper_pos = {}
neighbours = {}

filename  = './2025/day4/input'

def read_file(filename):
    with open(filename) as fh:
        lines = fh.readlines()

        paper_pos = {}
        max_coords = (len(lines[0].strip()), len(lines))

        for y in range(len(lines)):
            l = lines[y].strip()
            if not l: continue

            paper_pos_y = []
            for x in range(len(l)):
                if l[x] == '@':
                    paper_pos_y.append(x)

            paper_pos[y] = paper_pos_y

        return paper_pos, max_coords
        

def find_neighbour_rolls(coord):
    x,y = coord
    
    n = 0
    for xi in range(max(x-1, 0), min(x+2, max_coord[0])): 
        for yi in range(max(y-1, 0), min(y+2, max_coord[1])):
            if xi == x and yi == y: continue
            if xi in paper_pos[yi]:
                n+=1

    return n

def print_map(paper_pos, max_coord, pick_pos):
    for y in range(max_coord[1]):
        for x in range(max_coord[0]):
            if (x, y) in pick_pos: print(pick_pos[(x,y)], end='')
            elif x in paper_pos[y]: print('@', end='')
            else : print('.', end = '')

        print()
    print()

def find_all_neighbours():
    global max_coord, paper_pos, neighbours

    # print(paper_pos, max_coord)

    neighbours = {}

    for x in range(max_coord[0]):
        for y in range(max_coord[1]):
            if x in paper_pos[y]:
                neighbours[(x,y)] = find_neighbour_rolls((x,y))

    return neighbours

def main():
    global max_coord, paper_pos, neighbours

    paper_pos, max_coord = read_file(filename)
    neighbours = find_all_neighbours()

    return len(list(filter(lambda n: n < 4, neighbours.values())))

if __name__ == '__main__':
    print(main())
    print_map(paper_pos, max_coord, neighbours)







            
