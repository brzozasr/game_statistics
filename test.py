import reports
import unittest


def get_sorted():
    return ['Age of Empires',
            'Command & Conquer',
            'Counter-Strike',
            'Counter-Strike: Condition Zero',
            'Crysis',
            'Diablo II',
            'Diablo III',
            'Doom 3',
            'EverQuest',
            "Garry's Mod",
            'Guild Wars',
            'Half-Life',
            'Half-Life 2',
            'Minecraft',
            'Populous',
            'StarCraft',
            'StarCraft II: Wings of Liberty',
            'Terraria',
            'The Sims',
            'The Sims 2',
            'The Sims 3',
            'Warcraft III: Reign of Chaos',
            'Warhammer 40,000: Dawn of War (including expansions)',
            'World of Warcraft']


class Tester(unittest.TestCase):
    input_file = "game_stat.txt"

    def test_1_count_games(self):
        result = reports.count_games(self.input_file)
        self.assertEqual(result, 24)

    def test_2_decide(self):
        result = reports.decide(self.input_file, 2000)
        self.assertTrue(result)

    def test_3_get_latest(self):
        result = reports.get_latest(self.input_file)
        expected = "Diablo III"
        self.assertEqual(result, expected)

    def test_4_count_by_genre(self):
        result = reports.count_by_genre(
            self.input_file, "First-person shooter")
        self.assertEqual(result, 6)

    def test_5_get_line_number_by_title(self):
        result = reports.get_line_number_by_title(
            self.input_file, "Counter-Strike")
        self.assertEqual(result, 6)

    def test_5_raises_error_when_no_game(self):
        with self.assertRaises(ValueError):
            result = reports.get_line_number_by_title(
                self.input_file, "Non-existing game")

    def test_bonus_1_sort_abc(self):
        sorted_result = reports.sort_abc(self.input_file)
        expected_result = get_sorted()
        self.assertEqual(sorted_result, expected_result)

    def test_bonus_1_check_forbidden_functions(self):
        with open("reports.py") as file:
            lines = file.read()
            self.assertNotRegex(lines, r"\bsort(ed)?\(")

    def test_bonus_2_get_genres(self):
        result = reports.get_genres(self.input_file)
        expected_result = sorted(["Action-adventure", "First-person shooter",
                                  "Real-time strategy", "RPG", "Sandbox",
                                  "Simulation", "Survival game"])

        self.assertEqual(result, expected_result)

    def test_bonus_3_when_was_top_sold_fps(self):
        result = reports.when_was_top_sold_fps(self.input_file)
        self.assertEqual(result, 1999)

    def test_bonus_3_raises_error_when_no_fps_game(self):
        with self.assertRaises(ValueError):
            result = reports.when_was_top_sold_fps("game_stat_nofpstest.txt")


def main():
    unittest.main()


if __name__ == '__main__':
    main()
