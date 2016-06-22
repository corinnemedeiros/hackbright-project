
import unittest
from hb_intro_final_project import *


class TestFinalProject_GetScore(unittest.TestCase):

	def test_get_score_level_difficult(self):
		level = "difficult"
		result = get_score(level)
		print "TestDifficult", TOTAL_SCORE
		self.assertEqual(result, 20)

	def test_get_score_level_easy(self):
		level = "easy"
		result = get_score(level)
		print "TestEasy", TOTAL_SCORE
		self.assertEqual(result, 25)

	def test_get_score_level_medium(self):
		level = "medium"
		result = get_score(level)
		print "TestMedium", TOTAL_SCORE
		self.assertEqual(result, 35)

if __name__ == '__main__':
	unittest.main()