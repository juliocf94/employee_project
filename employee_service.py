import pandas as pd

from employee import Employee

class EmployeeService:

    def load_employees(self, path):

        dataframe = pd.read_excel(path)
        rows  = dataframe.iterrows()

        employees = []

        for index, row in rows:

            employee = Employee(
                row["id"],
                row["nombre"],
                row["salario"]
            )

            employees.append(employee)

        return employees

    def create_report(self, employees):

        report = []

        for employee in employees:

            report.append({
                "Id": employee.id_employee,
                "Nombre": employee.name,
                "Salario Mensual": employee.salary,
                "Salario Anual": employee.annual_salary(),
                "Salario Alto": employee.is_high_salary()
            })

        return pd.DataFrame(report)