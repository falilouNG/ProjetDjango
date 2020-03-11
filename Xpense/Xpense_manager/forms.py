from django import forms

class ExpenseForm(forms.Form):
    title = forms.CharField()
    amount = forms.DecimalField()
    date = forms.DateField()