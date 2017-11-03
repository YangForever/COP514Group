import sys,OFB_main as OFB,OFB_readFile as readFile,ECB_main as ECB,CTRmain as CTR,CBC_main as CBC,CFB_main as CFB,gui_readpic as readpic
from PIL import Image
from tkMessageBox import *
from PyQt4 import QtCore, QtGui, uic

qtCreatorFile = "dialog.ui"

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
 
class MyApp(QtGui.QMainWindow, Ui_MainWindow):

    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.btn_ECB.clicked.connect(self.startECBFun)
        self.btn_CFB.clicked.connect(self.startCFBFun)
        self.btn_OFB.clicked.connect(self.startOFBFun)
        self.btn_CTR.clicked.connect(self.startCTRFun)
        self.btn_CBC.clicked.connect(self.startCBCFun)
        self.btn_encryption.clicked.connect(self.startEncryption)
        self.btn_decryption.clicked.connect(self.startDecryption)
        self.btn_start.clicked.connect(self.start)
        self.btn_reset.clicked.connect(self.reset)
        self.btn_readfile.clicked.connect(self.readFile)
        self.btn_readpic.clicked.connect(self.readPic)
        # self.btn_showpic.clicked.connect(self.showPic)
        self.text_count.setDisabled(True)
        self.text_iv.setDisabled(True)
        self.btn_start.setDisabled(True)
        self.btn_readfile.setDisabled(True)

    mode = 0
    status = 0

    def readPic(self):
        self.fileDialog = QtGui.QFileDialog(self)
        file_name = self.fileDialog.getOpenFileName()
        pic_pix = readpic.readPic(file_name)
        self.text_plaintext.setText(pic_pix)


    def readFile(self):
        self.fileDialog = QtGui.QFileDialog(self)
        file_name = self.fileDialog.getOpenFileName()
        if self.status == 0:
            all_textAsc,all_text = readFile.readFile(str(file_name),self.status)
            self.text_plaintext.setText(all_text)
        else:
            all_text = readFile.readFile(str(file_name),self.status)
            self.text_ciphertext.setText(all_text)

    def startECBFun(self):
         self.label_disMode.setText("Current Mode:ECB")
         self.text_count.setDisabled(True)
         self.text_iv.setDisabled(True)
         self.mode = 1
    def startCFBFun(self):
         self.label_disMode.setText("Current Mode:CFB")
         self.text_iv.setDisabled(False)
         self.text_count.setDisabled(True)
         self.mode = 2
    def startOFBFun(self):
         self.label_disMode.setText("Current Mode:OFB")
         self.text_iv.setDisabled(False)
         self.text_count.setDisabled(True)
         self.mode = 3
    def startCTRFun(self):
         self.label_disMode.setText("Current Mode:CTR")
         self.text_count.setDisabled(False)
         self.text_iv.setDisabled(True)
         self.mode = 4
    def startCBCFun(self):
         self.label_disMode.setText("Current Mode:CBC")
         self.text_iv.setDisabled(False)
         self.text_count.setDisabled(True)
         self.mode = 5
    def startEncryption(self):
        self.status = 0
        self.btn_start.setDisabled(False)
        self.btn_readfile.setDisabled(False)
    def startDecryption(self):
        self.status = 1
        self.btn_start.setDisabled(False)
        self.btn_readfile.setDisabled(False)
    def start(self):
        self.btn_start.setDisabled(True)
        self.btn_encryption.setDisabled(True)
        self.btn_decryption.setDisabled(True)
        self.btn_readfile.setDisabled(True)
        cipherkey = str(self.text_key.toPlainText())
        if self.mode ==0:
            print 'error'
        elif self.mode == 1:
            if self.status == 0:
                plaintext = str(self.text_plaintext.toPlainText())
                ciphertext = ECB.Encryptionmain(plaintext,cipherkey)
                self.text_ciphertext.setText(ciphertext)
            else:
                print 'start'
                ciphertext = str(self.text_ciphertext.toPlainText())
                r_plaintext = ECB.Decryptionmain(ciphertext,cipherkey)
                self.text_plaintext.setText(r_plaintext)
        elif self.mode == 2:
            initialtext = str(self.text_iv.toPlainText())
            if self.status == 0:
                plaintext = str(self.text_plaintext.toPlainText())
                ciphertext = CFB.main(plaintext,initialtext,cipherkey,0)
                self.text_ciphertext.setText(ciphertext)
            else:
                print 'start'
                ciphertext = str(self.text_ciphertext.toPlainText())
                r_plaintext = CFB.main(ciphertext,initialtext,cipherkey,1)
                self.text_plaintext.setText(r_plaintext)
        elif self.mode == 3:    
            initialtext = str(self.text_iv.toPlainText())
            if self.status == 0:
                plaintext = str(self.text_plaintext.toPlainText())
                ciphertext = OFB.encryptionMain(plaintext,initialtext,cipherkey)
                self.text_ciphertext.setText(ciphertext)
            else:
                print 'start'
                ciphertext = str(self.text_ciphertext.toPlainText())
                r_plaintext = OFB.decryptionMain(ciphertext,initialtext,cipherkey)
                self.text_plaintext.setText(r_plaintext)
        elif self.mode == 4:
            count = str(self.text_count.toPlainText())
            if self.status == 0:
                plaintext = str(self.text_plaintext.toPlainText())
                ciphertext = CTR.main(count,plaintext,cipherkey)
                self.text_ciphertext.setText(ciphertext)
            else:
                print 'start'
                ciphertext = str(self.text_ciphertext.toPlainText())
                r_plaintext = CTR.main1(count,ciphertext,cipherkey)
                print r_plaintext
                self.text_plaintext.setText(r_plaintext)
        else:
            initialtext = str(self.text_iv.toPlainText())
            if self.status == 0:
                plaintext = str(self.text_plaintext.toPlainText())
                ciphertext = CBC.main_en(plaintext,initialtext,cipherkey)
                self.text_ciphertext.setText(ciphertext)
            else:
                print 'start'
                ciphertext = str(self.text_ciphertext.toPlainText())
                r_plaintext = CBC.main_de(ciphertext,initialtext,cipherkey)
                print r_plaintext
                self.text_plaintext.setText(r_plaintext)

    def reset(self):
        self.text_count.setDisabled(True)
        self.text_iv.setDisabled(True)
        self.btn_start.setDisabled(True)
        self.text_plaintext.setText('')
        self.text_ciphertext.setText('')
        self.text_key.setText('')
        self.text_iv.setText('')
        self.text_count.setText('')
        self.btn_encryption.setDisabled(False)
        self.btn_decryption.setDisabled(False)


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())