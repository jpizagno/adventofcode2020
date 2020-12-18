
def main():
    with open('input.txt') as f:
        lines_raw = f.readlines()
        lines = [line.replace('\n','') for line in lines_raw]
        i = 0
        j = 0
        num_trees = 0
        while j<len(lines)-1:
            i = i + 3
            j = j + 1
            if i >= len(lines[0]):
                i = i - len(lines[0])
            curr_place = lines[j][i]
            if curr_place == '#':
                num_trees += 1
    print(num_trees)


if __name__ == "__main__":
    main()