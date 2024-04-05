import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QDialog

from queries import update_login_password


class EditForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi("personal_date.ui", self)
        self.pushButton.clicked.connect(self.edit_data)

    def edit_data(self):
        new_login = self.ui.lineEdit.text()
        new_password = self.ui.lineEdit_2.text()


        user_id = 1

        update_login_password(user_id, new_login, new_password)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    edit_form = EditForm()
    edit_form.show()
    sys.exit(app.exec_())
