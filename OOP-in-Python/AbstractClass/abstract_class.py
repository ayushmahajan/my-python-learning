"""
This is an example of demonstrating what is an Abstract class and the use of Abstract class.
"""

import Inheritance_and_Composition as ic


def main():
    salaryEmployee = ic.SalaryEmployee(1, "Ayush", 1200)
    commissionEmployee = ic.CommissionEmployee(2, "John", 1200, 120)
    # Instance of Employee class --> uncomment it to understand the issue
    # genericEmployee = ic.Employee(3, "Tim")
    """
    When we create a genericEmployee of type Employee and we try to calculate its payroll,
    we get AttributeError: 'Employee' object has no attribute 'calculate_payroll'.
    
    And this happens because of the simple reason that the Employee class doesn't implement the
    calculate_payroll() method.
    
    But this was the intention behind the Employee class that it should be used to create other
    special classes like the SalaryEmployee, HourlyEmployee, etc.
    
    Employee class is basically an abstract class. It should not be instantiated directly.
    It should be used as Base class to create Derived classes.
    """
    employeeList = [salaryEmployee, commissionEmployee]  # , genericEmployee] --> uncomment to understand
    payrollSystem = ic.PayrollSystem()
    payrollSystem.calculate_payroll(employeeList)


if __name__ == "__main__":
    main()
