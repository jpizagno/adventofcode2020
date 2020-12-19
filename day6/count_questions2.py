
def main():
    with open('input.txt') as f:
        lines_raw = f.readlines()

        people_in_group = 0
        letter_count_in_group = {}   #key='a' value=2  a answered 2 x
        sum_matches_per_group = []
        ######
        # count times when number_in_group = letter_count.  i.e. 2 people with 2'a's  then 2
        ######
        for line in lines_raw:
            if line =='\n':
                # count matches
                total_group = 0
                for char,count in letter_count_in_group.items():
                    if count==people_in_group:
                        total_group += 1
                sum_matches_per_group.append(total_group)
                people_in_group = 0
                letter_count_in_group = {}
            else:
                line = line.replace('\n','')
                people_in_group += 1
                for char in line:
                    if char in letter_count_in_group.keys():
                        letter_count_in_group[char] += 1
                    else:
                        letter_count_in_group[char] = 1

        # count matches, one last time
        total_group = 0
        for char,count in letter_count_in_group.items():
            if count==people_in_group:
                total_group += 1
        sum_matches_per_group.append(total_group)

        print(sum_matches_per_group)
        print(sum(sum_matches_per_group))

if __name__ == "__main__":
    main()