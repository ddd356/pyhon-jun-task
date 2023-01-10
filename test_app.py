import app
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
        
        self.assertTrue(app.isDate('01.01.2023'))
        self.assertTrue(app.isDate('2023-01-01'))
        self.assertFalse(app.isDate('not a date'))
        self.assertFalse(app.isDate(''))

    def test_isPhone(self):

        self.assertTrue(app.isPhone('+7 999 999 99 99'))
        self.assertFalse(app.isPhone('7 999 999 99 99'))
        self.assertFalse(app.isPhone(''))

    def test_isEmail(self):

        self.assertTrue(app.isEmail('mail@mail.com'))
        self.assertFalse(app.isEmail('mail.com'))
        self.assertFalse(app.isEmail(''))

    def test_validator(self):
        self.assertEqual(app.validator("name", "Denis"), f1)
        self.assertEqual(app.validator("mail", "mail@mail.com"), f2)
        self.assertEqual(app.validator("period", "01.01.2023"), f3)
        self.assertEqual(app.validator("period", "2023-01-01"), f4)
        self.assertEqual(app.validator("cellphone", "+7 999 999 99 99"), f5)

    def test_Req2Fi(self):
        # rf: request field
        # f: field
        self.assertEqual(app.Req2Fi([rf1, rf2, rf3, rf4, rf5]), [f1, f2, f3, f4, f5])

if __name__ == '__main__':
    unittest.main()
