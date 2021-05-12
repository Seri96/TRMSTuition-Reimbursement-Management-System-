import unittest
from models.employee import Employee
from repository.employee_dao import EmployeeDAO
from repository.employee_dao_impl import EmployeeDAOImpl

# All DAO and Service methods must have a test proving that they work

employee_dao = EmployeeDAOImpl()

test_employee = Employee(0, 'TestFirstName', 'TestLastName',
                         'TestUsername', 'TestPassword', 'TestEmail', 1, 0)


class EmployeeTest(unittest.TestCase):

    def test_get_employee_by_id(self):
        retieved_employee = employee_dao.get_employee_by_id(
            test_employee.employee_id)
        assert test_employee.first_name == retieved_employee.first_name

    def test_update_reimbursement(self, cost):
        test_employee.reimbursement = 1000
        update_employee = employee_dao.update_reimbursement(
            test_employee, cost)
        assert update_employee.reimbursement == test_employee.reimbursement

    def test_get_username_password(self):
        retieved_employee = employee_dao.get_username_password(
            test_employee.username, test_employee.password)
        assert test_employee.username == retieved_employee.username
        assert test_employee.password == retieved_employee.password


if __name__ == '__main__':
    unittest.main()
