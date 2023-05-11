import unittest

from logic.floor_logic import GridManager


class TestPathManager(unittest.TestCase):
    def setUp(self):
        pass

    def test_path(self):
        alku =  [['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
                ['#', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '#'],
                ['#', '=', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '=', '#'],
                ['#', '=', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '=', '#'],
                ['#', '=', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '=', '#'],
                ['#', '=', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '=', '#'],
                ['#', '=', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-','=', '#'],
                ['#', '=', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '=', '#'],
                ['#', '=', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '=', '#'],
                ['#', '=', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '=', '#'],
                ['#', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '#'],
                ['#', '=', '#', '#', 'D', '#', '#', '#', '#', '#', '#', '=', '#', '#', 'D', '#', '#', '=', '=', '#'],
                ['#', '=', '#', '.', '.', '.', '.', '.', '.', '.', '#', '=', '#', '.', '.', '.', '#', '=', '=', '#'],
                ['#', '=', 'D', '.', '.', '.', '#', '.', '.', '.', 'D', '=', 'D', '.', '.', '.','D', '=', '=', '#'],
                ['#', '=', '#', '.', '.', '.', '.', '.', '.', '.', '#', '=', '#', '.', '.', '.', '#', '=', '=', '#'],
                ['#', '=', '#', '#', '#', '#', '#', '#', 'D', '#', '#', '=', '#', '#', 'D', '#', '#', '=', '=', '#'],
                ['#', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '#'],
                ['#', '=', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '=', '#'],
                ['#', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '#'],
                ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#']]
        ovigrid = [[(14, 11), (12, 13), (16, 13), (14, 15)], [(4, 11), (2, 13), (10, 13), (8, 15)]]

        my_griddy = GridManager()

        my_griddy.my_grid = alku #my_griddy.string_room_to_array_room(alku)
        my_griddy.door_array = ovigrid

        my_griddy.generate_paths()

        self.assertEqual(my_griddy.my_grid, [['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#'], ['#', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '#'], ['#', '=', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '=', '#'], ['#', '=', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '=', '#'], ['#', '=', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '=', '#'], ['#', '=', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '=', '#'], ['#', '=', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-',
'=', '#'], ['#', '=', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '=', '#'], ['#', '=', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '=', '#'], ['#', '=', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '=', '#'], ['#', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '#'], ['#', '=', '#', '#', 'D', '#', '#', '#', '#', '#', '#', '=', '#', '#', 'D', '#', '#', '=', '=', '#'], ['#', '=', '#', '.', '.', '.', '.', '.', '.', '.', '#', '#', '#', '.', '.', '.', '#', '=', '=', '#'], ['#', '=', 'D', '.', '.', '.', '#', '.', '.', '.', 'D', 'X', 'D', '.', '.', '.',
'D', '=', '=', '#'], ['#', '=', '#', '.', '.', '.', '.', '.', '.', '.', '#', '#', '#', '.', '.', '.', '#', '=', '=', '#'], ['#', '=', '#', '#', '#', '#', '#', '#', 'D', '#', '#', '=', '#', '#', 'D', '#', '#', '=', '=', '#'], ['#', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '#'], ['#', '=', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '=', '#'], ['#', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '#'], ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#']])
