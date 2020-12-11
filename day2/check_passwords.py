

def main():

    with open('input.txt') as f:
        valid_passwords = 0

        line = f.readline()
        while line:
            # 1-3 a: abcde
            items = line.split(' ')
            min = int(items[0].split('-')[0])
            max = int(items[0].split('-')[1])
            letter = items[1].replace(':','')
            password = items[2]
            if min <= password.count(letter) <= max:
                valid_passwords += 1
            line = f.readline()

        print("valid_passwords="+str(valid_passwords))
        return


if __name__ == "__main__":
    # execute only if run as a script
    main()