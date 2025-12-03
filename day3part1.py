def total_joltage(filepath):
    n = 2
    counter = 0
    with open(filepath,'r') as file:
        for line in file:
            line = line.rstrip()
            if line:
                bank_joltage = ''
                for i in range(n,0,-1):
                    j = len(line)-(i-1)
                    ind = line.index(max(line[:j]))
                    bank_joltage += str(line[ind])
                    line = line[ind+1:]
                counter += int(bank_joltage)
    return counter

if __name__ == "__main__":
    filepath = 'inputs/day3.txt'
    print(total_joltage(filepath))