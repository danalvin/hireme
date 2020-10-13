from django import forms

from .models import Event


class CreateEventForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(CreateEventForm, self).__init__(*args, **kwargs)
        self.fields['name'].label = "Event Name"
        self.fields['description'].label = "Event Description"
        self.fields['cake'].label = "Do you want cake?"
        self.fields['event_size'].label = "Event size estimate"
        self.fields['event_type'].label = "Event type"
        self.fields['resources'].label = "Resources"
        self.fields['AoB'].label = "Any Other Business"

        self.fields['name'].widget.attrs.update(
            {
                'placeholder': 'Enter Event Name',
            }
        )
        self.fields['location'].widget.attrs.update(
            {
                'placeholder': 'Event location',
            }
        )
        self.fields['description'].widget.attrs.update(
            {
                'placeholder': 'Event Description',
            }
        )
        self.fields['cake'].widget.attrs.update(
            {
                'placeholder': 'Tick for cake',
            }
        )
        self.fields['event_size'].widget.attrs.update(
            {
                'placeholder': 'Event size, 0-50, 50-100, 100-200, 200+',
            }
        )
        self.fields['last_date'].widget.attrs.update(
            {
                'placeholder': 'When is the last date of the event?',
            }
        )
        self.fields['event_type'].widget.attrs.update(
            {
                'placeholder': 'What type of event do you want?',
            }
        )
        self.fields['resources'].widget.attrs.update(
            {
                'placeholder': 'Do you want any resource eg chairs and tents',
            }
        )
        self.fields['AoB'].widget.attrs.update(
            {
                'placeholder': 'Anything else youd want us to know?',
            }
        )


    class Meta:
        model = Event
        fields = ['name', 'description', 'location', 'cake', 'event_size', 'event_type', 'last_date', 'resources', 'AoB']
        labels = {
            "last_date": "Event Date",
            "resources": "What do you need during the event?"
        }

    def is_valid(self):
        valid = super(CreateEventForm, self).is_valid()

        # if already valid, then return True
        if valid:
            return valid
        return valid

    def save(self, commit=True):
        event = super(CreateEventForm, self).save(commit=False)
        if commit:
            event.save()
        return event
