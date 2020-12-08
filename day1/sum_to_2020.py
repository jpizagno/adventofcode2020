

def main():
    """
        This is the single pass solution.  as one goes through the file, cache the value necessary to sum to
        2020.  this way when one ecounters it, we can stop.
    :return: nada
    """
    cached_values_2020 = {}  # value=seen_value key=value_sum_to_2020  example key=1721 value=299

    with open('input.txt') as f:
        line = f.readline()
        while line:
            seen_value = int(line)
            if seen_value in cached_values_2020.keys():
                # found a hit exiting
                print("success:  "+str(seen_value)+"x"+str(cached_values_2020[seen_value]) + "="+str(cached_values_2020[seen_value]*seen_value))
                return
            else:
                # not a key so create one
                key_new = 2020 - seen_value
                cached_values_2020[key_new] = seen_value
                line = f.readline()


if __name__ == "__main__":
    # execute only if run as a script
    main()