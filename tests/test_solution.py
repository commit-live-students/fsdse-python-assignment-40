from unittest import TestCase


class TestSolution(TestCase):
    def test_solution(self):
        from build import solution

        fpath = './files/lines.txt'
        n = 3
        res = solution(fpath, n)

        self.assertEqual(res[0], 'This is line one.')
        self.assertEqual(res[1], 'This is line two.')
        self.assertEqual(len(res), 3)
        self.assertIsInstance(res, list)
