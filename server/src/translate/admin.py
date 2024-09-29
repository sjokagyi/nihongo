from django.contrib import admin
from .models import Translation

class TranslationAdmin(admin.ModelAdmin):
    list_display = ('romaji_text', 'hiragana_text', 'katakana_text', 'romaji_from_hiragana', 'romaji_from_katakana')
    search_fields = ('romaji_text', 'hiragana_text', 'katakana_text', 'romaji_from_hiragana', 'romaji_from_katakana')

admin.site.register(Translation, TranslationAdmin)