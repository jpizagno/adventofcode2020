

def _get_element_code(code: str, rows:[int]):
    """code=FBFBBFFRLR and range=[0,1,2,3,4,5,...,127]"""
    if len(rows)==1:
        return rows[0]
    else:
        if code[0]=='F' or code[0]=='L':
            # get front
            return _get_element_code(code[1:], rows[:len(rows)//2])
        else:
            # ForB='B'
            return _get_element_code(code[1:], rows[len(rows)//2:])


def main():
    with open('input.txt') as f:
        lines_raw = f.readlines()
        id_max = -1

        # get all seats
        id_dict = {}
        #for row in range(0, 128):
        #    for aisle in range(0, 8):
        #        id = row*8 + aisle
        #        id_dict[id] = 0

        for line in lines_raw:
            line = line.replace('\n','')
            rows = [i for i in range(128)]
            aisles = [i for i in range(8)]

            row = _get_element_code(line[:7], rows)
            aisle = _get_element_code(line[7:], aisles)

            print("row: " + str(row))
            print("aisle: " + str(aisle))

            id = row*8 + aisle
            id_dict[id] = 1  # set in dict
            print("id: "+str(id))
            if id > id_max:
                id_max = id

        for row in range(1, 127):
            for aisle in range(0, 8):
                id = row*8 + aisle

                # is id-1 and id+1 open
                if id-1 in id_dict.keys() and id+1 in id_dict.keys() and id not in id_dict.keys():
                    if id_dict[id-1]==1 and id_dict[id+1]==1 :
                        print("your empty seat:  row: "+str(row) + " col: "+str(aisle)+ " id: "+str(row*8 + aisle))



        return id_max


if __name__ == "__main__":
    print("id_max:  " + str(main()))