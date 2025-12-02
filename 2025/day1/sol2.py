# https://adventofcode.com/2025/day/1
point = 50
num = 0

def read_file(file_path):
    with open(file_path) as fh:
        lines = fh.readlines()
        return lines
    
def rotate(line):
    global point, num
    dir, mag = line[0], int(line[1::])
    prev_point = point
   
    num += mag // 100 # Full Rotations
    partial_rotation = mag % 100 # Modulo for partial rotation

    if dir == 'L': partial_rotation *= -1  # Left rotation
    point += partial_rotation 

    if not ( 0 < point < 100 ) and prev_point: num += 1 # Crossing zero check

    point %= 100

def main():
    lines = read_file( './2025/day1/input')
    for l in lines: rotate(l)
    print(num)

main()