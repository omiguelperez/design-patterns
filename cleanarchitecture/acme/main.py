from json import dumps

from acme.infrastructure.controllers import credit_card_apply, loan_apply
from fastapi.encoders import jsonable_encoder


def print_json(data):
    print(dumps(jsonable_encoder(data), indent=2, default=str))


if __name__ == "__main__":
    print("-------------------------")

    print("Applying for a loan...")
    response = loan_apply()
    print_json(response)
    print("Loan application completed.")

    print("-------------------------")

    print("Applying for a credit card...")
    response = credit_card_apply()
    print_json(response)
    print("Credit card application completed.")

    print("-------------------------")

    print("Applying for a credit card...")
    response = credit_card_apply()
    print_json(response)
    print("Credit card application completed.")

    print("-------------------------")
