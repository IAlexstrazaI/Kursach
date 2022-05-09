from .models import notice, comment
from django.forms import ModelForm, TextInput


class noticeform(ModelForm):
    class Meta:
        model = notice
        fields = ["text"]
