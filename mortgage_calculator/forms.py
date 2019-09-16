from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column

# https://snakeycode.wordpress.com/2015/02/14/multisection-django-bootstrap-forms-using-crispy/

PAYMENT_PERIOD_CHOICES = (
	('12', 'Monthly'),
	('52', 'Weekly'),
	('365', 'Daily'),
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

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.layout = Layout(
			Row(
				Column('name_account', css_class='form-group col-md-6 mb-0'),
				Column('loan_value', css_class='form-group col-md-6 mb-0'),
				css_class='form-row'
			),
			Row(
				Column('number_years_payment', css_class='form-group col-md-4 mb-0'),
				Column('interest', css_class='form-group col-md-4 mb-0'),
				Column('payment_period', css_class='form-group col-md-4 mb-0'),
				css_class='form-row'
			),

			Submit('totals', 'Totals'),
			Submit('lists', 'Get List')
		)

		# Customize the help text and label
		for fieldname in ['name_account', 'loan_value', 'number_years_payment', 'interest']:
			self.fields[fieldname].help_text = None
			# self.fields['fieldname'].label = fieldname + ":"


class MortgageCalcNumberPaymentsForm(forms.Form):
	name_account = forms.CharField(help_text="Enter the Account Name", initial="joe")
	loan_value = forms.FloatField(help_text="Enter the loan value", initial=100000)
	interest = forms.FloatField(help_text="Enter the interest", initial=6)
	loan_payment = forms.FloatField(help_text="Enter the monthly payment", initial=599.55)

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.layout = Layout(
			Row(
				Column('name_account', css_class='form-group col-md-6 mb-0'),
				Column('loan_value', css_class='form-group col-md-6 mb-0'),
				css_class='form-row'
			),
			Row(
				Column('interest', css_class='form-group col-md-6 mb-0'),
				Column('loan_payment', css_class='form-group col-md-6 mb-0'),
				css_class='form-row'
			),

			Submit('totals', 'Totals'),
		)

		# Customize the help text and label
		for fieldname in ['name_account', 'loan_value', 'interest', 'loan_payment']:
			self.fields[fieldname].help_text = None