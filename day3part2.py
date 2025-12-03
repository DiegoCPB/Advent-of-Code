def total_joltage(filepath):
    n = 12
    counter = 0
    with open(filepath,'r') as file:
        for line in file:
            line = line.rstrip()
            if line:
                bank = [int(s) for s in line]
                bank_joltage = ''
                for i in range(n,0,-1):
                    j = len(bank)-(i-1)
                    ind = bank.index(max(bank[:j]))
                    bank_joltage += str(bank[ind])
                    bank = bank[ind+1:]
                counter += int(bank_joltage)
    return counter

if __name__ == "__main__":
    filepath ='inputs/day3.txt'
    print(total_joltage(filepath))