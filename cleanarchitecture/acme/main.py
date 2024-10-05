from acme.infrastructure.controllers import credit_card_apply, loan_apply

if __name__ == "__main__":
    print("-------------------------")

    print("Applying for a loan...")
    response = loan_apply()
    print(response)
    print("Loan application completed.")

    print("-------------------------")

    print("Applying for a credit card...")
    response = credit_card_apply()
    print(response)
    print("Credit card application completed.")

    print("-------------------------")

    print("Applying for a credit card...")
    response = credit_card_apply()
    print(response)
    print("Credit card application completed.")

    print("-------------------------")
