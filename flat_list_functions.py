import unittest


def flat_list_while(sequence):
    """Makes list flat using 'while' statement."""
    try:
        ind = 0
        while True:
            while isinstance(sequence[ind], list):
                sequence[ind:ind + 1] = list(sequence[ind])
            ind += 1
    except IndexError:
        pass
    return sequence


def flat_list_recursion(sequence):
    """Makes list flat using recursion."""
    result = []
    for item in sequence:
        if isinstance(item, list):
            result.extend(flat_list_recursion(item))
        else:
            result.append(item)
    return result


class TestFlatListFunctions(unittest.TestCase):

    def setUp(self):
        self.list = [1, 2, 5, [1, 7], 5, [4, [8, 12, 65], 5, [3]], 0]
        self.expected_result = [1, 2, 5, 1, 7, 5, 4, 8, 12, 65, 5, 3, 0]

    def test_flat_list_while(self):
        function_result = flat_list_while(self.list)
        self.assertEqual(function_result, self.expected_result)

    def test_flat_list_recursion(self):
        function_result = flat_list_recursion(self.list)
        self.assertEqual(function_result, self.expected_result)

if __name__ == '__main__':
    unittest.main()
