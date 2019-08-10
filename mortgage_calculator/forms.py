from django import forms


class MortgageCalcForm(forms.Form):
	name_account = forms.CharField(help_text="Enter the Account Name", initial="joe")
	loan_value = forms.FloatField(help_text="Enter the loan value", initial=100000)
	number_years_payment = forms.IntegerField(help_text="Enter the time for payment(in years)", initial=30)
	interest = forms.FloatField(help_text="Enter the interest", initial=6)
