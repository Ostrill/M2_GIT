from unittest import TestCase, main
from main import *


class ProgramTest(TestCase):
    def test_success_extracting(self):
        gr = 'V,несов,нп=непрош,ед,изъяв,3-л'
        required_parts = ['A', 'V', 'ADV']
        self.assertEqual(extract_and_check_part(gr, required_parts), 'V')

    def test_failed_extracting(self):
        gr = 'V,несов,нп=непрош,ед,изъяв,3-л'
        required_parts = ['A', 'ADV']
        self.assertIsNone(extract_and_check_part(gr, required_parts))


if __name__ == '__main__':
    main()
