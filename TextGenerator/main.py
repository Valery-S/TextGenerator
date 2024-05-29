import sys
from GeneratorWidget import *

if __name__ == '__main__':
	app=QApplication([])
	w=GeneratorWidget()
	w.show()
	sys.exit(app.exec_())
