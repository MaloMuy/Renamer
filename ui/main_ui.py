#import libraries
from PySide6 import QtWidgets, QtCore
import sys

try:
    import bpy
    logiciel = "Blender"
except ImportError:
    pass

try:
    from maya import cmds
    logiciel = "Maya"
except ImportError:
    pass


if logiciel == "Blender":
    import core.actions_blender as actions

elif logiciel == "Maya":
    import core.actions_maya as actions


class RenamerUI(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Renamer Tool")
        self.setFixedSize(275, 472)

        # Put window always on top
        self.setWindowFlag(QtCore.Qt.WindowType.WindowStaysOnTopHint, True)
        
        self.build_ui() 

    def build_ui(self):
        self.main_widget = QtWidgets.QWidget(self)
        self.setCentralWidget(self.main_widget)

        self.main_layout = QtWidgets.QVBoxLayout(self.main_widget)

        # ====================
        # == SELECT NAME UI ==
        # ====================

        self.select_all_button = QtWidgets.QPushButton("Select All", self.main_widget)
        self.main_layout.addWidget(self.select_all_button)
        self.select_all_button.clicked.connect(actions.select_all_objects)

        self.select_name_text = QtWidgets.QLineEdit()
        self.select_name_button = QtWidgets.QPushButton("Select with Name", self.main_widget)
        self.select_name_button.clicked.connect(self.search_object)


        self.select_name_layout = QtWidgets.QHBoxLayout()
        self.select_name_layout.addWidget(self.select_name_text)
        self.select_name_layout.addWidget(self.select_name_button)
        
        self.main_layout.addLayout(self.select_name_layout)

        # ===================
        # ==== RENAME UI ====
        # ===================

        self.rename_label = QtWidgets.QLabel("Rename :")
        self.rename_label.setFixedSize(50,10)
        self.rename_text = QtWidgets.QLineEdit()
        
        self.start_label = QtWidgets.QLabel("Start :")
        self.start_label.setFixedSize(50,10)
        self.start_text = QtWidgets.QLineEdit("1")
        
        self.padding_label = QtWidgets.QLabel("Padding :")
        self.padding_label.setFixedSize(50,17)
        self.padding_text = QtWidgets.QLineEdit("3")

        self.rename_button = QtWidgets.QPushButton("Rename")
        self.rename_button.clicked.connect(self.renamer)

        self.rename_number_button = QtWidgets.QPushButton("Rename and Number")
        self.rename_number_button.clicked.connect(self.rename_number)

        self.rename_layout = QtWidgets.QVBoxLayout()

        self.rename_text_layout = QtWidgets.QHBoxLayout()
        self.rename_text_layout.addWidget(self.rename_label)
        self.rename_text_layout.addWidget(self.rename_text)

        self.rename_option_layout = QtWidgets.QHBoxLayout()

        self.rename_option_layout.addWidget(self.start_label)
        self.rename_option_layout.addWidget(self.start_text)
        self.rename_option_layout.addWidget(self.padding_label)
        self.rename_option_layout.addWidget(self.padding_text)

        self.padding_option_layout = QtWidgets.QHBoxLayout()
        self.padding_option_layout.addWidget(self.padding_label)
        self.padding_option_layout.addWidget(self.padding_text)

        self.rename_button_layout = QtWidgets.QHBoxLayout()
        self.rename_button_layout.addWidget(self.rename_button)
        self.rename_button_layout.addWidget(self.rename_number_button)

        self.main_layout.addLayout(self.rename_layout)
        self.rename_layout.addLayout(self.rename_text_layout)
        self.rename_layout.addLayout(self.rename_option_layout)
        self.rename_layout.addLayout(self.rename_button_layout)
        self.rename_layout.setContentsMargins(0, 10, 0, 10)

        # ====================
        # = PREFIX/SUFFIX UI =
        # ====================

        self.prefix_label = QtWidgets.QLabel("Prefix :")
        self.prefix_label.setFixedSize(50,10)
        self.prefix_text = QtWidgets.QLineEdit()
        self.prefix_button = QtWidgets.QPushButton("Add")
        self.prefix_button.clicked.connect(self.add_prefix)
        self.prefix_button.setFixedSize(50,25)

        self.suffix_label = QtWidgets.QLabel("Suffix :")
        self.suffix_label.setFixedSize(50,10)
        self.suffix_text = QtWidgets.QLineEdit()
        self.suffix_button = QtWidgets.QPushButton("Add")
        self.suffix_button.clicked.connect(self.add_suffix)
        self.suffix_button.setFixedSize(50,25)

        self.msh_button = QtWidgets.QPushButton("MSH")
        self.msh_button.clicked.connect(actions.name_suffix_msh)
        self.grp_button = QtWidgets.QPushButton("GRP")
        self.grp_button.clicked.connect(actions.name_suffix_grp)
        self.jnt_button = QtWidgets.QPushButton("JNT")
        self.jnt_button.clicked.connect(actions.name_suffix_jnt)
        self.con_button = QtWidgets.QPushButton("CON")
        self.con_button.clicked.connect(actions.name_suffix_con)

        self.prefix_layout = QtWidgets.QHBoxLayout()
        self.prefix_layout.addWidget(self.prefix_label)
        self.prefix_layout.addWidget(self.prefix_text)
        self.prefix_layout.addWidget(self.prefix_button)

        self.suffix_layout = QtWidgets.QHBoxLayout()
        self.suffix_layout.addWidget(self.suffix_label)
        self.suffix_layout.addWidget(self.suffix_text)
        self.suffix_layout.addWidget(self.suffix_button)

        self.shortfix_layout = QtWidgets.QHBoxLayout()
        self.shortfix_layout.addWidget(self.msh_button)
        self.shortfix_layout.addWidget(self.grp_button)
        self.shortfix_layout.addWidget(self.jnt_button)
        self.shortfix_layout.addWidget(self.con_button)

        self.main_layout.addLayout(self.prefix_layout)
        self.main_layout.addLayout(self.suffix_layout)
        self.main_layout.addLayout(self.shortfix_layout)
        self.shortfix_layout.setContentsMargins(0, 0, 0, 10)

        # =====================
        # ===== REMOVE UI =====
        # =====================

        self.preremove_text = QtWidgets.QLineEdit("0")
        self.remove_button = QtWidgets.QPushButton("Remove")
        self.remove_button.setFixedSize(125,25)
        self.subremove_text = QtWidgets.QLineEdit("0")
        self.remove_button.clicked.connect(self.remove_character)

        self.remove_layout = QtWidgets.QHBoxLayout()
        self.remove_layout.addWidget(self.preremove_text)
        self.remove_layout.addWidget(self.remove_button)
        self.remove_layout.addWidget(self.subremove_text)

        self.main_layout.addLayout(self.remove_layout)
        self.remove_layout.setContentsMargins(0, 0, 0, 10)

        # =====================
        # = SEARCH/REPLACE UI =
        # =====================

        self.search_label = QtWidgets.QLabel("Search :")
        self.search_label.setFixedSize(70,10)
        self.search_text = QtWidgets.QLineEdit()
        self.replace_label = QtWidgets.QLabel("Replace by :")
        self.replace_label.setFixedSize(70,17)
        self.replace_text = QtWidgets.QLineEdit()

        self.radio_group = QtWidgets.QButtonGroup()
        self.selected_button = QtWidgets.QRadioButton("Selected")
        self.all_button = QtWidgets.QRadioButton("All")
        self.all_button.setChecked(True)
        self.hierarchy_button = QtWidgets.QRadioButton("Hierarchy")
        self.search_replace_button = QtWidgets.QPushButton("Search and Replace")
        self.search_replace_button.clicked.connect(self.search_replace)

        self.search_layout = QtWidgets.QHBoxLayout()
        self.search_layout.addWidget(self.search_label)
        self.search_layout.addWidget(self.search_text)

        self.replace_layout = QtWidgets.QHBoxLayout()
        self.replace_layout.addWidget(self.replace_label)
        self.replace_layout.addWidget(self.replace_text)

        self.radio_group.addButton(self.all_button, 1)
        self.radio_group.addButton(self.selected_button, 2)
        self.radio_group.addButton(self.hierarchy_button, 3)
        
        self.radio_layout = QtWidgets.QHBoxLayout()
        self.radio_layout.addWidget(self.all_button)
        self.radio_layout.addWidget(self.selected_button)
        self.radio_layout.addWidget(self.hierarchy_button)

        self.main_layout.addLayout(self.search_layout)
        self.main_layout.addLayout(self.replace_layout)
        self.main_layout.addLayout(self.radio_layout)
        self.main_layout.addWidget(self.search_replace_button)

        self.radio_group.checkedId()

    def search_object(self):
        actions.search_object(self.select_name_text.text())

    def renamer(self):
        actions.renamer(self.rename_text.text())

    def rename_number(self):
        rename_text = self.rename_text.text()
        start_text = int(self.start_text.text())
        padding_text = int(self.padding_text.text())
        actions.rename_number(rename_text, start_text, padding_text)

    def add_prefix(self):
        actions.name_prefix(self.prefix_text.text())

    def add_suffix(self):
        actions.name_suffix(self.suffix_text.text())

    def remove_character(self):
        actions.remove_character(int(self.preremove_text.text()), int(self.subremove_text.text()))

    def search_replace(self):
        actions.search_replace(self.search_text.text(), self.replace_text.text(), self.radio_group.checkedId())


def show_renamer():
    global window

    global _qt_app
    app = QtWidgets.QApplication.instance()
    if app is None:
        app = QtWidgets.QApplication(sys.argv if 'sys' in dir() else [])
    _qt_app = app
    
    try:
        window.close()
        window.deleteLater()
    except Exception:
        pass
    
    window = RenamerUI()
    window.show()
    



