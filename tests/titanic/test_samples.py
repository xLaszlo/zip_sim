from unittest import TestCase

from pydantic import ValidationError

from titanic.titanic_model import Passenger


class TestStrings(TestCase):
    def test_upper(self):
        self.assertEqual("spam".upper(), "SPAM")


class TestPassenger(TestCase):
    def test_passenger_with_no_id_raise_validation_error(self):
        with self.assertRaises(ValidationError):
            Passenger()
