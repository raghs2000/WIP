from django import forms
from .models import Event
from datetime import datetime
from bootstrap_datepicker_plus import DateTimePickerInput

eventTypes = (('Day Event', 'Day Event'), ('Exam', 'Exam'), ('Deadline'
              , 'Deadline'))
eventScopes = (('Private', 'Private'), ('Public', 'Pubic'))
recurrences = (('Never', 'Never'), ('Daily', 'Daily'), ('Monthly',
               'Monthly'), ('Yearly', 'Yearly'))


class addEvent(forms.ModelForm):
    def get_now():
        return datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    eventType = forms.ChoiceField(choices=eventTypes, label='')
    eventName = forms.CharField(max_length=200, label='', widget=forms.TextInput(attrs={'placeholder': 'Event Name'}))
    description = forms.CharField(max_length=200, label='', required=False, widget=forms.TextInput(attrs={'placeholder': 'Description'}))
    dateActive = forms.DateTimeField(initial=get_now,label='',widget=DateTimePickerInput())
    eventScope = forms.ChoiceField(choices=eventScopes,label='')
    recurrence = forms.ChoiceField(choices=recurrences, label='')

    class Meta:
        model = Event
        exclude = ['dateCreated']