
def main():
    with open('input.txt') as f:
        lines_raw = f.readlines()

        group_num_questions = []
        group_questions = {}
        for line in lines_raw:
            if line=='\n':
                group_num_questions.append(len(group_questions.keys()))
                group_questions = {}
            else:
                line = line.replace('\n','')
                for char in line:
                    group_questions[char] = 1
        group_num_questions.append(len(group_questions.keys()))
        print(group_num_questions)
        print("" + str(sum(group_num_questions)))

if __name__ == "__main__":
    main()