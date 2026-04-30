
import csv
import os
from PyQt6.QtWidgets import QMainWindow, QMessageBox
from gui import (Ui_NUID_window, Ui_Menu_window, Ui_voting_window,
                 Ui_edit_screen, Ui_Endvoting_window)
# Preset candidates and votes
current_candidates = ["Isabella", "Hannah", "Genji"]
vote_counts = {name: 0 for name in current_candidates}
edit_mode_active = True

# CSV file to record votes
def initialize_files():
    global vote_counts, current_candidates, edit_mode_active
    edit_mode_active = True
    vote_counts = {name: 0 for name in current_candidates}

    with open('votes.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['NUID', 'Candidate', 'Votes'])

# opens the main window and gives 3 options to vote, end voting, and to edit
class MenuLogic(QMainWindow, Ui_Menu_window):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    # hides the edit button after it's pressed or if voting is pressed
        if not edit_mode_active:
            self.edit_button.hide()

        self.vote_button.clicked.connect(self.to_login)
        self.edit_button.clicked.connect(self.to_edit)
        self.endvotoing_button.clicked.connect(self.to_end)
    #opens NUID
    def to_login(self):
        self.login_window = NUIDLogic()
        self.login_window.show()
        self.close()
    #opens Edit window
    def to_edit(self):
        self.edit_window = EditLogic()
        self.edit_window.show()
        self.close()
    #opens end voting
    def to_end(self):
        self.end_window = EndLogic()
        self.end_window.show()
        self.close()

# The edit window
class EditLogic(QMainWindow, Ui_edit_screen):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.submit_edit.clicked.connect(self.save_names)

    #saves the names to the votes window
    def save_names(self):
        global current_candidates, vote_counts, edit_mode_active
        inputs = [self.can_one.text().strip(), self.can_two.text().strip(),
                  self.can_three.text().strip(), self.can_four.text().strip(),
                  self.can_five.text().strip(), self.can_six.text().strip()]
        #makes sure that there are at least 2 candidates
        names = [n for n in inputs if n]
        if len(names) < 2:
            #message to let the user that candidates are not supposed to be less than 2
            QMessageBox.warning(self, "Error", "Minimum 2 candidates required.")
            return
        #change the variables in the current_candidate
        current_candidates = names
        vote_counts = {name: 0 for name in current_candidates}
        edit_mode_active = False  # Lock Edit button
        #message to let the user know that the candidates are updated
        QMessageBox.information(self, "Success", "Candidates updated.")
        self.back_to_menu()
    #back button
    def back_to_menu(self):
        self.menu = MenuLogic()
        self.menu.show()
        self.close()

# NUID window when vote is pressed
class NUIDLogic(QMainWindow, Ui_NUID_window):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.Enter_NUID.clicked.connect(self.check_nuid)
        # Does the place holder so u can just click in and it disappers
        self.lineEdit.setText("")
        self.lineEdit.setPlaceholderText("Enter NUID here")

    #check if the nuid is more than 8 digit or alphabets
    def check_nuid(self):
        nuid = self.lineEdit.text().strip()
        if not (nuid.isdigit() and len(nuid) == 8):
            QMessageBox.warning(self, "Error", "Enter 8-digit NUID.")
            return
        #check in the csv if the nuid has alredy been used or not
        if self.already_voted(nuid):
            QMessageBox.critical(self, "Error", "ID has already voted.")
        else:
            self.vote_win = VotingLogic(nuid)
            self.vote_win.show()
            self.close()
    #checking in csv and then saving it
    def already_voted(self, nuid):
        if not os.path.exists('votes.csv'): return False
        with open('votes.csv', 'r') as f:
            return any(row and row[0] == nuid for row in csv.reader(f))

#Voting window
class VotingLogic(QMainWindow, Ui_voting_window):
    def __init__(self, nuid):
        super().__init__()
        self.setupUi(self)
        self.nuid = nuid
        # the radio buttons to choose the candidates
        self.radio_btns = [self.radioone, self.radiotwo, self.radiothree,
                           self.radiofour, self.radiofive, self.radiosix]
        # If not enough candidates this part his the buttons
        for btn in self.radio_btns: btn.hide()
        for i, name in enumerate(current_candidates):
            self.radio_btns[i].setText(name)
            self.radio_btns[i].show()

        self.submitvote_button.clicked.connect(self.cast_vote)
        #cast votes and displays the error if nothing selected.
    def cast_vote(self):
        global vote_counts, edit_mode_active
        selected = next((rb.text() for rb in self.radio_btns if rb.isVisible() and rb.isChecked()), None)

        if not selected:
            QMessageBox.warning(self, "Error", "Pick a candidate.")
            return
        #adds bthe count of votes to the candidate
        vote_counts[selected] += 1
        edit_mode_active = False
        self.save_to_csv(selected)
        self.menu = MenuLogic()
        self.menu.show()
        self.close()
    #saves it to the csv file
    def save_to_csv(self, choice):
        with open('votes.csv', 'a', newline='') as f:
            csv.writer(f).writerow([self.nuid, choice, "1"])

# End voting window
class EndLogic(QMainWindow, Ui_Endvoting_window):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.back_button.clicked.connect(self.return_to_menu)
        global vote_counts
        #shows the name and the number of votes, and if the user chose end voting the beginning it shows winner as non and 0 votes
        if any(vote_counts.values()):
            winner = max(vote_counts, key=vote_counts.get)
            self.winner_candidate.setText(winner)
            self.count_label.setText(str(vote_counts[winner]))
        else:
            self.winner_candidate.setText("None")
            self.count_label.setText("0")
    #Lets the user go back to the main menu but they cannot change the candidates again
    def return_to_menu(self):
        from logic import MenuLogic
        self.menu = MenuLogic()
        self.menu.show()
        self.close()
