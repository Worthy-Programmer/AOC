import sol1 

filename = './2025/day4/input'

def neighbour_to_paper_pos(neighbour):
    paper_pos = {i:[] for i in range(sol1.max_coord[1])}

    for (x,y) in neighbour:
        paper_pos[y].append(x)

    return paper_pos


def main():
    sol1.paper_pos, sol1.max_coord = sol1.read_file(filename)
    n = 0

    while True:
        sol1.neighbours = sol1.find_all_neighbours()
        # sol1.print_map(sol1.paper_pos, sol1.max_coord, sol1.neighbours)
        prev_n = len(sol1.neighbours)

        new_neighbours = dict(filter(lambda n: n[1] >= 4, sol1.neighbours.items()))
        new_n = len(new_neighbours)

        delta = prev_n - new_n
        if delta == 0: break

        n+= delta
        sol1.paper_pos = neighbour_to_paper_pos(new_neighbours)
        # print()
    
    return n

print(main())