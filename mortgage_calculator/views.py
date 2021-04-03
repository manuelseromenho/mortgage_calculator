from django.shortcuts import render
from django.views import View
from django.views.generic import FormView

from mortgage_calculator.forms import MortgageCalcForm, MortgageCalcNumberPaymentsForm
from mortgage_calculator.utils import MortgageAccount


class HomeView(View):
    def get(self, request):
        return render(request, 'mortgage_calculator/index.html')


class SubmitFormData(FormView):
    template_name = "mortgage_calculator/mortgage_calc.html"
    form_class = MortgageCalcForm

    def __init__(self, *args, **kargs):
        self.form = super(SubmitFormData, self).__init__(*args, **kargs)

    def form_valid(self, form):
        name = form.cleaned_data['name_account']
        loan_amount = form.cleaned_data['loan_amount']
        number_years_payment = form.cleaned_data['number_years_payment']
        loan_interest = form.cleaned_data['loan_interest']
        payment_period = int(form.cleaned_data['payment_period'])

        attributes = {
            'name': name,
            'loan_amount': loan_amount,
            'number_years_payment': number_years_payment,
            'loan_interest': loan_interest,
            'payment_period': payment_period,
        }

        if 'totals' in self.request.POST:

            account_created = MortgageAccount(**attributes)
            result = account_created.calc_loan_payment

            context = {
                'name': name,
                'loan_amount': loan_amount,
                'time': number_years_payment,
                'loan_interest': loan_interest,
                'payment_period': dict(form['payment_period'].field.choices).get(form['payment_period'].data),
                'number_payments_true': False,
                'result': round(result, 2),
            }
            return render(self.request, 'mortgage_calculator/totals.html', context)
        elif 'lists' in self.request.POST:

            account_created = MortgageAccount(**attributes)
            result = account_created.calc_loan_payment

            percent_interest = loan_interest / 100
            monthly_interest = (loan_amount * (percent_interest / payment_period))
            principal = (result - monthly_interest)
            ending_balance = loan_amount - principal
            total_interest = monthly_interest

            index = 1

            amortization_list = []

            starting_balance = loan_amount
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

    def __init__(self, *args, **kwargs):
        self.form = super(SubmitFormDataNumberPayments, self).__init__(*args, **kwargs)

    def form_valid(self, form):
        if 'totals' in self.request.POST:
            name = form.cleaned_data['name_account']
            loan_amount = form.cleaned_data['loan_amount']
            loan_interest = form.cleaned_data['loan_interest']
            loan_monthly_payment = form.cleaned_data['loan_payment']

            attributes = {
                'name': name,
                'loan_amount': loan_amount,
                'loan_interest': loan_interest,
                'loan_monthly_payment': loan_monthly_payment,
            }

            account_created = MortgageAccount(**attributes)
            if account_created.calc_number_periodic_payments:
                number_payments = account_created.calc_number_periodic_payments
            else:
                context = {
                    'error_math': 'Unfortunately the loan its not possible to be paid with this parameters',
                    'form': form,
                }
                return render(self.request, 'mortgage_calculator/mortgage_calc.html', context)

            context = {
                'name': name,
                'loan_amount': loan_amount,
                'loan_interest': loan_interest,
                'loan_monthly_payment': loan_monthly_payment,
                'number_payments_true': True,
                'number_payments': round(number_payments, 2),
            }
            return render(self.request, 'mortgage_calculator/totals.html', context)
