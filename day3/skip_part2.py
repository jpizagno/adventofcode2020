
def steps(i_step, j_step):
    with open('input.txt') as f:
        lines_raw = f.readlines()
        lines = [line.replace('\n','') for line in lines_raw]
        i = 0
        j = 0
        num_trees = 0
        while j<len(lines)-1:
            i = i + i_step
            j = j + j_step
            if i >= len(lines[0]):
                i = i - len(lines[0])
            curr_place = lines[j][i]
            if curr_place == '#':
                num_trees += 1
    return num_trees


if __name__ == "__main__":
    factor = 1
    #Right 1, down 1.
    print(steps(1,1))
    factor = factor * steps(1,1)
    #Right 3, down 1. (This is the slope you already checked.)
    factor = factor * steps(3,1)
    print(steps(3,1))
    #Right 5, down 1.
    factor = factor * steps(5,1)
    print(steps(5,1))
    #Right 7, down 1.
    factor = factor * steps(7,1)
    print(steps(7,1))
    #Right 1, down 2.
    factor = factor * steps(1,2)
    print(steps(1,2))
    print(factor)

