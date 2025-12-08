# Using DP
# f(i, n) returns a string which is maximum jolts
# i => index in which it is checking
# n => How many numbers already chosen
# f(i, n) = max ( ai + f (i+1, n+1 ), f (i+1 ,n )) => returns '' if it is 0
# Boundary conditions: 
#   1.  n=10 => f = ''
#   2. i = (last index) => f='' except n = 9 (only one number is left)  where f = a14

from sol1 import banks, read_file
import sol1
filename = './2025/day3/input'

width = 0
digits = 12

DP = []

def setupDP(bank):
    DP = [['' for j in range(digits + 1)] for i in range(width)]
    DP[width-1][digits-1] = bank[-1] # n = (only one number is left)  where f = last digit
    return DP

def find_max_jolts(bank):

    if not bank: return 0

    DP = setupDP(bank)
    for i in range(width-2, -1, -1):
        for j in range(max(digits-width+i, 0), digits): # digits - j <= width - i; No of digits to be chosen <= No. of digits left
            DP[i][j] = max(bank[i] + DP[i+1][j+1], DP[i+1][j])
    return int(DP[0][0])
    
def main():
    global width, banks
    banks = read_file(filename)
    width = len(banks[0])

    max_jolts = list(map(find_max_jolts, banks))
    return sum(max_jolts)


if __name__ == '__main__':
    print(main())