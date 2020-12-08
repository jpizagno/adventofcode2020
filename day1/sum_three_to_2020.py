

def main():
    """
        sort the array, and search for pairs (i,l) where i,l < r. when i+l+r=2020, then print(i*l*r) and exit
    :return: nada
    """
    cached_values_2020 = {}  # value=seen_value key=value_sum_to_2020  example key=1721 value=299

    with open('input.txt') as f:
        lines = f.readlines()
        lines = [int(x) for x in lines]
        lines.sort()
        for i in range(0, len(lines)-2):
            l = i + 1
            r = len(lines)-1
            while (l < r):
                if( lines[i] + lines[l] + lines[r] == 2020):
                    print("Triplet is", lines[i],', ', lines[l], ', ', lines[r])
                    print("multiplication:  " + str(lines[i] * lines[l] * lines[r]))
                    return True
                elif (lines[i] + lines[l] + lines[r] < 2020):
                    l += 1
                else:
                    # A[i] + A[l] + A[r] > sum
                    r -= 1
            print("no matching triplets found")


if __name__ == "__main__":
    # execute only if run as a script
    main()