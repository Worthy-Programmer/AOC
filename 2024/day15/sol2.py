# https://adventofcode.com/2024/day/15

walls = []
boxes_l = []

robot_x = 0
robot_y = 0
directions = ''

gps_coord_sum = 0


def get_input(filepath):
    global robot_x, robot_y, directions

    with open(filepath) as fh:
        y = 0
        line = fh.readline()


        while line != '\n':
            walls.append([])
            boxes_l.append([])
            x = 0
            for i in line:
                if i == '#':
                    walls[y].append(x)
                    walls[y].append(x+1)
                elif i == 'O':
                    boxes_l[y].append(x)
                elif i == '@':
                    robot_x, robot_y = x, y

                x +=2
            line = fh.readline()
            y += 1

        directions = fh.read()


def get_mov_dir(dir):

    assert dir in '><^v'
    move_dir = (0, 0)
    if dir == '>':
        move_dir = (1, 0)
    elif dir == '<':
        move_dir = (-1, 0)
    elif dir == '^':
        move_dir = (0, -1)
    elif dir == 'v':
        move_dir = (0, 1)

    return move_dir

def move(current_pos, move_dir, ignore_pos=(-1,-1)):
    old_x, old_y = current_pos
    delx , dely = move_dir
    
    x, y = (old_x+delx,old_y+dely)

    if x in walls[y]:
        return current_pos
    elif x in boxes_l[y] or x - 1 in boxes_l[y]:
        
        xl = x
        if x - 1 in boxes_l[y]: xl = x-1

        boxes_l[y].remove(xl)

        box_dir_l = move((xl,y),  move_dir)
        box_dir_r = move((xl+1, y), move_dir)

    
        if  box_dir_l == (xl,y)  or  box_dir_r == (xl+1, y): 
            boxes_l[y].append(xl)
            return current_pos
        
        boxes_l[box_dir_l[1]].append(box_dir_l[0])
        
    
    return (x,y)


def print_map():
    for y in range(len(walls)):
        x = 0
        while x  < len(walls[0]):
            if (x,y) == (robot_x, robot_y):
                print('@', end='')
                x +=1
            elif x in walls[y]:
                print('##', end='')
                x+=2
            elif x in boxes_l[y]:
                print('[]', end='')
                x+=2
            else: 
                print('.', end='')
                x+=1 
        print()

    print(); print()


def sum_of_boxes_coord():
    s = 0
    for y in range(len(boxes_l)):
        for x in boxes_l[y]:
            s += 100 * y + x

    return s

def main():
    global robot_x, robot_y, gps_coord_sum
    get_input('./2024/day15/ex1')
    # print_map()

    for dir in directions:

        if dir in '^><v':
            new_pos = move((robot_x, robot_y), get_mov_dir(dir))
            
            robot_x, robot_y = new_pos

            print(robot_x, robot_y, dir)
            print_map()


    print('Sum of all boxes\' GPS coordinates = ' , sum_of_boxes_coord())

main()
            


