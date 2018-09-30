import math
import sys
from PyQt5 import QtWidgets, QtCore

class Calculator(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):                                                                          # Contains GUI

        self.display = QtWidgets.QLineEdit('0')                                                 # Display line
        self.display.setReadOnly(True)
        self.display.setAlignment(QtCore.Qt.AlignRight)
        self.display.setText('0')
        self.display.setStyleSheet(('QLineEdit {background-color: white; color: black;}'))

        self.num = 0.0
        self.oldnum = 0.0
        self.operatorPending = 'a'
        self.isOperatorPending = False


        self.zero = QtWidgets.QPushButton('0')                                                  # Defining digit buttons (0-9) and also pi and decimal point
        self.one = QtWidgets.QPushButton('1')
        self.two = QtWidgets.QPushButton('2')
        self.three = QtWidgets.QPushButton('3')
        self.four = QtWidgets.QPushButton('4')
        self.five = QtWidgets.QPushButton('5')
        self.six = QtWidgets.QPushButton('6')
        self.seven = QtWidgets.QPushButton('7')
        self.eight = QtWidgets.QPushButton('8')
        self.nine = QtWidgets.QPushButton('9')
        self.pieButton = QtWidgets.QPushButton(u'\u03A0')
        self.dotButton = QtWidgets.QPushButton('.')
        self.eButton = QtWidgets.QPushButton('e')
        self.zero.setStyleSheet(('QPushButton {background-color: white; color: black;}'))       # setting background colour and text colour
        self.one.setStyleSheet(('QPushButton {background-color: white; color: black;}'))
        self.two.setStyleSheet(('QPushButton {background-color: white; color: black;}'))
        self.three.setStyleSheet(('QPushButton {background-color: white; color: black;}'))
        self.four.setStyleSheet(('QPushButton {background-color: white; color: black;}'))
        self.five.setStyleSheet(('QPushButton {background-color: white; color: black;}'))
        self.six.setStyleSheet(('QPushButton {background-color: white; color: black;}'))
        self.seven.setStyleSheet(('QPushButton {background-color: white; color: black;}'))
        self.eight.setStyleSheet(('QPushButton {background-color: white; color: black;}'))
        self.nine.setStyleSheet(('QPushButton {background-color: white; color: black;}'))
        self.dotButton.setStyleSheet(('QPushButton {background-color: white; color: black;}'))
        self.zero.clicked.connect(self.digits)                                                  # connecting buttons to corresponding function (self.digit)
        self.one.clicked.connect(self.digits)
        self.two.clicked.connect(self.digits)
        self.three.clicked.connect(self.digits)
        self.four.clicked.connect(self.digits)
        self.five.clicked.connect(self.digits)
        self.six.clicked.connect(self.digits)
        self.seven.clicked.connect(self.digits)
        self.eight.clicked.connect(self.digits)
        self.nine.clicked.connect(self.digits)
        self.pieButton.clicked.connect(self.digits)
        self.dotButton.clicked.connect(self.digits)
        self.eButton.clicked.connect(self.digits)

        self.plusButton = QtWidgets.QPushButton(u'\u002B')                                                 # Defining basic operators
        self.minusButton = QtWidgets.QPushButton(u'\u002D')
        self.multiplyButton = QtWidgets.QPushButton(u'\u002A')
        self.divideButton = QtWidgets.QPushButton(u'\u00F7')
        self.equalButton = QtWidgets.QPushButton(u'\u003D')
        self.equalButton.setStyleSheet('QPushButton {background-color: orange; color: white;}')            # setting background colour and text colour
        self.plusButton.setStyleSheet(('QPushButton {background-color: #fdf6d6; color: black;}'))
        self.minusButton.setStyleSheet(('QPushButton {background-color: #fdf6d6; color: black;}'))
        self.multiplyButton.setStyleSheet(('QPushButton {background-color: #fdf6d6; color: black;}'))
        self.divideButton.setStyleSheet(('QPushButton {background-color: #fdf6d6; color: black;}'))
        self.plusButton.clicked.connect(self.operator)                                                     # Connecting basic operators to self.operator
        self.minusButton.clicked.connect(self.operator)
        self.multiplyButton.clicked.connect(self.operator)
        self.divideButton.clicked.connect(self.operator)
        self.equalButton.clicked.connect(self.equal)

        self.signChangeButton = QtWidgets.QPushButton(u'\u00B1')                                           # Defining more complex operators and functions
        self.sqrtButton = QtWidgets.QPushButton(u'\u221A')
        self.squareButton = QtWidgets.QPushButton(u"x\N{SUPERSCRIPT TWO}")
        self.inverseButton = QtWidgets.QPushButton('1/x')
        self.exponentialButton = QtWidgets.QPushButton('e^x')
        self.tenPowerButton = QtWidgets.QPushButton('10^x')
        self.sinButton = QtWidgets.QPushButton('sin')
        self.cosButton = QtWidgets.QPushButton('cos')
        self.tanButton = QtWidgets.QPushButton('tan')
        self.logButton = QtWidgets.QPushButton('log')
        self.signChangeButton.setStyleSheet(('QPushButton {background-color: white; color: black;}'))       # setting background colour and text colour
        self.sqrtButton.setStyleSheet(('QPushButton {background-color: #fdf6d6; color: black;}'))
        self.squareButton.setStyleSheet(('QPushButton {background-color: #fdf6d6; color: black;}'))
        self.inverseButton.setStyleSheet(('QPushButton {background-color: #fdf6d6; color: black;}'))
        self.exponentialButton.setStyleSheet(('QPushButton {background-color: #fdf6d6; color: black;}'))
        self.tenPowerButton.setStyleSheet(('QPushButton {background-color: #fdf6d6; color: black;}'))
        self.sinButton.setStyleSheet(('QPushButton {background-color: #fdf6d6; color: black;}'))
        self.cosButton.setStyleSheet(('QPushButton {background-color: #fdf6d6; color: black;}'))
        self.tanButton.setStyleSheet(('QPushButton {background-color: #fdf6d6; color: black;}'))
        self.logButton.setStyleSheet(('QPushButton {background-color: #fdf6d6; color: black;}'))
        self.eButton.setStyleSheet(('QPushButton {background-color: #fdf6d6; color: black;}'))
        self.pieButton.setStyleSheet(('QPushButton {background-color: #fdf6d6; color: black;}'))
        self.signChangeButton.clicked.connect(self.operator_adv)                                            # Linking these operators and mathematical function to self.operator_adv
        self.sqrtButton.clicked.connect(self.operator_adv)
        self.squareButton.clicked.connect(self.operator_adv)
        self.inverseButton.clicked.connect(self.operator_adv)
        self.exponentialButton.clicked.connect(self.operator_adv)
        self.tenPowerButton.clicked.connect(self.operator_adv)
        self.sinButton.clicked.connect(self.operator_adv)
        self.cosButton.clicked.connect(self.operator_adv)
        self.tanButton.clicked.connect(self.operator_adv)
        self.logButton.clicked.connect(self.operator_adv)



        self.clearButton = QtWidgets.QPushButton('CLR')                                                 # Additional buttons
        self.backspaceButton = QtWidgets.QPushButton('BACKSPC')
        self.backspaceButton.setStyleSheet(('QPushButton {background-color: #fdf6d6; color: black;}'))  # setting background colour and text colour
        self.clearButton.setStyleSheet(('QPushButton {background-color: #fdf6d6; color: black;}'))
        self.clearButton.clicked.connect(self.others)                                                   # Linking these buttons to self.others
        self.backspaceButton.clicked.connect(self.others)

        mainLayout = QtWidgets.QGridLayout()                                                            # Naming layout as main layout and setting it to Grid Layout
        mainLayout.setSpacing(1)
        #mainLayout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        #mainLayout.setSizeConstraint()
        #mainLayout.setSizeConstraint(QtWidgets.QtLaLayout.SetFixedSize)
        mainLayout.addWidget(self.display, 0, 0, 1, 5)                                                   # Adding different widgets defined above (display, buttons) to the grid
        mainLayout.addWidget(self.sqrtButton, 1, 0, 1, 1)
        mainLayout.addWidget(self.logButton, 1, 1, 1, 1)
        mainLayout.addWidget(self.sinButton, 1, 2, 1, 1)
        mainLayout.addWidget(self.cosButton, 1, 3, 1, 1)
        mainLayout.addWidget(self.tanButton, 1, 4, 1, 1)
        mainLayout.addWidget(self.tenPowerButton, 2, 0, 1, 1)
        mainLayout.addWidget(self.eButton, 2, 1, 1, 1)
        mainLayout.addWidget(self.clearButton, 2, 2, 1, 1)
        mainLayout.addWidget(self.backspaceButton, 2, 3, 1, 1)
        mainLayout.addWidget(self.plusButton, 2, 4, 1, 1)
        mainLayout.addWidget(self.squareButton, 3, 0, 1, 1)
        mainLayout.addWidget(self.seven, 3, 1, 1, 1)
        mainLayout.addWidget(self.eight, 3, 2, 1, 1)
        mainLayout.addWidget(self.nine, 3, 3, 1, 1)
        mainLayout.addWidget(self.minusButton, 3, 4, 1, 1)
        mainLayout.addWidget(self.inverseButton, 4, 0, 1, 1)
        mainLayout.addWidget(self.four, 4, 1, 1, 1)
        mainLayout.addWidget(self.five, 4, 2, 1, 1)
        mainLayout.addWidget(self.six, 4, 3, 1, 1)
        mainLayout.addWidget(self.multiplyButton, 4, 4, 1, 1)
        mainLayout.addWidget(self.exponentialButton, 5, 0, 1, 1)
        mainLayout.addWidget(self.one, 5, 1, 1, 1)
        mainLayout.addWidget(self.two, 5, 2, 1, 1)
        mainLayout.addWidget(self.three, 5, 3, 1, 1)
        mainLayout.addWidget(self.divideButton, 5, 4, 1, 1)
        mainLayout.addWidget(self.pieButton, 6, 0, 1, 1)
        mainLayout.addWidget(self.signChangeButton, 6, 1, 1, 1)
        mainLayout.addWidget(self.zero, 6, 2, 1, 1)
        mainLayout.addWidget(self.dotButton, 6, 3, 1, 1)
        mainLayout.addWidget(self.equalButton, 6, 4, 1, 1)


        mainLayout.hasHeightForWidth()
        self.setWindowTitle('Calculator')                               # Setting window title
        self.setLayout(mainLayout)
        app.setStyleSheet(('QtWidgets {background-colour: black}'))


        self.show()

    def digits(self):
        clickedButton = self.sender()                                               # extract information about button clicked
        digitClicked = str(clickedButton.text())

        if digitClicked == u'\u03A0':                                               # pi
            self.display.setText(str(math.pi))
            return
        elif digitClicked == 'e':                                                  # e
            self.display.setText(str(math.exp(1)))
        elif self.display.text() == '0' or self.display.text() == 'Math Error':     # display digit
            self.display.setText(digitClicked)
            return
        elif digitClicked == '.':                                                    # decimal point
            for i in self.display.text():
                if i == '.':
                    self.display.setText('Math Error')
                    return
            else:
                print('a'+self.display.text())
                self.display.setText(self.display.text() + '.')
                return
        else:
            self.display.setText(self.display.text() + digitClicked)
            return

    def operator(self):
        if str(self.display.text()) == "Math Error":        # if math error is display then clear memory and display 0
            self.num = 0.0
            self.oldnum = 0.0
            self.operatorPending = ''
            self.display.setText('0')
            return

        clickedButton = self.sender()
        clickedOperator = str(clickedButton.text())


        if self.isOperatorPending == False:                 # if no previous operator is pending then store clicked operator in memory and set operator pending as true
            self.oldnum = float(self.display.text())
            if clickedOperator == u'\u002B':                # addition
                self.display.setText('0')
                self.operatorPending = u'\u002B'
                self.isOperatorPending = True
            elif clickedOperator == u'\u002D':              # subtraction
                self.display.setText('0')
                self.operatorPending = u'\u002D'
                self.isOperatorPending = True
            elif clickedOperator == u'\u002A':              # multiply
                self.display.setText('0')
                self.operatorPending = u'\u002A'
                self.isOperatorPending = True
            elif clickedOperator == u'\u00F7':              # divide
                self.display.setText('0')
                self.operatorPending = u'\u00F7'
                self.isOperatorPending = True

        elif self.isOperatorPending == True:                # if operator is pending then calculate pending operation and update operator pending to true
            self.num = float(self.display.text())
            if self.operatorPending == u'\u002B':  # addition
                self.oldnum = self.num + self.oldnum
            elif self.operatorPending == u'\u002D':
                self.oldnum = self.oldnum - self.num
            elif self.operatorPending == u'\u002A':
                self.oldnum = self.num * self.oldnum
            elif self.operatorPending == u'\u00F7':
                if self.num == 0.0:
                    self.display.setText('Math Error')
                    return
                else:
                    self.oldnum = self.oldnum / self.num
            if clickedOperator == u'\u002B':                # addition
                self.display.setText('0')
                self.operatorPending = u'\u002B'
            elif clickedOperator == u'\u002D':              # subtraction
                self.display.setText('0')
                self.operatorPending = u'\u002D'
            elif clickedOperator == u'\u002A':              # multiply
                self.display.setText('0')
                self.operatorPending = u'\u002A'
            elif clickedOperator == u'\u00F7':              # divide
                self.display.setText('0')
                self.operatorPending = u'\u00F7'
        return

    def operator_adv(self):
        if str(self.display.text()) == "Math Error":                    # if math error is display then clear memory and display 0
            self.num = 0.0
            self.oldnum = 0.0
            self.operatorPending = ''
            self.display.setText('0')
            return

        clickedButton = self.sender()
        clickedOperator = str(clickedButton.text())
        result = float(self.display.text())

        if self.isOperatorPending == True:                             # if operator is pending then calculate pending operation and update operator pending to true
            self.num = float(self.display.text())
            if self.operatorPending == u'\u002B':  # addition
                self.oldnum = self.num + self.oldnum
            elif self.operatorPending == u'\u002D':
                self.oldnum = self.oldnum - self.num
            elif self.operatorPending == u'\u002A':
                self.oldnum = self.num * self.oldnum
            elif self.operatorPending == u'\u00F7':
                if self.num == 0.0:
                    self.display.setText('Math Error')
                    return
                else:
                    self.oldnum = self.oldnum / self.num
            self.isOperatorPending == False
            result = self.oldnum


        if clickedOperator == u'\u00B1':                                # sign change
            result = -result                                            # Still have to address problem about extra 0s in float
        elif clickedOperator == u'\u221A':                              # square root
            if result < 0:
                self.display.setText('Math Error')
                return
            else:
                result = math.sqrt(result)
        elif clickedOperator == u"x\N{SUPERSCRIPT TWO}":                # square
            result = result * result
        elif clickedOperator == '1/x':                                  # inverse
            if result == 0:
                self.display.setText('Math Error')
                return
            else:
                result = 1/result
        elif clickedOperator == 'e^x':                                  # exponential
            result = math.exp(result)
        elif clickedOperator == '10^x':                                 # power(10, x)
            result = pow(10, result)
        elif clickedOperator == 'sin':                                  # sin
            result = math.sin(result)
        elif clickedOperator == 'cos':                                  # cos
            result = math.cos(result)
        elif clickedOperator == 'tan':                                  # tan
            result = math.tan(result)
        elif clickedOperator == 'log':                                  # log
            if result <= 0:
                self.display.setText('Math Error')
                return
            else:
                result = math.log10(result)

        self.display.setText(str(result))
        return

    def equal(self):
        if str(self.display.text()) == "Math Error":         # if math error is display then clear memory and display 0
            self.num = 0.0
            self.oldnum = 0.0
            self.operatorPending = ''
            self.display.setText('0')
            return
        self.isOperatorPending = False                       # no operator will be pending after clicking equal
        self.num = float(self.display.text())
        if self.operatorPending == u'\u002B':                # addition
            self.num = self.num + self.oldnum
        elif self.operatorPending == u'\u002D':              # subtraction
            self.num = self.oldnum - self.num
        elif self.operatorPending == u'\u002A':              # multiply
            self.num = self.num * self.oldnum
        elif self.operatorPending == u'\u00F7':              # divide
            if self.num == 0:
                self.display.setText('Math Error')
                return
            else:
                self.num = self.oldnum/self.num
        self.display.setText(str(self.num))
        return

    def others(self):
        if str(self.display.text()) == "Math Error":                    # if math error is display then clear memory and display 0
            self.num = 0.0
            self.oldnum = 0.0
            self.operatorPending = ''
            self.display.setText('0')
            return
        clickedButton = self.sender()
        clickedOperator = str(clickedButton.text())

        if clickedOperator == 'CLR':                                    # clear memory and set display to 0
            self.num = 0.0
            self.oldnum = 0.0
            self.operatorPending = ''
            self.display.setText('0')
        elif clickedOperator == 'BACKSPC':                              # omit last digit except when math error( then it works like clear)
            if str(self.display.text()) == "Math Error":  # if math error is display then clear memory and display 0
                self.num = 0.0
                self.oldnum = 0.0
                self.operatorPending = ''
                self.display.setText('0')
                return
            self.display.setText(self.display.text()[:-1])
            if self.display.text() == '':
                self.display.setText('0')
        return

app = QtWidgets.QApplication(sys.argv)
a_window = Calculator()
sys.exit(app.exec_())