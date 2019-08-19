from django import forms

PAYMENT_PERIOD_CHOICES = (
	(12, 'monthly'),
	(52, 'weekly'),
	(365, 'dayly'),
)


class MortgageCalcForm(forms.Form):
	name_account = forms.CharField(help_text="Enter the Account Name", initial="joe")
	loan_value = forms.FloatField(help_text="Enter the loan value", initial=100000)
	number_years_payment = forms.IntegerField(help_text="Enter the time for payment(in years)", initial=30)
	interest = forms.FloatField(help_text="Enter the interest", initial=6)
	payment_period = forms.ChoiceField(
		help_text="Choose Payment Period",
		choices=PAYMENT_PERIOD_CHOICES,
		initial='monthly',
		widget=forms.Select(),
		required=True
	)


class MortgageCalcNumberPaymentsForm(forms.Form):
	name_account = forms.CharField(help_text="Enter the Account Name", initial="joe")
	loan_value = forms.FloatField(help_text="Enter the loan value", initial=100000)
	interest = forms.FloatField(help_text="Enter the interest", initial=6)
	loan_payment = forms.FloatField(help_text="Enter the monthly payment", initial=599.55)

