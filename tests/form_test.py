import unittest
from models.employee import Employee
from models.form import Form
from repository.form_dao import FormDAO
from repository.form_dao_impl import FormDAOImpl

form_dao = FormDAOImpl()
test_form = Form(0, 0, 'May', '9:00pm', 'testloc', 'testdesc', 100,
                 'testgrade', 'testtypeveent', 'justification', 1, 'testdenied')


class FormTest(unittest.TestCase):

    def test_create_form(self):
        new_form = form_dao.create_form(test_form)
        assert new_form.form_id != 0

    def test_get_form(self):
        retieved_form = form_dao.get_form_by_id(test_form.form_id)
        print(retieved_form.form_id)
        print(test_form.form_id)
        assert test_form.form_id == retieved_form.form_id

    def test_get_nonapproved_forms(self):
        form_dao.get_nonapproved_forms()
        assert test_form.is_approved == 1

    def test_update_form(self):
        test_form.is_approved = 2
        test_form.denied_reason = "N/A"
        update_form = form_dao.update_form(test_form)
        assert update_form.is_approved == test_form.is_approved
        assert update_form.denied_reason == test_form.denied_reason

    def test_delete_form(self):
        result = form_dao.delete_form(test_form.form_id)
        assert result == True
