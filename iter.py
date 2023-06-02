class FlatIterator:
    def __init__(self, nested_list):
        self.nested_list = nested_list
        self.current_list = 0
        self.current_element = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_list >= len(self.nested_list):
            raise StopIteration
        elif self.current_element >= len(self.nested_list[self.current_list]):
            self.current_list += 1
            self.current_element = 0
            return next(self)
        else:
            value = self.nested_list[self.current_list][self.current_element]
            self.current_element += 1
            return value

def test_1():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
    test_1()

#
# FlatIterator(nested_list)
# for item in FlatIterator(nested_list):
#     print(item)
# # flat_list = [item for item in FlatIterator(nested_list)]
# # print(flat_list)
#
# def flat_generator(nested_list):
#     for sublist in nested_list:
#         for item in sublist:
#             if item is not False:
#                 yield item
#
#
# for item in flat_generator(nested_list):
#     print(item)
#
# """Генератор с любым уровнем вложенности"""
# def nested_generator(nested_list):
#     for item in nested_list:
#         if isinstance(item, list):
#             yield from nested_generator(item)
#         else:
#             yield item
# for item in nested_generator(nested_list):
#     print(item)
#
#
# """итератор, который обрабатывает списки с любым уровнем вложенности"""
# class NestedIterator:
#     def __init__(self, nested_list):
#         self.stack = [iter(nested_list)]
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         while True:
#             try:
#                 item = next(self.stack[-1])
#                 if isinstance(item, list):
#                     self.stack.append(iter(item))
#                 else:
#                     return item
#             except StopIteration:
#                 self.stack.pop()
#
#                 if not self.stack:
#                     raise
#
# for item in NestedIterator(nested_list):
#     print(item)