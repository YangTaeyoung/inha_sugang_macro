import datetime
from unittest import TestCase

from util.crawler import extract_datetime


class Test(TestCase):
    def test_extract_datetime(self):
        text = "2023. 7. 21.(금) 10:00 ~ 7. 25.(화) 16:00 우선수강신청일"

        got = extract_datetime(text)

        expected = datetime.datetime(2023, 7, 21, 10, 0)

        self.assertEqual(got, expected)
