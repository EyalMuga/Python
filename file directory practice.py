import unittest
import os
import csv


class TestFI(unittest.TestCase):

    # ________________________________init__________________________________#

    @classmethod
    def setUpClass(cls) -> None:
        cls.csv1 = CsvFile('/Users/MUGA/PycharmProjects/EDULABS/edulabs excercises/Classes practise/new_AAPL.csv')
        cls.json1 = JsonFile('/Users/MUGA/PycharmProjects/EDULABS/edulabs excercises/Classes practise/data.json')
        cls.txt1 = TxtFile('/Users/MUGA/PycharmProjects/EDULABS/edulabs excercises/Classes practise/data.txt')

    # __________________________test_file_size_txt____________________________#

    def test2_file_size1(self):
        result = self.txt_file1.file_size()
        self.assertEqual(result, os.path.getsize("FHfiles/alice_in_wonderland.txt"))

    def test3_file_size2(self):
        result = self.txt_file4.file_size()
        self.assertEqual(result, os.path.getsize("FHfiles/empty.txt"))

    def test4_file_size3(self):
        result = self.txt_file4.file_size()
        self.assertEqual(result, os.path.getsize("FHfiles/empty.txt"))

    def test5_file_size4(self):
        result = self.txt_file5.file_size()
        self.assertEqual(result, os.path.getsize("FHfiles/sample-2mb-text-file.txt"))

    # ___________________________test_file_size_csv__________________________________#

    def test6_file_size5(self):
        result = self.csv_file2.file_size()
        self.assertEqual(result, os.path.getsize("FHfiles/email-password-recovery-code.csv"))

    def test7_file_size6(self):
        result = self.csv_file1.file_size()
        self.assertEqual(result, os.path.getsize("FHfiles/csv_ex.csv"))

    # ___________________________test_file_size_json__________________________________#

    def test8_file_size7(self):
        result = self.json_file1.file_size()
        self.assertEqual(result, os.path.getsize("FHfiles/json_ex.json"))

    def test9_file_size8(self):
        result = self.json_file2.file_size()
        self.assertEqual(result, os.path.getsize("FHfiles/json_ex2.json"))

    # __________________________test_file_size_unit_txt______________________________#

    def test10_file_size_unit1(self):
        result = self.txt_file5.file_size_unit()
        self.assertEqual(result, os.path.getsize("FHfiles/sample-2mb-text-file.txt"))

    def test11_file_size_unit2(self):
        result = self.txt_file5.file_size_unit("bytes")
        self.assertEqual(result, os.path.getsize("FHfiles/sample-2mb-text-file.txt"))

    def test12_file_size_unit3(self):
        result = self.txt_file5.file_size_unit("megabytes")
        self.assertEqual(result, self.txt_file5.file_size() / (1024 * 1024))

    def test13_file_size_unit4(self):
        result = self.txt_file5.file_size_unit("gigabytes")
        self.assertEqual(result, self.txt_file5.file_size() / (1024 ** 3))

    def test14_file_size_unit5(self):
        result = self.txt_file5.file_size_unit("terabytes")
        self.assertEqual(result, self.txt_file5.file_size() / (1024 ** 4))

    def test15_file_size_unit6(self):
        result = self.txt_file5.file_size_unit()
        assert result == os.path.getsize("FHfiles/sample-2mb-text-file.txt"), "in bytes"

    def test16_file_size_unit7(self):
        txt_file1 = TxtFile("FHfiles/sample-2mb-text-file.txt")
        result = txt_file1.file_size_unit("tdsfdsafaggerwsaf34324")
        self.assertEqual(result, os.path.getsize("FHfiles/sample-2mb-text-file.txt"))

    def test17_file_size_unit8(self):
        result = self.txt_file5.file_size_unit("1423156143")
        self.assertEqual(result, os.path.getsize("FHfiles/sample-2mb-text-file.txt"))

    def test18_file_size_unit9(self):
        result = self.txt_file5.file_size_unit(False)
        self.assertEqual(result, os.path.getsize("FHfiles/sample-2mb-text-file.txt"))

    # __________________________test_file_size_unit_csv______________________________#

    def test19_file_size_unit10(self):
        result = self.csv_file2.file_size_unit("dssadsada")
        self.assertEqual(result, os.path.getsize("FHfiles/email-password-recovery-code.csv"))

    def test20_file_size_unit11(self):
        result = self.csv_file2.file_size_unit(True)
        self.assertEqual(result, os.path.getsize("FHfiles/email-password-recovery-code.csv"))

    def test21_file_size_unit12(self):
        result = self.csv_file2.file_size_unit(1)
        self.assertEqual(result, os.path.getsize("FHfiles/email-password-recovery-code.csv"))

    def test22_file_size_unit13(self):
        result = self.csv_file2.file_size_unit("megabytes")
        self.assertEqual(result, self.csv_file2.file_size() / (1024 * 1024))

    def test23_file_size_unit14(self):
        result = self.csv_file2.file_size_unit("gigabytes")
        self.assertEqual(result, self.csv_file2.file_size() / (1024 ** 3))

    def test24_file_size_unit15(self):
        result = self.csv_file2.file_size_unit("terabytes")
        self.assertEqual(result, self.csv_file2.file_size() / (1024 ** 4))

    def test25_file_size_unit16(self):
        result = self.csv_file2.file_size_unit()
        self.assertEqual(result, os.path.getsize("FHfiles/email-password-recovery-code.csv"))

    # __________________________test_file_size_unit_csv______________________________#

    def test26_file_size_unit17(self):
        result = self.json_file1.file_size_unit("dsaddadads")
        self.assertEqual(result, os.path.getsize("FHfiles/json_ex.json"))

    def test27_file_size_unit18(self):
        result = self.json_file1.file_size_unit("12343214")
        self.assertEqual(result, os.path.getsize("FHfiles/json_ex.json"))

    def test28_file_size_unit19(self):
        result = self.json_file1.file_size_unit(True)
        self.assertEqual(result, os.path.getsize("FHfiles/json_ex.json"))

    def test29_file_size_unit20(self):
        result = self.json_file1.file_size_unit(1)
        self.assertEqual(result, os.path.getsize("FHfiles/json_ex.json"))

    def test30_file_size_unit21(self):
        result = self.json_file1.file_size_unit("megabytes")
        self.assertEqual(result, self.json_file1.file_size() / (1024 * 1024))

    def test31_file_size_unit22(self):
        result = self.json_file1.file_size_unit("gigabytes")
        self.assertEqual(result, self.json_file1.file_size() / (1024 ** 3))

    def test32_file_size_unit23(self):
        result = self.json_file1.file_size_unit("terabytes")
        self.assertEqual(result, self.json_file1.file_size() / (1024 ** 4))

    def test33_file_size_unit24(self):
        result = self.json_file2.file_size_unit()
        self.assertEqual(result, os.path.getsize("FHfiles/json_ex2.json"))

    # _______________________________________________________________________#
    # ________________________________CSV____________________________________#
    # _______________________________________________________________________#
    # ___________________________test_Csv_rows_______________________________#

    def test34_rows1(self):
        self.assertEqual(self.csv_file2.rows(), len(self.csv_file2.content()))

    def test35_rows2(self):
        self.assertEqual(self.csv_file1.rows(), len(self.csv_file1.content()))

    def test36_rows3(self):
        self.assertEqual(self.csv_file3.rows(), len(self.csv_file3.content()))

    def test38_rows5(self):
        self.assertEqual(self.csv_file3.rows(), 0)

    # ___________________________test_Csv_columns_______________________________#

    def test39_row1(self):
        self.assertEqual(self.csv_file2.columns(), 8)

    def test40_row2(self):
        self.assertEqual(self.csv_file1.columns(), 4)

    def test41_row3(self):
        self.assertEqual(self.csv_file3.columns(), 0)

    def test42_row4(self):
        self.assertEqual(self.csv_file4.columns(), 1)

    # _________________________test_Csv_by_columns_______________________________#

    def test43_by_row1(self):
        csv_file1 = CsvFile("FHfiles/email-password-recovery-code.csv", ";")
        csv_row = csv_file1.by_row(6)
        assert csv_row == csv_file1.content()[4]

    def test44_by_row2(self):
        csv_file1 = CsvFile("FHfiles/csv_ex.csv")
        csv_row = csv_file1.by_row(4)
        assert csv_row == csv_file1.content()[2]

    def test45_by_row3(self):
        csv_file1 = CsvFile("FHfiles/empty.csv")
        csv_row = csv_file1.by_row(0)
        assert csv_row == dict()

    # _________________________test_Csv_by_columns_______________________________#

    def test46_by_column1(self):
        csv_file1 = CsvFile("FHfiles/email-password-recovery-code.csv", ";")
        csv_column = csv_file1.by_column(4)
        assert csv_column == ["Rachel", "Laura", "Craig", "Mary", "Jamie"]

    def test47_by_column2(self):
        csv_file1 = CsvFile("FHfiles/csv_ex.csv")
        csv_column = csv_file1.by_column(0)
        assert csv_column == ['1', '2', '3']

    def test48_by_column3(self):
        csv_file1 = CsvFile("FHfiles/empty.csv")
        csv_column = csv_file1.by_column(0)
        assert csv_column == list()

    # _________________________test_Csv_by_columns_______________________________#

    def test49_by_cell1(self):
        csv_file1 = CsvFile("FHfiles/email-password-recovery-code.csv", ";")
        csv_cell = csv_file1.by_cell(1, 2)
        assert csv_cell == "04ap67"

    def test50_by_cell2(self):
        csv_file1 = CsvFile("FHfiles/empty.csv")
        with self.assertRaises(Exception):
            csv_cell = csv_file1.by_cell(6, 3)

    def test51_by_cell3(self):
        csv_file1 = CsvFile("FHfiles/csv_ex.csv")
        csv_cell = csv_file1.by_cell(2, 3)
        assert csv_cell == "bjones@example.com"

    # _______________________________________________________________________#
    # ________________________________JSON___________________________________#
    # _______________________________________________________________________#
    # _________________________test_Json_is_list_____________________________#

    def test52_is_list1(self):
        json_file1 = JsonFile("FHfiles/json_ex2.json")
        json_file = json_file1.is_list()
        assert json_file is True

    def test53_is_list2(self):
        json_file1 = JsonFile("FHfiles/json_ex.json")
        json_file = json_file1.is_list()
        assert json_file is False

    def test54_is_list3(self):
        json_file1 = JsonFile("FHfiles/empty_broken.json")
        json_file = json_file1.is_list()
        assert json_file is False

    # _________________________test_Json_is_object_____________________________#

    def test55_is_list1(self):
        json_file1 = JsonFile("FHfiles/json_ex2.json")
        json_file = json_file1.is_object()
        assert json_file is False

    def test56_is_list2(self):
        json_file1 = JsonFile("FHfiles/json_ex.json")
        json_file = json_file1.is_object()
        assert json_file is True

    def test57_is_list3(self):
        json_file1 = JsonFile("FHfiles/empty_broken.json")
        json_file = json_file1.is_object()
        assert json_file is False

    # _______________________________________________________________________#
    # ________________________________TXT____________________________________#
    # _______________________________________________________________________#
    # _______________________test_Txt_words_amount___________________________#

    def test58_words_amount1(self):
        txt_file1 = TxtFile("FHfiles/sample-2mb-text-file.txt")
        txt_file = txt_file1.words_amount()
        assert txt_file == len(str(txt_file1.content()).split())

    def test59_words_amount2(self):
        txt_file1 = TxtFile("FHfiles/alice_in_wonderland.txt_alice_in_wonderland2.txt")
        txt_file = txt_file1.words_amount()
        assert txt_file == len(str(txt_file1.content()).split())

    def test60_words_amount3(self):
        txt_file1 = TxtFile("FHfiles/empty.txt")
        txt_file = txt_file1.words_amount()
        assert txt_file == 0

    # _______________________test_Txt_avg_len_of_word__________________________#

    def test61_avg_word_len1(self):
        counter: int = 0
        txt_file1 = TxtFile("FHfiles/alice_in_wonderland.txt_alice_in_wonderland2.txt")
        txt_file = txt_file1.avg_word_len()
        for word in str(txt_file1.content()).split():
            counter += len(word)
        assert txt_file == counter / len(str(txt_file1.content()).split())

    def test62_avg_word_len2(self):
        counter: int = 0
        txt_file1 = TxtFile("FHfiles/alice_in_wonderland.txt")
        txt_file = txt_file1.avg_word_len()
        for word in str(txt_file1.content()).split():
            counter += len(word)
        assert txt_file == counter / len(str(txt_file1.content()).split())

    def test63_avg_word_len3(self):
        txt_file1 = TxtFile("FHfiles/empty.txt")
        with self.assertRaises(Exception):
            txt_file1.avg_word_len()


if __name__ == "__main__":
    unittest.main()
