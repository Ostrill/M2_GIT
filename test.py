from unittest import TestCase, main
from main import *
import os


class ProgramTest(TestCase):
    def test_success_extracting(self):
        gr = 'V,несов,нп=непрош,ед,изъяв,3-л'
        required_parts = ['A', 'V', 'ADV']
        self.assertEqual(extract_and_check_part(gr, required_parts), 'V')

    def test_failed_extracting(self):
        gr = 'V,несов,нп=непрош,ед,изъяв,3-л'
        required_parts = ['A', 'ADV']
        self.assertIsNone(extract_and_check_part(gr, required_parts))

    def test_opening(self):
        test_path = 'test_opening.txt'
        test_content = 'test'
        with open(test_path, 'w') as file:
            file.write(test_content)
        self.assertEqual(open_text_file(test_path), test_content)
        os.remove(test_path)

    def test_analyze(self):
        test_query = 'Простая проверка'
        self.assertIsInstance(analyze(test_query), list)
        for token in analyze(test_query):
            self.assertIsInstance(token, dict)

    def test_counting_A(self):
        test_query = 'Простая проверка на подсчет частей речи'
        test_analysis = analyze(test_query)
        self.assertDictEqual(count_parts(test_analysis), {'A': 1, 'ADV': 0, 'V': 0})

    def test_counting_ADV(self):
        test_query = 'Качественно и быстро'
        test_analysis = analyze(test_query)
        self.assertDictEqual(count_parts(test_analysis), {'A': 0, 'ADV': 2, 'V': 0})

    def test_counting_V(self):
        test_query = 'В этом тесте могут находиться два глагола'
        test_analysis = analyze(test_query)
        self.assertDictEqual(count_parts(test_analysis), {'A': 0, 'ADV': 0, 'V': 2})

    def test_printing_success(self):
        self.assertIsNone(print_result({'A': 0, 'ADV': 2, 'V': 0}))

    def test_printing_unexpected_dict(self):
        self.assertIsNone(print_result({1: '2', 3: '4'}))

    def test_printing_fail(self):
        with self.assertRaises(Exception) as e:
            print_result(10)
        self.assertIsInstance(e.exception, AttributeError)


if __name__ == '__main__':
    main()
