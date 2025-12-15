input_filename = './2025/day9/input'
AM_filename = './2025/day9/input.bin'
import pprint
import pickle

vertices = []

def read_file():
    global vertices

    with open(input_filename) as fh:
        for l in fh:
            l = l.strip()
            if not l: continue
            
            v = tuple(map(int, l.split(',')))
            vertices.append(v)


def find_area(v1, v2):
    l = abs(v1[0] - v2[0]) + 1 if abs(v1[0] - v2[0]) != 0 else 0
    h = abs(v1[1] - v2[1]) + 1 if abs(v1[1] - v2[1]) != 0 else 0
    return l * h

def generate_matrix(vertices):
    # Adjecency Matrix
    AM = [[find_area(vertices[i], vertices[j]) for j in range(len(vertices))] for i in range(len(vertices))]
    return AM

def storeAM(filename, AM):
    with open(filename, 'wb') as fh:
        pickle.dump(AM, fh)

def readAM(filename):
    with open(filename, 'rb') as fh:
        return pickle.load(fh)

def main():
    read_file()
    AM = generate_matrix(vertices)
    storeAM(AM_filename, [vertices, AM])

    # pprint.pp(AM)

if __name__ == '__main__':
    main()