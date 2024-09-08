from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from ..models import Translation

class TranslationViewSetTestCase(APITestCase):
    def setUp(self):
        self.translation = Translation.objects.create(romaji_text='konnichiwa')

    def test_translation_endpoint(self):
        url = reverse('translation-translate', args=[self.translation.id])
        response = self.client.post(url)
        self.translation.refresh_from_db()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(self.translation.hiragana_text, 'こんにちは')
        self.assertEqual(self.translation.katakana_text, 'コンニチハ')

    def test_translation_with_spaces_and_newlines(self):
        self.translation.romaji_text = 'kon ni chi wa\nsayo nara'
        self.translation.save()
        url = reverse('translation-translate', args=[self.translation.id])
        response = self.client.post(url)
        self.translation.refresh_from_db()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(self.translation.hiragana_text, 'こん に ち は\nさよ なら')
        self.assertEqual(self.translation.katakana_text, 'コン ニ チ ハ\nサヨ ナラ')