import sol1

sol1.filename = './2025/day7/input'
sol1.main()

dp_map = [ [ 0 for j in range(sol1.m_width)] for i in range(sol1.m_height)]

# Using dynamic programming, when there is a splitter a[i,j] = a[i+1, j+1] + a[i+1, j-1] where is i is the rows, j is columns

def main():
    global dp_map


    for i in sol1.tachyon_positions[-1]: # Boundary conditions, no. of paths for the bottom paths are 1
        dp_map[-1][i] = 1

    for i in range(sol1.m_height - 2, -1, -1):
        for j in sol1.tachyon_positions[i]:
            if j in sol1.splitters[i+1]: # If I splitter is below it,
                dp_map[i][j] = dp_map[i+1][j+1] + dp_map[i+1][j-1]
            else: # If It is just pass through
                dp_map[i][j] = dp_map[i+1] [j]

    s_pos  = list(sol1.tachyon_positions[0])[0]
    return dp_map[0][s_pos]

if __name__ == '__main__':
    print('Result = ', main())