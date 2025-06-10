from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column

PAYMENT_PERIOD_CHOICES = (
    ("12", "Monthly"),
    ("52", "Weekly"),
    ("365", "Daily"),
)


class BaseFormMortgage(forms.Form):
    name_account = forms.CharField(
        label="User account name:", help_text="Enter the Account Name", initial="joe"
    )
    loan_amount = forms.FloatField(help_text="Enter the loan amount", initial=100000)
    loan_interest = forms.FloatField(help_text="Enter the loan interest", initial=6)


class MortgageCalcForm(BaseFormMortgage):
    number_years_payment = forms.IntegerField(
        label="Number of years for payment:",
        help_text="Enter the time for payment(in years)",
        initial=30,
    )
    payment_period = forms.ChoiceField(
        help_text="Choose Payment Period Per Year",
        choices=PAYMENT_PERIOD_CHOICES,
        initial="monthly",
        widget=forms.Select(),
        required=True,
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column("name_account", css_class="form-group col-md-6 mb-0"),
                Column("loan_amount", css_class="form-group col-md-6 mb-0"),
                css_class="form-row",
            ),
            Row(
                Column("number_years_payment", css_class="form-group col-md-4 mb-0"),
                Column("loan_interest", css_class="form-group col-md-4 mb-0"),
                Column("payment_period", css_class="form-group col-md-4 mb-0"),
                css_class="form-row",
            ),
            Submit("totals", "Totals"),
            Submit("lists", "Get List"),
        )

        # Customize the help text and label for crispy forms
        for fieldname in [
            "name_account",
            "loan_amount",
            "number_years_payment",
            "loan_interest",
        ]:
            self.fields[fieldname].help_text = None


class MortgageCalcNumberPaymentsForm(BaseFormMortgage):
    loan_payment = forms.FloatField(
        help_text="Enter the monthly payment", initial=599.55
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column("name_account", css_class="form-group col-md-6 mb-0"),
                Column("loan_amount", css_class="form-group col-md-6 mb-0"),
                css_class="form-row",
            ),
            Row(
                Column("loan_interest", css_class="form-group col-md-6 mb-0"),
                Column("loan_payment", css_class="form-group col-md-6 mb-0"),
                css_class="form-row",
            ),
            Submit("totals", "Totals"),
        )

        # Customize the help text and label
        for fieldname in [
            "name_account",
            "loan_amount",
            "loan_interest",
            "loan_payment",
        ]:
            self.fields[fieldname].help_text = None
