import math
import unittest
from statistics import calculateStats


class StatsTest(unittest.TestCase):
  def test_report_min_max_avg(self):
    computedStats = calculateStats([1.5, 8.9, 3.2, 4.5])
    epsilon = 0.001
    self.assertAlmostEqual(computedStats["avg"], 4.525, delta=epsilon)
    self.assertAlmostEqual(computedStats["max"], 8.9, delta=epsilon)
    self.assertAlmostEqual(computedStats["min"], 1.5, delta=epsilon)

  def test_avg_is_nan_for_empty_input(self):
    computedStats = calculateStats([])
    self.assertTrue(math.isnan(computedStats["avg"]))
    self.assertTrue(math.isnan(computedStats["max"]))
    self.assertTrue(math.isnan(computedStats["min"]))

  def test_single_element(self):
    computedStats = calculateStats([7.0])
    self.assertAlmostEqual(computedStats["avg"], 7.0)
    self.assertAlmostEqual(computedStats["max"], 7.0)
    self.assertAlmostEqual(computedStats["min"], 7.0)

  def test_all_same_elements(self):
    computedStats = calculateStats([2.2, 2.2, 2.2])
    self.assertAlmostEqual(computedStats["avg"], 2.2)
    self.assertAlmostEqual(computedStats["max"], 2.2)
    self.assertAlmostEqual(computedStats["min"], 2.2)

  def test_negative_numbers(self):
    computedStats = calculateStats([-1.0, -5.0, -3.0])
    self.assertAlmostEqual(computedStats["avg"], -3.0)
    self.assertAlmostEqual(computedStats["max"], -1.0)
    self.assertAlmostEqual(computedStats["min"], -5.0)

  def test_mixed_positive_negative(self):
    computedStats = calculateStats([-2.0, 0.0, 2.0])
    self.assertAlmostEqual(computedStats["avg"], 0.0)
    self.assertAlmostEqual(computedStats["max"], 2.0)
    self.assertAlmostEqual(computedStats["min"], -2.0)

  def test_large_numbers(self):
    computedStats = calculateStats([1e10, 1e10 + 1, 1e10 - 1])
    self.assertAlmostEqual(computedStats["avg"], 1e10)
    self.assertAlmostEqual(computedStats["max"], 1e10 + 1)
    self.assertAlmostEqual(computedStats["min"], 1e10 - 1)
    
  def test_string_numbers(self):
    computedStats = calculateStats(["1.5", "2.5", "3.5"])
    self.assertAlmostEqual(computedStats["avg"], 2.5)
    self.assertAlmostEqual(computedStats["max"], 3.5)
    self.assertAlmostEqual(computedStats["min"], 1.5)
    
  def test_mixed_valid_invalid_input(self):
    computedStats = calculateStats([1.0, "2.0", "invalid", 3.0, None, True])
    self.assertAlmostEqual(computedStats["avg"], 1.75)  # 1.0, 2.0, 3.0, 1.0 (True) = 7.0/4
    self.assertAlmostEqual(computedStats["max"], 3.0)
    self.assertAlmostEqual(computedStats["min"], 1.0)
    
  def test_non_list_input(self):
    # Test with a string
    computedStats = calculateStats("not a list")
    self.assertTrue(math.isnan(computedStats["avg"]))
    self.assertTrue(math.isnan(computedStats["max"]))
    self.assertTrue(math.isnan(computedStats["min"]))
    
    # Test with a number
    computedStats = calculateStats(42)
    self.assertTrue(math.isnan(computedStats["avg"]))
    self.assertTrue(math.isnan(computedStats["max"]))
    self.assertTrue(math.isnan(computedStats["min"]))
    
  def test_all_invalid_inputs(self):
    computedStats = calculateStats(["invalid", None, "error"])
    self.assertTrue(math.isnan(computedStats["avg"]))
    self.assertTrue(math.isnan(computedStats["max"]))
    self.assertTrue(math.isnan(computedStats["min"]))
    
  def test_floating_point_precision(self):
    computedStats = calculateStats([0.1, 0.2, 0.3])
    # The sum 0.1 + 0.2 + 0.3 is not exactly 0.6 due to floating point precision
    epsilon = 1e-10
    self.assertAlmostEqual(computedStats["avg"], 0.2, delta=epsilon)
    self.assertAlmostEqual(computedStats["max"], 0.3, delta=epsilon)
    self.assertAlmostEqual(computedStats["min"], 0.1, delta=epsilon)


if __name__ == "__main__":
  unittest.main()
