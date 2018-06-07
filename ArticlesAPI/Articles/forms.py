from django.forms import ModelForm
from .models import Articles

class ArticleForm(ModelForm):
    class Meta:
        model = Articles
        fields = ["title", "content", "author"]