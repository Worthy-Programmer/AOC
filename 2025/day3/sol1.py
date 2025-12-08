filename = './2025/day3/input'

banks = []

def read_file(filename):
    global banks
    with open(filename) as fh:
       banks = fh.read().split('\n')
    return banks

def find_max_jolts(bank):
    if len(bank) == 0: return 0
    n1 = max(bank)
    maxi  = bank.find(n1)

    rslice = bank[maxi + 1:]
    if rslice:
        n2 = max(rslice)
    else:
        n1, n2 = max(bank[:maxi]), n1

    return int(n1 + n2)


def main():
    read_file(filename)
    print(banks)

    max_jolts = list(map(find_max_jolts, banks))
    return max_jolts, sum(max_jolts)



if __name__ == '__main__':
    print(main())