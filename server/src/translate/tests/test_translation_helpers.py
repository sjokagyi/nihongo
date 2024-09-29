from django.test import TestCase
from ..translation_helpers import translate_to_hiragana, translate_to_katakana, katakana_to_romaji, hiragana_to_romaji

class TranslationHelperTestCase(TestCase):
    def test_translate_to_hiragana(self):
        romaji = 'konnichiwa'
        expected_hiragana = 'こんにちは'
        result = translate_to_hiragana(romaji)
        self.assertEqual(result, expected_hiragana)

    def test_translate_to_katakana(self):
        romaji = 'gakkou'
        expected_katakana = 'ガッコウ'
        result = translate_to_katakana(romaji)
        self.assertEqual(result, expected_katakana)

    def test_gemination_handling(self):
        romaji = 'gakkou'
        expected_hiragana = 'がっこう'
        result = translate_to_hiragana(romaji)
        self.assertEqual(result, expected_hiragana)

    def test_long_vowel_handling(self):
        romaji = 'kaapetto'
        expected_katakana = 'カーペット'
        result = translate_to_katakana(romaji)
        self.assertEqual(result, expected_katakana)

    def test_translation_with_spaces(self):
        romaji = 'kon ni chi wa'
        expected_hiragana = 'こん に ち は'
        result = translate_to_hiragana(romaji)
        self.assertEqual(result, expected_hiragana)

    def test_translation_with_capital_letters(self):
        romaji = 'Konnichiwa'
        expected_hiragana = 'こんにちは'
        result = translate_to_hiragana(romaji)
        self.assertEqual(result, expected_hiragana)

    def test_translation_with_newlines(self):
        romaji = 'konnichiwa\nsayonara'
        expected_hiragana = 'こんにちは\nさよなら'
        result = translate_to_hiragana(romaji)
        self.assertEqual(result, expected_hiragana)

    def test_translation_with_blank_lines(self):
        romaji = 'konnichiwa\n\nsayonara'
        expected_hiragana = 'こんにちは\n\nさよなら'
        result = translate_to_hiragana(romaji)
        self.assertEqual(result, expected_hiragana)

    def test_gemination_handling(self):
        romaji = 'gakkou'
        expected_hiragana = 'がっこう'
        result = translate_to_hiragana(romaji)
        self.assertEqual(result, expected_hiragana)

    def test_double_consonants_handling(self):
        katakana = 'ガッコウ'
        expected_romaji = 'gakkou'
        result = katakana_to_romaji(katakana)
        self.assertEqual(result, expected_romaji)

    def test_translation_with_double_n(self):
        romaji = 'konnichiwa'
        expected_hiragana = 'こんにちは'
        result = translate_to_hiragana(romaji)
        self.assertEqual(result, expected_hiragana)

    def test_translation_sayonara(self):
        romaji = 'sayonara'
        expected_hiragana = 'さよなら'
        result = translate_to_hiragana(romaji)
        self.assertEqual(result, expected_hiragana)

    def test_translation_konnichiwa_sayonara_1(self):
        romaji = 'Konnichiwa sayonara'
        expected_hiragana = 'こんにちは さよなら'
        expected_katakana = 'コンニチワ サヨナラ'
        hiragana_result = translate_to_hiragana(romaji)
        katakana_result = translate_to_katakana(romaji)
        self.assertEqual(hiragana_result, expected_hiragana)
        self.assertEqual(katakana_result, expected_katakana)

    def test_translation_konnichiwa_sayonara_2(self):
        romaji = 'Konnichiwa Sayonara'
        expected_hiragana = 'こんにちは さよなら'
        expected_katakana = 'コンニチワ サヨナラ'
        hiragana_result = translate_to_hiragana(romaji)
        katakana_result = translate_to_katakana(romaji)
        self.assertEqual(hiragana_result, expected_hiragana)
        self.assertEqual(katakana_result, expected_katakana)