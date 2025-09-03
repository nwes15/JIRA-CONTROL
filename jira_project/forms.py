from django import forms
from .models import Jira, Comment, Ticket, Customer


class JiraForm(forms.ModelForm):
    applied_releases = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        help_text='Enter releases separated by commas, e.g. "2024.1, 2024.2"'
    )

    class Meta:
        model = Jira
        fields = ['jira_number', 'type', 'first_release', 'applied_releases', 'creation_date', 'solution_date', 'tickets']
        widgets = {
            'jira_number': forms.TextInput(attrs={'class': 'form-control'}),
            'type': forms.Select(attrs={'class': 'form-select'}),
            'first_release': forms.TextInput(attrs={'class': 'form-control'}),
            'creation_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'solution_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'tickets': forms.SelectMultiple(attrs={'class': 'form-select'}),
        }
    
    def clean_applied_releases(self):
        data = self.cleaned_data['applied_releases']
        if data:
            # convert string to list stripping spaces
            return [r.strip() for r in data.split(',')]
        return []


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['author', 'text', 'informed_date']
        widgets = {
            'text': forms.Textarea(attrs={'rows': 3}),
            'informed_date': forms.DateInput(format=('%d/%m/%Y'), attrs={'type': 'date'}),
        }


class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['number', 'customer']
        widgets = {
            'number': forms.TextInput(attrs={'class': 'form-control'}),
            'customer': forms.Select(attrs={'class': 'form-select'}),
        }


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }