from django.forms import ModelForm, Textarea

from .models import Posts


class PostForm(ModelForm):
    class Meta:
        model = Posts
        fields = '__all__'
        exclude = {'author',}
        widgets = {
            'body': Textarea()
        }

