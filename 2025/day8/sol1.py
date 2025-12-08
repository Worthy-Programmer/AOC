'''
Docstring for 2025.day8.sol1


BETTER METHOD: O(n^2logn)
Find the Distance among all vertices => O(n^2)
Use Kruskal algorithm => O((m+n)logn) => O(n^2logn)


BELOW METHOD:  1000 * O(nlogn) = n * O(logn)  = O(n^2 logn)
FROM PDSA: Divide and Conquer https://pdsaiitm.github.io/
def ClosestPair(Px,Py):
    if len(Px) <= 3:
        compute pairwise distances
        return closest pair and distance
    Construct (Qx,Qy), (Rx,Ry)
    (q1,q2,dQ) = ClosestPair(Qx,Qy)
    (r1,r2,dR) = ClosestPair(Rx,Ry)
    Construct Sy from Qy,Ry
    Scan Sy, find (s1,s2,dS)
    return (q1,q2,dQ), (r1,r2,QR), (s1,s2,dS)
    #depending on which of dQ, dR, dS is minimum

I will combine it with union find to combine minimum pairs  
'''

from union_find import UnionFind
import closest_pair as cp
import pprint


filename = './2025/day8/input'
NUM = 1000 # It's a failure because NUM = n (no. of vertices). So its is n*O(nlogn)


def read_file(filename):
    with open(filename) as fh:
        lines = fh.readlines()
        vertices = []
        for l in lines:
            vertices.append(tuple(map(int, l.split(','))))

        index_map = {}
        for i in range(len(vertices)):
            index_map[vertices[i]] = i


        return tuple(vertices), index_map


    
def find_pair_and_union(vertices, index_map, uf):
    v1, v2 = cp.find_closest_pair(vertices, 3)
    # print(i+1, '. Joining', v2, v1, index_map[v1], index_map[v2])
    if v1 == v2: 
        print('v1, v2 = ', v1, v2)
        print('Components', uf.components, uf.members, uf.size)
        raise AssertionError()

def find_pair(vertices, index_map):
    uf = UnionFind()
    uf.make(list(index_map.values()))


    for i in range(NUM):
        find_pair_and_union(vertices, index_map, uf)

        # try:
        #     uf.union(index_map[v1], index_map[v2])
        # except OverflowError:
        #     uf = uf.create_higher_uf(uf.components)
        #     uf.union(index_map[v1], index_map[v2])


    sorted_comp = sorted(uf.size.values(), reverse=True)

    # extra = sum(sorted_comp) - len(sorted_comp)
    # sorted_comp[0] -= extra

    v = 1
    for i in range(3):
        v *= sorted_comp[i]


    # print(sorted_comp)

    # print(sorted_comp)
    return v
    
def main():
    vertices, index_map = read_file(filename)
    return find_pair(vertices, index_map)

if __name__ == '__main__':
    print(main())






