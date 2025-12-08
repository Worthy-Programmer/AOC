'''
Docstring for 2025.day8.UnionFind
MakeUnionFind(S) — O(n)
Find(i) — O(1)
Union(i,j) —  O(logn)


Refer
https://pdsaiitm.github.io/
Week6

'''
# import pprint
class UnionFind:
    def __init__(self):
        self.components = {}
        self.lower_components = {}
        self.members = {}
        self.size = {}

    def make(self, vertices):
        for v in vertices:
            self.components[v] = v
            self.members[v] = [v]
            self.size[v] = 1

    # def make(self, vertices, lower_components = None):
    #     # print(vertices, lower_components)
    #     for v in vertices:
    #         self.components[v] = v
    #         self.members[v] = [v]
    #         self.size[v] = 1

    #     self.lower_components = self.components.copy() if lower_components is None else lower_components.copy() # Didn't use this anyway
    def find(self, vertex):
        return self.components[vertex]
    
    def union(self, v1, v2):
        c_old = self.find(v1); c_new = self.find(v2)
        if c_old == c_new: return ##### Forgot to write this line and found it only after spending 8 hours on this

        if self.size[c_old] > self.size[c_new]:
            c_old, c_new = c_new, c_old


        if not self.size[c_old] > 0:
            #pprint.pp([self.size, self.members])
            assert False


        for v in self.members[c_old]:
            self.components[v] = c_new

        # if len(self.members[c_old]) > 2:
        #     raise OverflowError
        
        self.members[c_new].extend(self.members[c_old])
            
        self.size[c_new] += self.size[c_old]
        self.size[c_old] = 0

        #pprint.pp([self.size, self.members])



    # # Didn't use the below one
    # def create_higher_uf(self):
    #     valid_unions = filter(lambda x: x[1] != 0, self.size.items())
    #     new_components =  list(map(lambda x: x[0], valid_unions))

    #     uf = UnionFind()
    #     uf.make(new_components, self.components)
    #     uf.get_size_from_components()

    #     return uf

    # def get_size_from_components(self):
    #     self.size = {}
    #     for component in self.components.values():
    #         if component in self.size:
    #             self.size[component] += 1
    #         else: self.size[component] = 1
