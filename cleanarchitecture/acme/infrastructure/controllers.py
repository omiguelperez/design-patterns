from acme.application import LoanContainer
from acme.domain.usecases.apply_credit_card import CreditCardApplicationRequest
from acme.domain.usecases.apply_loan import LoanApplicationRequest


def loan_apply():
    loan_apply_use_case = LoanContainer.loan_apply_use_case()
    request = LoanApplicationRequest(ssn="123-45-6789", amount=1000)
    response = loan_apply_use_case.execute(request)
    return response


def credit_card_apply():
    credit_card_apply_use_case = LoanContainer.credit_card_apply_use_case()
    request = CreditCardApplicationRequest(ssn="123-45-6789", amount=1000)
    response = credit_card_apply_use_case.execute(request)
    return response
