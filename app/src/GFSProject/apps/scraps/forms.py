from django import forms
from .models import Event
from django.forms import ModelForm, TextInput, Textarea


class EventForm(ModelForm):
    class Meta:
        model = Event  # ...1
        fields = ['title', "image", 'text', 'category', 'tag', 'date']  # ...2
        widgets = {
            'title': TextInput(attrs={'placeholder': 'title'}),  # ...3
            'text': Textarea(attrs={'placeholder': 'text'}),  # ...4
            'date': forms.SelectDateWidget
        }

    def save(self):
        event = Event.objects.create(
            title=self.cleaned_data['title'],
            text=self.cleaned_data['text'],
            category=self.cleaned_data['category'],
            date=self.cleaned_data['date'],
            image=self.cleaned_data['image']

        )
        if 'tag' in self.cleaned_data:
            event.tag.set(self.cleaned_data['tag'].values_list('id', flat=True))  # ...5