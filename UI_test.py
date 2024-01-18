from PyQt5 import QtWidgets, uic, QtGui
import sys

# 加载UI文件
Ui_MainWindow, QMainWindow = uic.loadUiType(r'E:\yfgu_workspace\建模提参\自研建模工具及经验积累\codes\PYTHON_UI\UI_20240117.ui')


class MyWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setupUi(self)

        # Set window icon
        icon = QtGui.QIcon(r"E:\yfgu_workspace\myicon\tool-box.png")  # Replace with the path to your icon file
        self.setWindowIcon(icon)

        # Connect btn_import_setting button to custom method
        self.btn_import_setting.clicked.connect(self.import_settings)

        # Connect btn_simulate button to custom method
        self.btn_simulate.clicked.connect(self.simulate)

        # Initialize class attributes
        self.parallel_num = ""
        self.simulator_select = ""
        self.simulate_option = ""
        self.optimize_select = ""
        self.optimize_max_num = ""
        self.loss_goal = ""
        self.device_name = ""
        self.taskflow_path = ""
        self.ini_model_path = ""
        self.silicon_data_path = ""
        self.parameter_shift_path = ""
        self.simulate_speed = ""
        self.show_print = False
        self.save_png = False
        self.optimize_algorithm = ""
        self.optimize_popsize = ""
        self.save_loss_log = False

    def import_settings(self):
        # Get values from QComboBox and QLineEdit widgets
        self.parallel_num = self.cb_parallel_num.currentText()
        self.simulator_select = self.cb_simulator_select.currentText()
        self.simulate_option = self.cb_simulate_option.currentText()
        self.optimize_select = self.cb_optimize_select.currentText()
        self.optimize_max_num = self.txt_optimize_iter.text()
        self.loss_goal = self.txt_loss_goal.text()
        self.device_name = self.txt_device_name.text()
        self.taskflow_path = self.txt_taskflow.text()
        self.ini_model_path = self.txt_ini_model.text()
        self.silicon_data_path = self.txt_silicon_data.text()
        self.parameter_shift_path = self.txt_parameter_shift.text()
        self.simulate_speed = self.cb_simulate_option_2.currentText()
        self.show_print = self.cb_show_print.isChecked()
        self.save_png = self.cb_save_png.isChecked()
        self.optimize_algorithm = self.cb_optimize_select.currentText()
        self.optimize_popsize = self.txt_optimize_popsize.text()
        self.save_loss_log = self.cb_save_loss_log.isChecked()

        # Set fixed size for the main window
        self.setFixedSize(self.size())

        # Print or use the values as needed
        print("Settings Imported:")
        print("Parallel Num:", self.parallel_num)
        print("Simulator Select:", self.simulator_select)
        print("Simulate Option:", self.simulate_option)
        print("Optimize Select:", self.optimize_select)
        print("Optimize Max Num:", self.optimize_max_num)
        print("Loss Goal:", self.loss_goal)
        print("Device Name:", self.device_name)
        print("Taskflow Path:", self.taskflow_path)
        print("Ini-model Path:", self.ini_model_path)
        print("Silicon-data Path:", self.silicon_data_path)
        print("Parameters Shift Path:", self.parameter_shift_path)
        print("Simulate Speed:", self.simulate_speed)
        print("Show Print:", self.show_print)
        print("Save PNG:", self.save_png)
        print("Optimize Algorithm:", self.optimize_algorithm)
        print("Optimize Popsize:", self.optimize_popsize)
        print("Save Loss Log:", self.save_loss_log)

    def simulate(self):
        # Add your simulation logic here
        print("Simulation Button Clicked")
        # You can perform any actions related to simulation here


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())


