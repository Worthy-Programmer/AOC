filename = './2025/day7/ex1'

splitters = {0: set([])} # dict of sets
tachyon_positions = [] # list
m_height = 0  # Map dimensions
m_width = 0

def read_file(filename):
    global splitters, tachyon_positions, m_height, m_width

    with open(filename) as fh:
        l = fh.readlines()
        find_splitters(l)

        for i in l: tachyon_positions.append(set())
        tachyon_positions[0].add(l[0].find('S'))

        m_height = len(l)
        m_width = len(l[0].strip())


def find_splitters(linelist):
    global splitters
    for i in range(1, len(linelist)):
        line = linelist[i]
        splitters[i] = set()

        for j in range(len(line)):
            if line[j] == '^':
                splitters[i].add(j)
    # print(splitters)

def split(row):
    global tachyon_positions
    prev_pos = tachyon_positions[row-1]
    
    split_hits = prev_pos.intersection(splitters[row])
    passthrough = prev_pos.difference(split_hits)


    splits = set()

    for i in split_hits:
        splits.add(i+1)
        splits.add(i-1)

    unique_splits  = splits.difference(passthrough)

    tachyon_positions[row] = splits.union(passthrough)

    return unique_splits, split_hits

def print_map():
    global splitters, tachyon_positions, m_height, m_width

    for i in range(m_height):
        for j in range(m_width):
            if j in splitters[i]: print('^', end='')
            elif j in tachyon_positions[i]: print('|', end='')
            else: print('.', end='')
        print()

    print()

def main():
    read_file(filename)
    split_sum = 0
    for i in range(1, m_height):
        unique_splits, split_hits = split(i)
        split_sum += len(split_hits)
        # print(unique_splits)
        # print_map()
        # print()

    return split_sum

if __name__ == '__main__':
    print ('Result =', main() )