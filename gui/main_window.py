from PyQt5.QtWidgets import QStatusBar, QMainWindow, QTabWidget
from PyQt5.QtCore import Qt, QSize

from gui import (DataView, ColChangeDock, ColListDock, QueryDock,
                 SelectCaseDock, MenuBar, ComputeDock, RecodeDock,
                 QueryHistoryDock, OldNewValuesDock)


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.data_view = DataView(self)
        self.change_col_dock = ColChangeDock(self)
        self.list_col_dock = ColListDock(self)
        self.query_dock = QueryDock(self)
        self.query_history_dock = QueryHistoryDock(self)
        self.select_case_dock = SelectCaseDock(self)
        self.compute_dock = ComputeDock(self)
        self.recode_dock = RecodeDock(self)
        self.old_new_values_dock = OldNewValuesDock(self)

        self.menu_bar = MenuBar(self)
        self.status_bar = QStatusBar(self)
        self.ui()
        self.properties()

    def properties(self):
        self.setCentralWidget(self.data_view)
        self.setMenuBar(self.menu_bar)
        self.setStatusBar(self.status_bar)
        self.addDockWidget(Qt.DockWidgetArea(2), self.change_col_dock)
        self.addDockWidget(Qt.DockWidgetArea(2), self.select_case_dock)
        self.addDockWidget(Qt.DockWidgetArea(2), self.old_new_values_dock)

        self.addDockWidget(Qt.DockWidgetArea(1), self.list_col_dock)

        self.addDockWidget(Qt.DockWidgetArea(1), self.recode_dock)
        self.addDockWidget(Qt.DockWidgetArea(1), self.query_dock)
        self.addDockWidget(Qt.DockWidgetArea(1), self.query_history_dock)
        self.addDockWidget(Qt.DockWidgetArea(1), self.compute_dock)

        self.setDockOptions(QMainWindow.VerticalTabs)
        self.tabifyDockWidget(self.change_col_dock, self.select_case_dock)
        self.tabifyDockWidget(self.query_dock, self.query_history_dock)
        self.tabifyDockWidget(self.query_history_dock, self.compute_dock)
        self.tabifyDockWidget(self.compute_dock, self.recode_dock)
        self.tabifyDockWidget(self.select_case_dock, self.old_new_values_dock)
        # self.tabifyDockWidget(self.list_col_dock, self.change_col_dock)

        self.list_col_dock.raise_()

    def ui(self):
        self.setMinimumSize(QSize(1000, 500))
