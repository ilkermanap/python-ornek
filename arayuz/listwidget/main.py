import sys

from PyQt5.QtWidgets import QApplication, QDialog
from ui_listwidget import Ui_ornek

class MainWindow(QDialog, Ui_ornek):
    def __init__(self, app=None):
        super(MainWindow, self).__init__()
        self.app = app
        self.secili = None
        self.setupUi(self)
        self.show()

    def btn_sil_basildi(self):
        templiste = []
        for i in  range(self.liste.count()):
            if i == self.secili:
                pass
            else:
                templiste.append(self.liste.item(i).text())
        self.liste.clear()
        self.edit_eleman.setText("")
        for eleman in templiste:
            self.liste.addItem(eleman)

    def list_eleman_tiklandi(self):
        self.secili = self.liste.currentRow()
        self.edit_eleman.setText(self.liste.item(self.secili).text())

    
    def btn_ekle_basildi(self):
        metin = self.edit_eleman.text().strip()
        if metin != "":
            durum = self.eleman_kontrol(metin)
            if durum == False:
                print(metin, " ekleyecegiz")
                self.liste.addItem(metin)
            else:
                print(metin, " zaten eklenmis")
        
    def eleman_kontrol(self, metin):
        eleman_sayisi = self.liste.count()
        if eleman_sayisi > 0:
            for ndx in range(eleman_sayisi):
                item = self.liste.item(ndx)
                if item.text() == metin:
                    return True
        return False
        
            
if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWin = MainWindow(app)
    ret = app.exec_()
    app.exit()
    sys.exit(ret)
