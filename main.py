import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from connection import connect_to_db
from PyQt5 import uic
from personal_date import EditForm

class EmployeeForm(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("untitled.ui", self)
        self.pushButton.clicked.connect(self.load_data_from_database)
        self.pushButton_2.clicked.connect(self.personal_date)
        self.comboBox.currentTextChanged.connect(self.chees_Dc())


    def load_data_from_database(self):
        conn = connect_to_db()
        cursor = conn.cursor()

        select_query = "SELECT day_week, start, finish, break FROM shedule "
        cursor.execute(select_query)
        data = cursor.fetchall()

        self.tableWidget.setRowCount(0)
        for row_num, row_data in enumerate(data):
            self.tableWidget.insertRow(row_num)
            for col_num, col_data in enumerate(row_data):
                item = QTableWidgetItem(str(col_data))
                self.tableWidget.setItem(row_num, col_num, item)

        cursor.close()
        conn.close()

    def personal_date(self):

        self.personal_date = EditForm()
        self.personal_date.show()

    def chees_Dc(self,doctor_name):
        conn = connect_to_db()
        cursor = conn.cursor()
        print(doctor_name)
        select_query = f"SELECT day_week, start, finish, break FROM shedule JOIN doctors " \
                       f"on doctors.id=shedule.id_doctor and doctors.name = '{doctor_name}'"
        cursor.execute(select_query)
        data = cursor.fetchall()

        self.tableWidget.setRowCount(0)
        for row_num, row_data in enumerate(data):
            self.tableWidget.insertRow(row_num)
            for col_num, col_data in enumerate(row_data):
                item = QTableWidgetItem(str(col_data))
                self.tableWidget.setItem(row_num, col_num, item)

        cursor.close()
        conn.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = EmployeeForm()
    form.show()
    sys.exit(app.exec_())
