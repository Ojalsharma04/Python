
import sys
from PyQt6.QtWidgets import QApplication
from logic import MenuLogic, initialize_files

def main():
    initialize_files()
    app = QApplication(sys.argv)

    start_screen = MenuLogic()
    start_screen.show()

    sys.exit(app.exec())

if __name__ == "__main__":
    main()
