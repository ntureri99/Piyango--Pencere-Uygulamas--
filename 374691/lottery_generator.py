#bağlantı modülleri
 
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout
from random import randint
app = QApplication([])
 
# ana pencere:
my_win = QWidget()
my_win.setWindowTitle('Lottery')
my_win.move(100, 100)  # ekran neree gözükecek
my_win.resize(400, 400) # ekran boyutu

# pencere widget'ları: düğme ve etiket
button = QPushButton('Try your luck') # şansınızı deneyiniz butonu
text = QLabel('Click to participate') # katılamk i.çin tıklayınız etiketi
number1 = QLabel('?')  # 1. ragele sayı
number2 = QLabel('?') # 2. rasgele sayı 

# widget anahattı
line = QVBoxLayout()
line.addWidget(text, alignment = Qt.AlignCenter) # metin yazacak
line.addWidget(number1, alignment = Qt.AlignCenter)  # 1.sayı
line.addWidget(number2, alignment = Qt.AlignCenter)  # sayı 2
line.addWidget(button, alignment = Qt.AlignCenter)  # pusbutton şansınızı deneyiniz
my_win.setLayout(line)
 
# bir sayı üreten ve görüntüleyen işlev
def start_lottery():
    n1 = randint(0, 9) # 2 tane ratgele sayı
    n2 = randint(0, 9)
    number1.setText(str(n1)) #sayısı metine dönüştürdüm
    number2.setText(str(n2))
    if n1 == n2:  # 2 sayı birbirine eşitse
        text.setText('Kazandınız! Tekrar oynayınız')
    else:
        text.setText('Kaybettiniz! Tekrar oynayınız')
 
# düğme tıklama işleme
button.clicked.connect(start_lottery)

my_win.show() # ana pencere gözüksün
app.exec_() # uygulama başsın diye