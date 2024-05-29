from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

from GenerationFunctions import *

class GeneratorWidget(QWidget):
	def __init__(self):
		super().__init__()
		self.initWindow()
		
	#Инициализация главного окна
	def initWindow(self):
		self.resize(800,450)
		self.setMinimumSize(800,450)
		self.setWindowTitle('Генерация текста')
		
		#Установка цвета окна
		pal = self.palette()
		pal.setColor(QPalette.Normal,
			     QPalette.Window,
			     QColor("orange"))
		pal.setColor(QPalette.Inactive,
			     QPalette.Window,
			     QColor("orange"))
		self.setPalette(pal)
		
		#Перемещение окна в центр монитора
		self.moveToCenter()
		#Инициализация виджетов окна
		self.initWidgets()
		
	#Инициализация виджетов окна
	def initWidgets(self):
		#Объявление виджетов окна.
		#self для того, чтобы к виджетам
		#можно было обратиться из других методов
		self.intputTextLabel = QLabel('Введите текст')
		self.outputTextLabel = QLabel('Сгенерированый текст')
		self.inputTextEdit = QTextEdit()
		self.outputTextEdit = QTextEdit()
		self.generateButton = QPushButton('Сгенерировать')
		
		#Присвоение родителя - чтобы виджеты
		#отображались в окне
		self.inputTextEdit.setParent(self)
		self.outputTextEdit.setParent(self)
		self.intputTextLabel.setParent(self)
		self.outputTextLabel.setParent(self)
		self.generateButton.setParent(self)
		
		#Размещение виджетов
		self.intputTextLabel.move(100,20)
		self.inputTextEdit.move(100,50)
		self.outputTextEdit.move(100,230)
		self.outputTextLabel.move(100,200)
		self.generateButton.move(300,160)
		
		#Установка размеров
		self.inputTextEdit.resize(600,100)
		self.outputTextEdit.resize(600,200)
		self.generateButton.resize(200,40)
		
		#Установка шрифта
		font=QFont()
		font.setPointSize(15)
		self.inputTextEdit.setFont(font)
		self.outputTextEdit.setFont(font)
		self.intputTextLabel.setFont(font)
		self.outputTextLabel.setFont(font)
		self.generateButton.setFont(font)
		
		#Добавление обработчика кнопки
		self.generateButton.clicked.connect(self.generate)
		
	#Перемещение окна в центр монитора
	def moveToCenter(self):
		windowGeom = self.frameGeometry()
		monitorCenter = QDesktopWidget().availableGeometry().center()
		windowGeom.moveCenter(monitorCenter)
		self.move(windowGeom.topLeft())
		
	#Обработчик нажатия кнопки "Сгенерировать"
	def generate(self):
		try:
			genT = generateText(self.inputTextEdit.toPlainText())
			self.outputTextEdit.setText(genT)
		except:
			print("Ошибка генерации")
		
		
