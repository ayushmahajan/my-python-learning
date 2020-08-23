class PayrollSystem:
    def calculate_payroll(self, employees):
        print("calculating payroll....")
        for employee in employees:
            print("Payroll for {} with id {}".format(employee.name, employee.id))
            print("Total pay is {}".format(employee.calculate_payroll()))


class Employee:
    def __int__(self, emp_id, name):
        self.id = emp_id
        self.name = name


class SalaryEmployee(Employee):
    def __int__(self, emp_id, name, weekly_salary):
        super().__int__(emp_id, name)
        self.weekly_salary = weekly_salary

    def calculate_payroll(self):
        return self.weekly_salary


class HourlyEmployee(Employee):
    def __int__(self, emp_id, name, hours_worked, hourly_rate):
        super().__int__(emp_id, name)
        self.hours_worked = hours_worked
        self.hourly_rate = hourly_rate

    def calculate_payroll(self):
        return self.hours_worked * self.hourly_rate


class CommissionEmployee(SalaryEmployee):
    def __int__(self, emp_id, name, weekly_salary, commission):
        super().__int__(emp_id, name, weekly_salary)
        self.commission = commission

    def calculate_payroll(self):
        fixed_salary = super().calculate_payroll()
        return fixed_salary + self.commission

