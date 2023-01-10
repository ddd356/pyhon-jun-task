import main
import unittest
from unittest import mock

rf1 = ("name", "Denis")
rf2 = ("mail", "mail@mail.com")
rf3 = ("period", "01.01.2023")
rf4 = ("period", "2023-01-01")
rf5 = ("cellphone", "+7 999 999 99 99")

f1 = ("name", "text")
f2 = ("mail", "email")
f3 = ("period", "date")
f4 = ("period", "date")
f5 = ("cellphone", "phone")

class MainTestCase(unittest.TestCase):

    def test_isDate(self):
        
        self.assertTrue(main.isDate('01.01.2023'))
        self.assertTrue(main.isDate('2023-01-01'))
        self.assertFalse(main.isDate('not a date'))
        self.assertFalse(main.isDate(''))

    def test_isPhone(self):

        self.assertTrue(main.isPhone('+7 999 999 99 99'))
        self.assertFalse(main.isPhone('7 999 999 99 99'))
        self.assertFalse(main.isPhone(''))

    def test_isEmail(self):

        self.assertTrue(main.isEmail('mail@mail.com'))
        self.assertFalse(main.isEmail('mail.com'))
        self.assertFalse(main.isEmail(''))

    def test_validator(self):
        self.assertEqual(main.validator("name", "Denis"), f1)
        self.assertEqual(main.validator("mail", "mail@mail.com"), f2)
        self.assertEqual(main.validator("period", "01.01.2023"), f3)
        self.assertEqual(main.validator("period", "2023-01-01"), f4)
        self.assertEqual(main.validator("cellphone", "+7 999 999 99 99"), f5)

    def test_Req2Fi(self):
        # rf: request field
        # f: field
        self.assertEqual(main.Req2Fi([rf1, rf2, rf3, rf4, rf5]), [f1, f2, f3, f4, f5])

if __name__ == '__main__':
    unittest.main()
