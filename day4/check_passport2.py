import re

def main():
    with open('input.txt') as f:
        lines_raw = f.readlines()
        newpass_port = ''
        passports = []
        for line in lines_raw:
            if line == '\n':
                # just add to list.  must be checked at the end
                passports.append(newpass_port.replace('\n',' ').rstrip())

                # reset newpass_port
                newpass_port = ''
            else:
                newpass_port = newpass_port + line
        # add last one:
        passports.append(newpass_port.replace('\n',' ').rstrip())

        fields_no_cid = ['byr' ,'iyr' ,'eyr' ,'hgt' ,'hcl' ,'ecl' ,'pid'  ]
        num_valid_passports = 0
        for passport in passports:
            passport_dict = dict(x.split(":") for x in passport.split(" "))

            if not all(passport.count(field) for field in passport_dict.keys()):
                # a key is missing.. exit
                break
            else:
                #  all keys are there, but check each one....
                try:
                    if int(passport_dict['byr']) < 1920 or int(passport_dict['byr']) > 2002:
                        break
                    if int(passport_dict['iyr']) < 2010 or int(passport_dict['iyr']) > 2020:
                        break
                    if int(passport_dict['eyr']) < 2020 or int(passport_dict['eyr']) > 2030:
                        break
                    height = passport_dict['hgt']
                    if height.count('cm')>0:
                        if int(height.replace('cm','')) < 150 or int(height.replace('cm','')) > 193:
                            break
                    if height.count('in')>0:
                        if int(height.replace('in','')) < 59 or int(height.replace('in','')) > 76:
                            break
                    if passport_dict['hcl'][0] != '#' and len(passport_dict['hcl']) != 7:  # '#ceb3a1'
                        break
                    hair_color = passport_dict['hcl'].replace('#','')  # 'ceb3a1'
                    pattern = re.compile("[a-f0-9]+")  #followed by exactly six characters 0-9 or a-f.
                    if pattern.fullmatch(hair_color) is None:
                        break

                    possible_eye_colors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
                    if any(passport_dict['ecl'].count(eye_color)>0 for eye_color in possible_eye_colors):
                        pass
                    else:
                        break
                    if len(passport_dict['pid'])!=9 and int(passport_dict['pid'])>=0:  #a nine-digit number, including leading zeroes.
                        break

                    num_valid_passports += 1
                except:
                    pass

        print("answer:  "+str(num_valid_passports))



if __name__ == "__main__":
    main()