from rest_framework import routers
from .viewsets import TranslationViewSet
#from .views_elasticsearch import UserDocumentViewSet 

app_name = "translate"

router = routers.DefaultRouter()
router.register('translate', TranslationViewSet)
