import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QGraphicsScene, QGraphicsView, QSizePolicy
from PyQt5.uic import loadUi
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt



class MyMainWindow(QMainWindow):
    def __init__(self):
        super(MyMainWindow, self).__init__()
        self.initUI()

    def initUI(self):
        # 使用loadUi加载UI文件
        loadUi(r'E:\IVAN\pyQT_ui\mainForm.ui', self)

        # 为每个按钮连接独立的槽函数
        self.pushButton1.clicked.connect(self.onButtonClick1)
        self.pushButton2.clicked.connect(self.onButtonClick2)
        # 继续添加更多按钮...

        # Matplotlib初始化
        self.figure, self.ax = plt.subplots()
        self.canvas = FigureCanvas(self.figure)
        self.canvas.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)  # Set size policy
        self.scene = QGraphicsScene(self)
        self.scene.addWidget(self.canvas)
        self.graphicsView.setScene(self.scene)

    def resizeEvent(self, event):
        # Resize the Matplotlib plot when the main window is resized
        self.canvas.setGeometry(0, 0, self.graphicsView.width(), self.graphicsView.height())
        self.ax.set_position([0.1, 0.1, 0.8, 0.8])  # Adjust plot position within the figure
        self.canvas.draw()

    def onButtonClick1(self):
        # 处理按钮1点击事件
        print("Button 1 Clicked!")

        # Matplotlib绘制XY曲线图
        x = [1, 2, 3, 4, 5]
        y = [2, 4, 1, 6, 3]
        self.ax.plot(x, y)
        self.canvas.draw()

    def onButtonClick2(self):
        # 处理按钮2点击事件
        print("Button 2 Clicked!")
        # 继续添加更多槽函数...

        # 清除Matplotlib图形
        self.ax.clear()
        self.canvas.draw()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = MyMainWindow()
    mainWin.show()
    sys.exit(app.exec_())
