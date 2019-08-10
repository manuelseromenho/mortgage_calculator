from django.shortcuts import render
from django.views.generic import FormView

from mortgage_calculator.forms import MortgageCalcForm

from mortgage_calculator.utils import MortgageAccount

#https://developer.mozilla.org/pt-BR/docs/Learn/Server-side/Django/Forms

"""
Mortgage Calculator - Calculate the monthly payments of a fixed term mortgage over given Nth terms at a given interest 
rate. Also figure out how long it will take the user to pay back the loan. For added complexity, add an option for users 
to select the compounding interval (Monthly, Weekly, Daily, Continually).
"""


class SubmitFormData(FormView):
	template_name = "mortgage_calculator/index.html"
	form_class = MortgageCalcForm

	def form_valid(self, form):
		if 'totals' in self.request.POST:
			name = form.cleaned_data['name_account']
			loan = form.cleaned_data['loan_value']
			number_years_payment = form.cleaned_data['number_years_payment']
			interest = form.cleaned_data['interest']

			account_created = MortgageAccount(name, loan, number_years_payment, interest)
			result = account_created.calc_loan_payment

			context = {
				'name': name,
				'loan': loan,
				'time': number_years_payment,
				'interest': interest,
				'result': round(result, 2),
			}
			return render(self.request, 'mortgage_calculator/totals.html', context)
		elif 'lists' in self.request.POST:
			name = form.cleaned_data['name_account']
			loan = form.cleaned_data['loan_value']
			number_years_payment = form.cleaned_data['number_years_payment']
			interest = form.cleaned_data['interest']

			account_created = MortgageAccount(name, loan, number_years_payment, interest)
			result = account_created.calc_loan_payment

			percent_interest = interest / 100
			monthly_interest = (loan * (percent_interest / 12))
			principal = (result - monthly_interest)
			ending_balance = loan - principal
			total_interest = monthly_interest

			index = 1

			amortization_list = []

			starting_balance = loan
			while (starting_balance - result) > 0:
				if index > 1:
					starting_balance = ending_balance
				monthly_interest = starting_balance * (percent_interest / 12)
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





"""
def home(request):

	if request.method == 'POST' and 'totals' in request.POST:
		form = MortgageCalcForm(request.POST)

		if form.is_valid():
			name = form.cleaned_data['name_account']
			loan = form.cleaned_data['loan_value']
			number_years_payment = form.cleaned_data['number_years_payment']
			interest = form.cleaned_data['interest']

			account_created = MortgageAccount(name, loan, number_years_payment, interest)
			result = account_created.calc_loan_payment

			context = {
				'name': name,
				'loan': loan,
				'time': number_years_payment,
				'interest': interest,
				'result': round(result, 2),
			}

			return render(request, 'main/totals.html', context)

	elif request.method == 'POST' and 'lists' in request.POST:
		form = MortgageCalcForm(request.POST)

		if form.is_valid():
			name = form.cleaned_data['name_account']
			loan = form.cleaned_data['loan_value']
			number_years_payment = form.cleaned_data['number_years_payment']
			interest = form.cleaned_data['interest']

			account_created = MortgageAccount(name, loan, number_years_payment, interest)
			result = account_created.calc_loan_payment

			percent_interest = interest / 100
			monthly_interest = (loan * (percent_interest / 12))
			principal = (result - monthly_interest)
			ending_balance = loan - principal
			total_interest = monthly_interest

			index = 1

			amortization_list = []

			starting_balance = loan
			while (starting_balance - result) > 0:
				if index > 1:
					starting_balance = ending_balance
				monthly_interest = starting_balance * (percent_interest / 12)
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

			return render(request, 'main/loan_amortization.html', context)
	else:
		form = MortgageCalcForm()

		context = {
			'form': form,
		}
		
	return render(request, 'main/index.html', context)

"""