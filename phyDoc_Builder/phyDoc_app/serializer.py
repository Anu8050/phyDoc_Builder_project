from rest_framework import  serializers
from .models import Document_templates, Document_details
class Document_templatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document_templates
        fields = '__all__'
        
class Document_detailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document_details
        fields = '__all__'