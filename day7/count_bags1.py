
class Bag:
    def __init__(self, line):
        if line.count('contain no other bags.') > 0:
            # line = 'faded blue bags contain no other bags.'
            self.bag_name = line.split('bags')[0].strip() # 'faded blue'
            self.bags = {}
        else:
            # "shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags."
            # set attrs
            line = line.replace('bags','bag').lower() # "shiny gold bag contain 1 dark olive bag, 2 vibrant plum bag."
            line = line.replace('.','') # "shiny gold bag contain 1 dark olive bag, 2 vibrant plum bag"
            line = line.replace(',','') # "shiny gold bag contain 1 dark olive bag 2 vibrant plum bag"
            line = line.replace('contain','') # "shiny gold bag  1 dark olive bag 2 vibrant plum bag"
            bags_tmp = line.split('bag') # ['shiny gold',' 1 dark olive', ' 2 vibrant plum ']
            # want dict with key:bag value: number_of_bag_type
            bags_tmp2 = [bag_iter.strip() for bag_iter in bags_tmp] # ['shiny gold','1 dark olive', '2 vibrant plum']
            bags_tmp2.remove('')
            self.bag_name = bags_tmp2[0]  # 'shiny gold'
            self.bags = {}
            for bag_iter in bags_tmp2[1:]:  # ['1 dark olive', '2 vibrant plum']
                number = bag_iter.split(' ')[0]
                name = bag_iter.replace(number,'').strip()  #  'dark olive'  or 'vibrant plum'
                self.bags[name] = int(number)

    def __lt__(self, other):
        """ this will allow us to sort the bags, via sorted()"""
        # get if another
        if other.bag_name == self.bag_name:
            return False
        else:
            if other.bag_name in self.bags.keys():
                # this means self contains other, and therefore other is smaller than self
                return True
            elif self.bag_name in other.bags.keys():
                return False
            else:
                for bag_other in other.bags.keys():
                    if bag_other in self.bags.keys():
                        if self.bags[bag_other] < other.bags[bag_other]:  # compare number of bags
                            return False
                        else:
                            return True
                print("what")
                return False


def main():
    with open('input.txt') as f:
        lines_raw = f.readlines()

        my_bag = Bag("shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.")
        bags = []
        for line in lines_raw:
            bags.append(Bag(line))

        # sorted largest to smallest
        bags_sorted = sorted(bags)
        number_bags = 0
        for bag_iter in bags_sorted:
            if bag_iter.bag_name == 'shiny gold':
                break
            else:
                number_bags += 1
        print(number_bags)


if __name__ == "__main__":
    main()