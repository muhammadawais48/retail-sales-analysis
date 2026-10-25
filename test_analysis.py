import unittest,tempfile
from pathlib import Path
from src.analysis import analyze
class RetailTests(unittest.TestCase):
 def test_end_to_end(self):
  with tempfile.TemporaryDirectory() as d:
   result=analyze(Path('data/retail_sales.csv'),Path(d))
   self.assertEqual(result['orders'],500)
   self.assertTrue((Path(d)/'monthly_revenue.png').exists())
   self.assertTrue((Path(d)/'category_summary.csv').exists())
if __name__=='__main__':unittest.main()
