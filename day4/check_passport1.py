def main():
    with open('input.txt') as f:
        lines_raw = f.readlines()
        newpass_port = ''
        passports = []
        for line in lines_raw:
            if line == '\n':
                # just add to list.  must be checked at the end
                passports.append(newpass_port)

                # reset newpass_port
                newpass_port = ''
            else:
                newpass_port = newpass_port + line
        # add last one:
        passports.append(newpass_port)

        fields_no_cid = ['byr' ,'iyr' ,'eyr' ,'hgt' ,'hcl' ,'ecl' ,'pid'  ]
        num_valid_passports = 0
        for passport in passports:
            if all(passport.count(field) for field in fields_no_cid):
                num_valid_passports += 1

        print("answer:  "+str(num_valid_passports))



if __name__ == "__main__":
    main()