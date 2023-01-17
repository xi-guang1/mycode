from unittest import TestCase
import unittest
from unittest.main import main
from main import Solution

class Test(TestCase,Solution):
    def test01_main(self):
        self.assertEqual(self.minimumMoves("OXOX"),1)
    def test02_main(self):
        self.assertEqual(self.minimumMoves("XXXOXOO"),2)
    def test03_main(self):
        self.assertEqual(self.minimumMoves("XXOX"),2)
        
if __name__ == "__main__":
    main()