from math import log


class MortgageAccount:

	def __init__(self, **kwargs):

		self.name = kwargs.get('name', 'nobody')
		self.loan_amount = kwargs.get('loan_amount', 0)
		self.number_years_payment = kwargs.get('number_years_payment', 0)
		self.loan_interest = kwargs.get('loan_interest', 0)
		self.loan_monthly_payment = kwargs.get('loan_monthly_payment', 0)
		self.payment_period = kwargs.get('payment_period', 12)

	@property
	def periodic_interest_rate(self):
		return (self.loan_interest / 100) / self.payment_period

	@property
	def number_periodic_payments(self):
		return self.number_years_payment*self.payment_period

	@property
	def discount_factor(self):
		discount_factor_numerator = (((1+self.periodic_interest_rate)**self.number_periodic_payments)-1)
		discount_factor_divisor = (
				self.periodic_interest_rate*(1+self.periodic_interest_rate)**self.number_periodic_payments
		)
		return discount_factor_numerator/discount_factor_divisor

	@property
	def calc_loan_payment(self):
		loan_payment = self.loan_amount / self.discount_factor
		return loan_payment

	@property
	def calc_number_periodic_payments(self):
		"""Calculates the number of periodic payments with loan interest, loan amount and loan monthly payment

		Parameters:
		loan_interest
		loan_amount
		loan_monthly_payment

		Returns:
		number_periodic_payments
		"""
		interest_percent = self.loan_interest * 0.01
		try:
			N1 = -log(1 - interest_percent * self.loan_amount / (self.loan_monthly_payment * 12))
			N2 = log(1+interest_percent)
			number_periodic_payments = (N1/N2)*12
			return number_periodic_payments
		except ValueError:
			return None

	def __str__(self):
		return f"{self.name}"
