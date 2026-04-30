
from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_NUID_window(object):
    def setupUi(self, NUID_window):
        NUID_window.setObjectName("NUID_window")
        NUID_window.resize(434, 475)
        NUID_window.setMaximumSize(QtCore.QSize(438, 478))
        NUID_window.setStyleSheet("background-color: #b5b5e5; color: black;")
        self.centralwidget = QtWidgets.QWidget(parent=NUID_window)

        self.flower_top = QtWidgets.QLabel(parent=self.centralwidget)
        self.flower_top.setGeometry(QtCore.QRect(-110, -90, 621, 191))
        self.flower_top.setFont(QtGui.QFont("Bodoni Ornaments", 14))
        self.flower_top.setText("nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn")

        self.flower_top_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.flower_top_2.setGeometry(QtCore.QRect(-30, 220, 931, 381))
        self.flower_top_2.setFont(QtGui.QFont("Bodoni Ornaments", 14))
        self.flower_top_2.setText("nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn")

        self.Enter_NUID = QtWidgets.QPushButton(parent=self.centralwidget)
        self.Enter_NUID.setGeometry(QtCore.QRect(150, 220, 141, 51))
        self.Enter_NUID.setText("Enter")

        self.lineEdit = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(130, 120, 201, 61))
        self.lineEdit.setFont(QtGui.QFont("Arial", 24))
        self.lineEdit.setStyleSheet("background-color: white; color: black;")
        self.lineEdit.setText("ENTER NUID")

        NUID_window.setCentralWidget(self.centralwidget)



class Ui_Menu_window(object):
    def setupUi(self, Menu_window):
        Menu_window.setObjectName("Menu_window")
        Menu_window.resize(438, 478)
        Menu_window.setStyleSheet("background-color: #b5b5e5; color: black;")
        self.centralwidget = QtWidgets.QWidget(parent=Menu_window)

        self.Menu_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.Menu_label.setGeometry(QtCore.QRect(170, 40, 121, 31))
        self.Menu_label.setFont(QtGui.QFont("Euphemia UCAS", 36, QtGui.QFont.Weight.Bold))
        self.Menu_label.setText("MENU")

        font_btn = QtGui.QFont("Euphemia UCAS", 18, QtGui.QFont.Weight.Bold)
        style_btn = "QPushButton { background-color: #dde0fc; border: 1px solid #ababab; border-radius: 4px; } QPushButton:hover { background-color: white; border: 1px solid #8A2BE2; }"

        self.vote_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.vote_button.setGeometry(QtCore.QRect(130, 100, 191, 71))
        self.vote_button.setFont(font_btn)
        self.vote_button.setStyleSheet(style_btn)
        self.vote_button.setText("VOTE")

        # Swapped: End Voting is now middle (190), Edit is bottom (280)
        self.endvotoing_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.endvotoing_button.setGeometry(QtCore.QRect(130, 190, 191, 71))
        self.endvotoing_button.setFont(font_btn)
        self.endvotoing_button.setStyleSheet(style_btn)
        self.endvotoing_button.setText("END VOTING")

        self.edit_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.edit_button.setGeometry(QtCore.QRect(130, 280, 191, 71))
        self.edit_button.setFont(font_btn)
        self.edit_button.setStyleSheet(style_btn)
        self.edit_button.setText("EDIT")

        self.flower_top = QtWidgets.QLabel(parent=self.centralwidget)
        self.flower_top.setGeometry(QtCore.QRect(0, 0, 441, 20))
        self.flower_top.setFont(QtGui.QFont("Bodoni Ornaments", 14))
        self.flower_top.setText("nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn")

        self.flower_bottom = QtWidgets.QLabel(parent=self.centralwidget)
        self.flower_bottom.setGeometry(QtCore.QRect(0, 400, 441, 20))
        self.flower_bottom.setFont(QtGui.QFont("Bodoni Ornaments", 14))
        self.flower_bottom.setText("nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn")

        Menu_window.setCentralWidget(self.centralwidget)


class Ui_voting_window(object):
    def setupUi(self, voting_window):
        voting_window.setObjectName("voting_window")
        voting_window.resize(436, 478)
        voting_window.setStyleSheet("background-color:#b5b5e5;")
        self.centralwidget = QtWidgets.QWidget(parent=voting_window)

        self.candidates_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.candidates_label.setGeometry(QtCore.QRect(100, 30, 250, 40))
        self.candidates_label.setFont(QtGui.QFont("Euphemia UCAS", 20, QtGui.QFont.Weight.Bold))
        self.candidates_label.setText("CHOOSE ONE")
        self.candidates_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

        radio_style = "color: black; font-size: 16px; font-weight: bold;"
        self.radioone = QtWidgets.QRadioButton(parent=self.centralwidget);
        self.radioone.setGeometry(QtCore.QRect(130, 80, 200, 30));
        self.radioone.setStyleSheet(radio_style)
        self.radiotwo = QtWidgets.QRadioButton(parent=self.centralwidget);
        self.radiotwo.setGeometry(QtCore.QRect(130, 115, 200, 30));
        self.radiotwo.setStyleSheet(radio_style)
        self.radiothree = QtWidgets.QRadioButton(parent=self.centralwidget);
        self.radiothree.setGeometry(QtCore.QRect(130, 150, 200, 30));
        self.radiothree.setStyleSheet(radio_style)
        self.radiofour = QtWidgets.QRadioButton(parent=self.centralwidget);
        self.radiofour.setGeometry(QtCore.QRect(130, 185, 200, 30));
        self.radiofour.setStyleSheet(radio_style)
        self.radiofive = QtWidgets.QRadioButton(parent=self.centralwidget);
        self.radiofive.setGeometry(QtCore.QRect(130, 220, 200, 30));
        self.radiofive.setStyleSheet(radio_style)
        self.radiosix = QtWidgets.QRadioButton(parent=self.centralwidget);
        self.radiosix.setGeometry(QtCore.QRect(130, 255, 200, 30));
        self.radiosix.setStyleSheet(radio_style)

        self.submitvote_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.submitvote_button.setGeometry(QtCore.QRect(140, 340, 150, 50))
        self.submitvote_button.setText("SUBMIT VOTE")
        self.submitvote_button.setStyleSheet("background-color: #dde0fc; font-weight: bold; border-radius: 8px;")

        voting_window.setCentralWidget(self.centralwidget)


class Ui_edit_screen(object):
    def setupUi(self, edit_screen):
        edit_screen.setObjectName("edit_screen")
        edit_screen.resize(436, 477)
        edit_screen.setStyleSheet("background-color:#b5b5e5;")
        self.centralwidget = QtWidgets.QWidget(parent=edit_screen)

        self.Edit_header = QtWidgets.QLabel(parent=self.centralwidget)
        self.Edit_header.setGeometry(QtCore.QRect(50, 10, 351, 41))
        self.Edit_header.setFont(QtGui.QFont("Euphemia UCAS", 18, QtGui.QFont.Weight.Bold))
        self.Edit_header.setText("Enter 2 to 6 Candidates")

        le_style = "background-color: white; color: black;"
        self.can_one = QtWidgets.QLineEdit(parent=self.centralwidget);
        self.can_one.setGeometry(QtCore.QRect(100, 60, 250, 25));
        self.can_one.setStyleSheet(le_style)
        self.can_two = QtWidgets.QLineEdit(parent=self.centralwidget);
        self.can_two.setGeometry(QtCore.QRect(100, 95, 250, 25));
        self.can_two.setStyleSheet(le_style)
        self.can_three = QtWidgets.QLineEdit(parent=self.centralwidget);
        self.can_three.setGeometry(QtCore.QRect(100, 130, 250, 25));
        self.can_three.setStyleSheet(le_style)
        self.can_four = QtWidgets.QLineEdit(parent=self.centralwidget);
        self.can_four.setGeometry(QtCore.QRect(100, 165, 250, 25));
        self.can_four.setStyleSheet(le_style)
        self.can_five = QtWidgets.QLineEdit(parent=self.centralwidget);
        self.can_five.setGeometry(QtCore.QRect(100, 200, 250, 25));
        self.can_five.setStyleSheet(le_style)
        self.can_six = QtWidgets.QLineEdit(parent=self.centralwidget);
        self.can_six.setGeometry(QtCore.QRect(100, 235, 250, 25));
        self.can_six.setStyleSheet(le_style)

        num_style = "background-color: transparent; border: none; font-weight: bold;"
        self.n1 = QtWidgets.QLabel("1.", self.centralwidget);
        self.n1.setGeometry(QtCore.QRect(70, 60, 20, 25));
        self.n1.setStyleSheet(num_style)
        self.n2 = QtWidgets.QLabel("2.", self.centralwidget);
        self.n2.setGeometry(QtCore.QRect(70, 95, 20, 25));
        self.n2.setStyleSheet(num_style)
        self.n3 = QtWidgets.QLabel("3.", self.centralwidget);
        self.n3.setGeometry(QtCore.QRect(70, 130, 20, 25));
        self.n3.setStyleSheet(num_style)
        self.n4 = QtWidgets.QLabel("4.", self.centralwidget);
        self.n4.setGeometry(QtCore.QRect(70, 165, 20, 25));
        self.n4.setStyleSheet(num_style)
        self.n5 = QtWidgets.QLabel("5.", self.centralwidget);
        self.n5.setGeometry(QtCore.QRect(70, 200, 20, 25));
        self.n5.setStyleSheet(num_style)
        self.n6 = QtWidgets.QLabel("6.", self.centralwidget);
        self.n6.setGeometry(QtCore.QRect(70, 235, 20, 25));
        self.n6.setStyleSheet(num_style)

        self.submit_edit = QtWidgets.QPushButton(parent=self.centralwidget)
        self.submit_edit.setGeometry(QtCore.QRect(140, 340, 150, 50))
        self.submit_edit.setText("SUBMIT")
        self.submit_edit.setStyleSheet("background-color: #dde0fc; font-weight: bold;")

        edit_screen.setCentralWidget(self.centralwidget)


class Ui_Endvoting_window(object):
    def setupUi(self, Endvoting_window):
        Endvoting_window.setObjectName("Endvoting_window")
        Endvoting_window.resize(438, 478)
        Endvoting_window.setStyleSheet("background-color: #b5b5e5; color: black;")
        self.centralwidget = QtWidgets.QWidget(parent=Endvoting_window)

        # "Winner:" Label
        self.winner_label = QtWidgets.QLabel("Winner:", parent=self.centralwidget)
        self.winner_label.setGeometry(QtCore.QRect(90, 100, 100, 51))
        self.winner_label.setFont(QtGui.QFont("Arial", 18, QtGui.QFont.Weight.Bold))

        # Placeholder for the Winner's Name
        self.winner_candidate = QtWidgets.QLabel(parent=self.centralwidget)
        self.winner_candidate.setGeometry(QtCore.QRect(200, 110, 200, 31))
        self.winner_candidate.setFont(QtGui.QFont("Arial", 18))

        # "Votes:" Label
        self.votes_text = QtWidgets.QLabel("Votes:", parent=self.centralwidget)
        self.votes_text.setGeometry(QtCore.QRect(90, 160, 100, 51))
        self.votes_text.setFont(QtGui.QFont("Arial", 18, QtGui.QFont.Weight.Bold))

        # Placeholder for the Vote Count
        self.count_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.count_label.setGeometry(QtCore.QRect(200, 170, 200, 31))
        self.count_label.setFont(QtGui.QFont("Arial", 18))

        # New Return to Menu Button
        self.back_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.back_button.setGeometry(QtCore.QRect(120, 280, 200, 60))
        self.back_button.setText("RETURN TO MENU")

        # Styling the button to match your Menu design
        self.back_button.setFont(QtGui.QFont("Euphemia UCAS", 14, QtGui.QFont.Weight.Bold))
        self.back_button.setStyleSheet("""
            QPushButton { 
                background-color: #dde0fc; 
                border: 1px solid #ababab; 
                border-radius: 8px; 
            } 
            QPushButton:hover { 
                background-color: white; 
                border: 1px solid #8A2BE2; 
            }
        """)

        # Decorative flower labels (consistent with your other screens)
        self.flower_bottom = QtWidgets.QLabel(parent=self.centralwidget)
        self.flower_bottom.setGeometry(QtCore.QRect(0, 400, 441, 20))
        self.flower_bottom.setFont(QtGui.QFont("Bodoni Ornaments", 14))
        self.flower_bottom.setText("nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn")

        Endvoting_window.setCentralWidget(self.centralwidget)
