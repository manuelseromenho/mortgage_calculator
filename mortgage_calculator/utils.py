from math import log10

# https://brownmath.com/bsci/loan.htm#Derive3


class MortgageAccount:

	def __init__(self, owner="nobody", loan=0, number_years_payment=0, interest=0, loan_payment=0):
		self.owner = owner
		self.loan = loan
		self.number_years_payment = number_years_payment
		self.interest = interest
		self.loan_payment = loan_payment

	@property
	def periodic_interest_rate(self):
		return (self.interest/100)/12

	@property
	def number_periodic_payments(self):
		return self.number_years_payment*12

	@property
	def discount_factor(self):
		return (((1+self.periodic_interest_rate)**self.number_periodic_payments)-1)/(self.periodic_interest_rate*(1+self.periodic_interest_rate)**self.number_periodic_payments)

	@property
	def calc_loan_payment(self):
		loan_payment = self.loan/self.discount_factor
		return loan_payment

	@property
	def calc_number_periodic_payments(self):
		N1 = -log10(1-(self.interest*self.loan)/self.loan_payment)
		N2 = log10(1+self.interest)
		return N1/N2

	def __str__(self):
		return f"{self.owner}"
