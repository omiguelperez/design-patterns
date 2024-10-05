from acme.application import LoanContainer
from acme.domain.usecases.apply_loan import LoanApplicationRequest


def loan_apply():
    loan_apply_use_case = LoanContainer.loan_apply_use_case()
    request = LoanApplicationRequest(name="John Doe", amount=1000)
    response = loan_apply_use_case.execute(request)
    return response
