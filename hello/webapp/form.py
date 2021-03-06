from django import forms

from webapp.models import Guestbook

class BookForm(forms.ModelForm):

    class Meta:
        model = Guestbook
        fields = ('author', 'email', 'text', 'status')

class BookDeleteForm(forms.Form):
    author = forms.TimeField(required=True, label='Enter of the task, to delete! ')