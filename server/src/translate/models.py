from django.db import models

class Translation(models.Model):
    romaji_text = models.CharField(max_length=255)
    hiragana_text = models.CharField(max_length=255, blank=True)
    katakana_text = models.CharField(max_length=255, blank=True)
    romaji_from_hiragana = models.CharField(max_length=255, blank=True)  # New field
    romaji_from_katakana = models.CharField(max_length=255, blank=True)  # New field
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (f"Romaji: {self.romaji_text} | Hiragana: {self.hiragana_text} | "
                f"Katakana: {self.katakana_text} | Romaji from Hiragana: {self.romaji_from_hiragana} | "
                f"Romaji from Katakana: {self.romaji_from_katakana}")