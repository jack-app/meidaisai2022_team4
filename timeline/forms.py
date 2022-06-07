# from attr import field
from django import forms
from .models import Event
from django.contrib.admin.widgets import AdminDateWidget    #インポート


class EventPostForm(forms.ModelForm):
    class Meta():
        model = Event
        fields = ('name', 'detail', "date", )
        labels={
           'name':'名前',
           'detail':'詳細',
           'date':'日付',
           }
        widgets = {
            "date": AdminDateWidget(),    #インポートしたウィジェットを使う指示
        }