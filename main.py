from employee_service import EmployeeService

service = EmployeeService()

employees = service.load_employees("employee.xlsx")

report = service.create_report(employees)

report.to_excel("employee_report.xlsx", index=False)

print(report)