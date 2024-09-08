from django.contrib import admin
from .models import Translation

class TranslationAdmin(admin.ModelAdmin):
    list_display = ('romaji_text', 'hiragana_text', 'katakana_text')
    search_fields = ('romaji_text', 'hiragana_text', 'katakana_text')

admin.site.register(Translation, TranslationAdmin)