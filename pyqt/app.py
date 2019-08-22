import sys
from PyQt5.QtWidgets import QDialog, QApplication
from pyqt import Ui_Form

class AppWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.ui=Ui_Form()
        self.ui.setupUi(self)
        self.ui.textBrowser.setText("輸入為圖騰左上點座標\n 輸出為圖騰中心座標\n 行列數包含畫面外圖騰")
        self.ui.pushButton.clicked.connect(self.pushButton_Click)
        self.show()

    def calcSymbolPos(self):    
        w=int(self.ui.symbolWidth.text())
        h = int(self.ui.symbolHeight.text())
        x=int(self.ui.initxPos.text())
        y=int(self.ui.inityPos.text())
        col=int(self.ui.col.text())
        row=int(self.ui.row.text())
        for j in range(row):
            for i in range(col):
                # print('- +'{'+'x: {}, y:{}'+' }'.format((x+w*j),(y+h*i)))
                self.ui.textBrowser.append("  - {x: "+ str(x+w*i)+", y: "+str(y+h*j)+"}")
                # print("- {x:"+ str(x+w*j)+", y:"+str(y+h*i)+"}")
            self.ui.textBrowser.append("")
    def pushButton_Click(self):
        # self.ui.label.setText("Hello World")
        self.ui.textBrowser.setText("輸入為圖騰左上點座標\n 輸出為圖騰中心座標\n 行列數包含畫面外圖騰")
        self.calcSymbolPos()
        # self.ui.textBrowser.append("test")

app=QApplication(sys.argv)
w=AppWindow()
w.show()
sys.exit(app.exec_())
