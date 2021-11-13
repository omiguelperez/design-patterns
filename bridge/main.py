from abc import ABC, abstractmethod


class Payroll:
    """
    The Abstraction defines the interface for the "control" part of the two
    class hierarchies. It maintains a reference to an object of the
    Implementation hierarchy and delegates all of the real work to this object.
    """

    def __init__(self, implementation: 'YearlyPayrollPolicies') -> None:
        self.implementation = implementation

    def calculate_salary(self) -> str:
        return (f"Payroll: Base operation with:\n"
                f"{self.implementation.get_base_salary_from_external_sources()}")


class IntegralWithoutLimitPayroll(Payroll):
    """
    You can extend the Abstraction without changing the Implementation classes.
    """

    def calculate_salary(self) -> str:
        return (f"IntegralWithoutLimitPayroll: Extended operation with:\n"
                f"{self.implementation.get_base_salary_from_external_sources()}")


class YearlyPayrollPolicies(ABC):
    """
    The Implementation defines the interface for all implementation classes. It
    doesn't have to match the Abstraction's interface. In fact, the two
    interfaces can be entirely different. Typically the Implementation interface
    provides only primitive operations, while the Abstraction defines higher-
    level operations based on those primitives.
    """

    @abstractmethod
    def get_base_salary_from_external_sources(self) -> str:
        pass


class ConcreteYearlyPayrollPolicies2020(YearlyPayrollPolicies):
    def get_base_salary_from_external_sources(self) -> str:
        return "ConcreteYearlyPayrollPolicies2020: Here's the result on the platform 2020"


class ConcreteYearlyPayrollPolicies2021(YearlyPayrollPolicies):
    def get_base_salary_from_external_sources(self) -> str:
        return "ConcreteYearlyPayrollPolicies2021: Here's the result on the platform 2021"


def client_code(abstraction: Payroll) -> None:
    """
    Except for the initialization phase, where an Abstraction object gets linked
    with a specific Implementation object, the client code should only depend on
    the Abstraction class. This way the client code can support any abstraction-
    implementation combination.
    """
    print(abstraction.calculate_salary(), end="")


if __name__ == "__main__":
    """
    The client code should be able to work with any pre-configured abstraction-
    implementation combination.
    """

    payroll_policy_2020 = ConcreteYearlyPayrollPolicies2020()
    payroll_abstraction = Payroll(payroll_policy_2020)
    client_code(payroll_abstraction)

    print("\n")

    payroll_policy_2021 = ConcreteYearlyPayrollPolicies2021()
    integral_without_limit_payroll = IntegralWithoutLimitPayroll(payroll_policy_2021)
    client_code(integral_without_limit_payroll)
