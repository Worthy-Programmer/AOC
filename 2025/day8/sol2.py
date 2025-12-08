from sol1 import read_file, find_pair_and_union
from union_find import UnionFind

filename = './2025/day8/input'

def main():
    vertices, index_map = read_file(filename)

    uf = UnionFind()
    uf.make(list(index_map.values()))

    # prev_values = ()
    i = 0
    while True:
        v1,v2 = find_pair_and_union(vertices, index_map, uf)
        max_size = max(uf.size.values())
        if max_size >= len(vertices): return v1[0] * v2[0]

        i += 1
        print(i, '. Max size = ', max_size)

if __name__ == '__main__':
    print(main())
