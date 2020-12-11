

def main():

    with open('input.txt') as f:
        valid_passwords = 0

        line = f.readline()
        while line:
            # 1-3 a: abcde
            items = line.split(' ')
            pos1 = int(items[0].split('-')[0])-1
            pos2 = int(items[0].split('-')[1])-1
            letter = items[1].replace(':','')
            password = items[2]
            if not (password[pos1]==letter and password[pos2]==letter) and (password[pos1]==letter or password[pos2]==letter):
                valid_passwords += 1
            line = f.readline()

        print("valid_passwords="+str(valid_passwords))
        return


if __name__ == "__main__":
    # execute only if run as a script
    main()