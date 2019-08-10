
class MortgageAccount:

	def __init__(self, owner, loan, number_years_payment, interest):
		self.owner = owner
		self.loan = loan
		self.number_years_payment = number_years_payment
		self.interest = interest

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

	def __str__(self):
		return f"{self.owner}"