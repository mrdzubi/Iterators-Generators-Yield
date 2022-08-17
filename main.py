from list import nested_list

class FlatIterator:
    def __init__(self,any_list):
        self.any_list = any_list

    def __iter__(self):
        self.iter_list = iter(self.any_list)
        self.list = []
        self.coursor = -1
        return self

    def __next__(self):
        self.coursor += 1
        if len(self.list) == self.coursor:
            self.list = None
            self.coursor = 0
            while not self.list:
                self.list = next(self.iter_list)
        return self.list[self.coursor]

def flat_generator(list):
    for iterlist in list:
        for item in iterlist:
            yield item


if __name__ == '__main__':


    for item in FlatIterator(nested_list):
        print(item)
    print('________________________________________')
    for item in flat_generator(nested_list):
        print(item)
    print('________________________________________')
    flat_list = [item for item in FlatIterator(nested_list)]
    print(flat_list)
