import unittest
import atm



class TestATM (unittest.TestCase):
    def test_withdraw(self):
        self.assertEqual(atm.withdraw(60,100),40)
        self.assertEqual(atm.withdraw(50,100),50)
        self.assertEqual(atm.withdraw(1, 100),99)



if __name__ == '__main__':
    unittest.main()
