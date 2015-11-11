#!/usr/bin/env python

# FIXME Copied from dials.index.py. This is needed here because scipy needs to
# be imported before cctbx otherwise there will be a segmentation fault. This
# should be fixed in dials.index so that we don't need to import here.
try:
  # try importing scipy.linalg before any cctbx modules, otherwise we
  # sometimes get a segmentation fault/core dump if it is imported after
  # scipy.linalg is a dependency of sklearn.cluster.DBSCAN
  import scipy.linalg # import dependency
except ImportError, e:
  pass

from PyQt4 import QtCore, QtGui
from phil_param_widget_builder import ParameterWidget


class ImportPage(QtGui.QWidget):
    def __init__(self, parent=None):
        super(ImportPage, self).__init__(parent)

        self.cmd_lin_default = "dials.import ~/data/th_8_2_0*"
        self.button_label = "Import"

        my_dui_path = os.environ["DUI_PATH"]
        self.logo_path = my_dui_path + "/../dui/dartlang_logo_small.png"

        configGroup = QtGui.QGroupBox("Box 01")
        configLayout = QtGui.QVBoxLayout()

        lin_txt =  QtGui.QLineEdit(self)
        configLayout.addWidget(lin_txt)
        configGroup.setLayout(configLayout)

        mainLayout = QtGui.QVBoxLayout()
        mainLayout.addWidget(configGroup)
        mainLayout.addStretch(1)

        self.setLayout(mainLayout)

        fl_diag = QtGui.QFileDialog()
        fileName = fl_diag.getOpenFileName(self, "Open File")#,QtCore.QDir.currentPath())
        print "Hi 01"
        if fileName:
            print "Hi 02"
            image = QtGui.QImage(fileName)
            if image.isNull():
                print "image.isNull()"
        print "image =", image

        example_from_the_mouse_n_the_python = '''
            #----------------------------------------------------------------------
            def openFileDialog(self):
                """
                Opens a file dialog and sets the label to the chosen path
                """
                import os
                path, _ = QtGui.QFileDialog.getOpenFileName(self, "Open File", os.getcwd())
                self.label.setText(path)

            #----------------------------------------------------------------------
            def openDirectoryDialog(self):
                """
                Opens a dialog to allow user to choose a directory
                """
                flags = QtGui.QFileDialog.DontResolveSymlinks | QtGui.QFileDialog.ShowDirsOnly
                d = directory = QtGui.QFileDialog.getExistingDirectory(self,
                                                                       "Open Directory",
                                                                       os.getcwd(),
                                                                       flags)
                self.label.setText(d)

        '''

        example_from_StackOverflow = '''
          fileName = QtGui.QFileDialog.getSaveFileName(self, 'Dialog Title', '/path/to/default/directory', selectedFilter='*.txt')
          if fileName:
              print fileName

        '''

        example_from_StackOverflow_02 = '''
          from PySide import QtGui
          app = QtGui.QApplication([])
          dialog = QtGui.QFileDialog()
          dialog.setFileMode(QtGui.QFileDialog.Directory)
          dialog.setOption(QtGui.QFileDialog.ShowDirsOnly)
          dialog.exec_()
        '''


class FindspotstParameterWidget(QtGui.QWidget):

    def __init__(self, parent=None):
        from dials.command_line.find_spots import phil_scope
        super(FindspotstParameterWidget, self).__init__(parent)

        self.super_parent = parent
        param_widg = ParameterWidget(self.super_parent, phil_scope)

        mainLayout = QtGui.QVBoxLayout()
        mainLayout.addWidget(param_widg)
        self.setLayout(mainLayout)

        self.cmd_lin_default = "dials.find_spots datablock.json"
        self.button_label = "Find Spots"
        my_dui_path = os.environ["DUI_PATH"]
        self.logo_path = my_dui_path + "/../dui/nuclear_dartlang_logo_small.png"


class IndexParameterWidget(QtGui.QWidget):

    def __init__(self, parent=None):
        from dials.command_line.index import phil_scope
        super(IndexParameterWidget, self).__init__(parent)

        self.super_parent = parent
        param_widg = ParameterWidget(self.super_parent, phil_scope)

        mainLayout = QtGui.QVBoxLayout()
        mainLayout.addWidget(param_widg)
        self.setLayout(mainLayout)

        self.cmd_lin_default = "dials.index datablock.json strong.pickle"
        self.button_label = "Index"
        my_dui_path = os.environ["DUI_PATH"]
        self.logo_path = my_dui_path + "/../dui/bird_dartlang_logo_small.png"



class RefineParameterWidget(QtGui.QWidget):

    def __init__(self, parent=None):
        from dials.command_line.refine import phil_scope
        super(RefineParameterWidget, self).__init__(parent)

        self.super_parent = parent
        param_widg = ParameterWidget(self.super_parent, phil_scope)

        mainLayout = QtGui.QVBoxLayout()
        mainLayout.addWidget(param_widg)
        self.setLayout(mainLayout)

        self.cmd_lin_default = "dials.refine experiments.json indexed.pickle"
        self.button_label = "Refine"
        my_dui_path = os.environ["DUI_PATH"]
        self.logo_path = my_dui_path + "/../dui/dartlang_logo_small.png"


class IntegrateParameterWidget(QtGui.QWidget):

    def __init__(self, parent=None):
        from dials.command_line.integrate import phil_scope
        super(IntegrateParameterWidget, self).__init__(parent)

        self.super_parent = parent
        param_widg = ParameterWidget(self.super_parent, phil_scope)

        mainLayout = QtGui.QVBoxLayout()
        mainLayout.addWidget(param_widg)
        self.setLayout(mainLayout)

        self.cmd_lin_default = "dials.integrate refined_experiments.json refined.pickle"
        self.button_label = "Integrate"
        my_dui_path = os.environ["DUI_PATH"]
        self.logo_path = my_dui_path + "/../dui/nuclear_dartlang_logo_small.png"


class ExportParameterWidget(QtGui.QWidget):

    def __init__(self, parent=None):
        from dials.command_line.export_mtz import phil_scope
        super(ExportParameterWidget, self).__init__(parent)

        self.super_parent = parent
        param_widg = ParameterWidget(self.super_parent, phil_scope)

        mainLayout = QtGui.QVBoxLayout()
        mainLayout.addWidget(param_widg)
        self.setLayout(mainLayout)

        self.cmd_lin_default = "dials.export_mtz experiments.json integrated.pickle hklout=integrated.mtz"
        self.button_label = "Export mtx"
        my_dui_path = os.environ["DUI_PATH"]
        self.logo_path = my_dui_path + "/../dui/bird_dartlang_logo_small.png"


from subprocess import call as shell_func
import os


class MainWindow(QtGui.QMainWindow):

  def __init__(self, parent=None):

    # Call the parent constructor
    super(MainWindow, self).__init__(parent)

    # Create the parameter window widget
    params = FindspotstParameterWidget(self)
    #params = IndexParameterWidget()
    #params = RefineParameterWidget()
    #params = IntegrateParameterWidget()
    #params = ExportParameterWidget()

    # Create the window layout
    layout = QtGui.QVBoxLayout()
    layout.addWidget(params)

    # Setup the window contents
    window = QtGui.QWidget()
    window.setLayout(layout)
    self.setCentralWidget(window)

  def update_lin_txt(self):
    print "from tmp parent.update_lin_txt"

if __name__ == '__main__':
  import sys

  # Create the application
  app = QtGui.QApplication(sys.argv)

  # Create the main window
  window = MainWindow()
  window.resize(800, 600)
  window.show()

  # Execute the application
  sys.exit(app.exec_())

