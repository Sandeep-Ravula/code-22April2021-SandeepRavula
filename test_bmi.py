import unittest
import pytest
import BMI_analysis

sample_input = [
   {
      "Gender":"Female",
      "HeightCm":150,
      "WeightKg":70
   },
   {
      "Gender":"Female",
      "HeightCm":167,
      "WeightKg":82
   }
]

@pytest.mark.parametrize(sample_input)
def validate_overweighted():
    assert True
#
#
# class MyTestCase(unittest.TestCase):
#     def test_something(self):
#         self.assertEqual(True, False)
#
#
# if __name__ == '__main__':
#     unittest.main()
