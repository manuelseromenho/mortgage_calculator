from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import FormView

from mortgage_calculator.forms import MortgageCalcForm, MortgageCalcNumberPaymentsForm

from mortgage_calculator.utils import MortgageAccount

#https://developer.mozilla.org/pt-BR/docs/Learn/Server-side/Django/Forms

"""
Mortgage Calculator - Calculate the monthly payments of a fixed term mortgage over given Nth terms at a given interest 
rate. Also figure out how long it will take the user to pay back the loan. For added complexity, add an option for users 
to select the compounding interval (Monthly, Weekly, Daily, Continually).
"""


class HomeView(View):
	def get(self, request):
		return render(request, 'mortgage_calculator/index.html')


class SubmitFormData(FormView):
	template_name = "mortgage_calculator/mortgage_calc.html"
	form_class = MortgageCalcForm

	def __init__(self, *args, **kargs):
		self.form = super(SubmitFormData, self).__init__(*args, **kargs)

	# def get_form(self, *args, **kwargs):

	# def form_invalid(self, form):
	# 	print("HELLO")
	# 	return render(self.request, 'mortgage_calculator/totals.html')

	def form_valid(self, form):
		name = form.cleaned_data['name_account']
		loan = form.cleaned_data['loan_value']
		number_years_payment = form.cleaned_data['number_years_payment']
		interest = form.cleaned_data['interest']
		payment_period = int(form.cleaned_data['payment_period'])

		# form.cleaned_data['payment_period'] in form.fields['payment_period'].choices

		if 'totals' in self.request.POST:

			account_created = MortgageAccount(name, loan, number_years_payment, interest, payment_period)
			result = account_created.calc_loan_payment

			#dict(bf.field.choices).get(int(bf.data))

			context = {
				'name': name,
				'loan': loan,
				'time': number_years_payment,
				'interest': interest,
				'payment_period': dict(form['payment_period'].field.choices).get(form['payment_period'].data),
				'number_payments_true': False,
				'result': round(result, 2),
			}
			return render(self.request, 'mortgage_calculator/totals.html', context)
		elif 'lists' in self.request.POST:

			account_created = MortgageAccount(name, loan, number_years_payment, interest)
			result = account_created.calc_loan_payment

			percent_interest = interest / 100
			monthly_interest = (loan * (percent_interest / payment_period))
			principal = (result - monthly_interest)
			ending_balance = loan - principal
			total_interest = monthly_interest

			index = 1

			amortization_list = []

			starting_balance = loan
			while (starting_balance - result) > 0:
				if index > 1:
					starting_balance = ending_balance
				monthly_interest = starting_balance * (percent_interest / payment_period)
				principal = result - monthly_interest

				if index > 1:
					ending_balance -= principal
					total_interest += monthly_interest

				amortization_list.append({
					'index': index,
					'starting_balance': round(starting_balance, 2),
					'monthly_payment': round(result, 2),
					'monthly_interest': round(monthly_interest, 2),
					'principal': round(principal, 2),
					'ending_balance': abs(round(ending_balance, 2)),
					'total_interest': round(total_interest, 2),
				})

				index += 1

			context = {
				'amortization_list': amortization_list,
			}

			return render(self.request, 'mortgage_calculator/loan_amortization.html', context)


class SubmitFormDataNumberPayments(FormView):
	template_name = "mortgage_calculator/mortgage_calc.html"
	form_class = MortgageCalcNumberPaymentsForm

	def __init__(self, *args, **kargs):
		self.form = super(SubmitFormDataNumberPayments, self).__init__(*args, **kargs)

	def form_valid(self, form):
		if 'totals' in self.request.POST:
			name = form.cleaned_data['name_account']
			loan = form.cleaned_data['loan_value']
			interest = form.cleaned_data['interest']
			loan_monthly_payment = form.cleaned_data['loan_payment']

			fields_kwargs = {
				'owner': name,
				'loan': loan,
				'interest': interest,
				'loan_monthly_payment': loan_monthly_payment,
			}

			account_created = MortgageAccount(**fields_kwargs)
			number_payments = account_created.calc_number_periodic_payments

			context = {
				'name': name,
				'loan': loan,
				'interest': interest,
				'loan_monthly_payment': loan_monthly_payment,
				'number_payments_true': True,
				'number_payments': round(number_payments, 2),
			}
			return render(self.request, 'mortgage_calculator/totals.html', context)
