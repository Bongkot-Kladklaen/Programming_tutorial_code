list1 = [5,1.2,'hello']

# iterators = iter(list1)
# print(next(iterators))
# print(next(iterators))
# print(next(iterators))


def print_each(iterable):
    iterator = iter(iterable)
    while True:
        try:
            item = next(iterator)
        except StopIteration:
            break
        else:
            print(item)

print_each(list1)