from rest_framework import serializers
from .models import Translation

class TranslationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Translation
        fields = [
            'id', 'romaji_text', 'hiragana_text', 'katakana_text',
            'romaji_from_hiragana', 'romaji_from_katakana', 'created_at'
        ]
        read_only_fields = [
            'hiragana_text', 'katakana_text', 'romaji_from_hiragana',
            'romaji_from_katakana', 'created_at'
        ]
