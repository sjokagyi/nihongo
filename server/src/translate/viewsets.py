from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Translation
from .serializers import TranslationSerializer
from .translation_helpers import (
    translate_to_hiragana, translate_to_katakana,
    hiragana_to_romaji, katakana_to_romaji
)

class TranslationViewSet(viewsets.ModelViewSet):
    queryset = Translation.objects.all()
    serializer_class = TranslationSerializer

    @csrf_exempt  # Disable CSRF for this view
    @action(detail=True, methods=['post'])
    def translate(self, request, pk=None):
        translation = self.get_object()
        
        # Romaji to Hiragana and Katakana translations
        translation.hiragana_text = translate_to_hiragana(translation.romaji_text)
        translation.katakana_text = translate_to_katakana(translation.romaji_text)
        
        # Hiragana/Katakana to Romaji translations
        translation.romaji_from_hiragana = hiragana_to_romaji(translation.hiragana_text)
        translation.romaji_from_katakana = katakana_to_romaji(translation.katakana_text)
        
        translation.save()
        return Response(self.get_serializer(translation).data)
