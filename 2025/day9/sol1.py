import AM as amf
from pprint import pp

vertices = []
AM = []

def find_biggest():
    Mx = -1
    for i in range(len(vertices)):
        for j in range(i+1, len(vertices)):
            Mx = max(Mx, AM[i][j])

    return Mx

def main():
    global vertices, AM
    vertices, AM = amf.readAM(amf.AM_filename)
    print('Biggest = ', find_biggest())


if __name__ == '__main__':
    main()