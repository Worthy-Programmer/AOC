# https://adventofcode.com/2025/day/1

point = 50
num = 0

def read_file(file_path):
    with open(file_path) as fh:
        lines = fh.readlines()
        return lines
    
def rotate(line):
    global point
    dir, mag = line[0], int(line[1::])

    if dir == 'R':
        point += mag
    else:
        point -= mag
    
    point %= 100

    assert 0 <= point < 100


def main():
    global num
    lines = read_file( './2025/day1/input')

    for l in lines:
        rotate(l)
        print(point)
        if point == 0: num += 1
    
    print(num)

main()