from django_elasticsearch_dsl import fields
from django_elasticsearch_dsl_drf.serializers import (
    DocumentSerializer,
)
from .models import (
    Article,
)
from .documents import (
    ArticleDocument,
)


class ArticleDocumentSerializer(DocumentSerializer):
    class Meta:
        model = Article
        document = ArticleDocument

        fields = '__all__'

        def get_location(self, obj):
            try:
                return obj.location.to_dict()
            except:
                return {}