import glob
import os
import numpy as np
from PyQt4 import QtGui, QtCore
from RefRed.interfaces.template_management import Ui_MainWindow
from RefRed.interfaces.confirm_auto_reduce_dialog import Ui_Dialog
from RefRed.preview_config.preview_config import PreviewConfig


class TemplateManagement(QtGui.QMainWindow):
    
    _window_title = "Template Management - "
    _filter = "*template*.cfg"
    _list_filter = ['*template*.cfg', '*.cfg', '*.txt', '*']
    _window_offset = np.array([25, 50])
    _auto_reduce_folder = '/SNS/REF_L/shared/'
    _final_auto_reduce_template_folder = _auto_reduce_folder + 'autoreduce'
    _auto_reduce_name = 'template.xml'
    _full_template_file_name_selected = ''
    _folder = ''
    _current_ipts = ''
    
    def __init__(self, parent=None):
        self.parent = parent
        
        QtGui.QMainWindow.__init__(self, parent=parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self._init_gui()
        self._current_ipts = self.parent.current_ipts
        
        if not (self.parent.current_ipts == ''):
            self._auto_reduce_folder = '/SNS/REF_L/' + self._current_ipts + '/shared/'
        
        self._folder = self._auto_reduce_folder

    def load_default_directory(self):
        self._populate_table()
        
    def _init_gui(self):
        self.ui.template_filter_button.addItems(self._list_filter)
        
    def browseFolderButton(self):
        _path = self._auto_reduce_folder
        pathQFileDialog = QtGui.QFileDialog(self.parent)
        folder = str(pathQFileDialog.getExistingDirectory(self, 
                                                      'Select Template Folder',
                                                      _path,
                                                      QtGui.QFileDialog.ShowDirsOnly))
        
        if folder == "":
            return
        
        self._folder = folder
        self._populate_table()

    def _populate_table(self):
        self._clear_table()
        self.ui.tableWidget.setColumnCount(2)

        if self._folder is '':
            return
        
        _folder = self._folder
        _filter = self._filter
        _full_list_files = glob.glob(_folder + '/*')
        self.full_list_files = _full_list_files
        
        _list_files = glob.glob(_folder + '/' + _filter)
        self._list_files = _list_files
        self.ui.tableWidget.setRowCount(len(_list_files))

        for _row, _file in enumerate(_list_files):
            if _row == 0:
                # put full path in window title
                _path = os.path.dirname(_file)
                self.setWindowTitle(self._window_title + _path)

            # name of file
            _short_file = os.path.basename(_file)
            _item = QtGui.QTableWidgetItem(_short_file)
            self.ui.tableWidget.setItem(_row, 0, _item)
        
            # preview button
            _button = QtGui.QPushButton("Preview")
            QtCore.QObject.connect(_button, QtCore.SIGNAL("clicked()"),
                                   lambda row=_row: self.preview_button(row))
            self.ui.tableWidget.setCellWidget(_row, 1, _button)
        
        _default_selection = QtGui.QTableWidgetSelectionRange(0, 0, 0, 1)
        self.ui.tableWidget.setRangeSelected(_default_selection, True)
    
        if len(_list_files) > 0:
            self.check_gui(status = True)
        else:
            self.check_gui(status = False)
        
    def check_gui(self, status=False):
        self.ui.template_file_button.setEnabled(status)

    def preview_button(self, _row):
        try:
            o_preview_config = PreviewConfig(parent = self, 
                                             is_live = False,
                                             filename = self._list_files[_row],
                                             geometry_parent = self.geometry(),
                                             window_offset = _row * self._window_offset)
            o_preview_config.show()
            _current_selection = self.ui.tableWidget.selectedRanges()
            self.ui.tableWidget.setRangeSelected(_current_selection[0], False)
            _selection = QtGui.QTableWidgetSelectionRange(_row, 0, _row, 1)
            self.ui.tableWidget.setRangeSelected(_selection, True)
        except:
            _widget = self.ui.tableWidget.cellWidget(_row, 1)
            _widget.setEnabled(False)
            _widget.setText("NOT A TEMPLATE!")
        
    def _clear_table(self):
        self.ui.tableWidget.clear()
    
    def filterTemplateButton(self, filter_string):
        self._filter = str(filter_string)
        self._populate_table()
    
    def templateFileSelectedButton(self):
        _selected_row = self.ui.tableWidget.currentRow()
        _filename = self._list_files[_selected_row]
        o_confirm = ConfirmAutoReduceDialog(parent = self, 
                                            filename = _filename,
                                            ipts = self._current_ipts)
        o_confirm.show()

    def _replace_auto_template(self, full_file_name=''):
        _final_auto_reduce_template_folder = self._final_auto_reduce_template_folder
        _auto_reduce_name = self._auto_reduce_name
        _template_source_name = self._full_template_file_name_selected 

        print(_final_auto_reduce_template_folder)
        print(_auto_reduce_name)
        print(_template_source_name)


    def closeEvent(self, event=None):
        self.close()


class ConfirmAutoReduceDialog(QtGui.QDialog):
    
    def __init__(self, parent=None, filename=None, ipts=''):
        self.parent = parent
        
        QtGui.QDialog.__init__(self, parent=parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        
        self.full_file_name = filename
        self.parent._full_template_file_name_selected = filename
        _short_file = os.path.basename(filename)
        self.ui.file_name.setText(_short_file)
        
        if ipts == '':
            self.ui.select_ipts_button.setEnabled(True)
        else:
            self.ui.ipts.setText(ipts)
            
        self.check_gui()
        
    def check_gui(self):
        if self.parent._current_ipts == '':
            status = False
        else: 
            status = True
        self.ui.buttonBox.setEnabled(status)
    
    def browse_ipts(self):
        _path = self.parent._auto_reduce_folder
        pathQFileDialog = QtGui.QFileDialog(self.parent)
        folder = str(pathQFileDialog.getExistingDirectory(self, 
                                                      'Select IPTS folder',
                                                      _path,
                                                      QtGui.QFileDialog.ShowDirsOnly))
        
        if folder == "":
            return

        _ipts = self.isolate_ipts(folder)
        self.ui.ipts.setText(_ipts)
        self.check_gui()
        
    def isolate_ipts(self, folder):
        list_folder = folder.split('/')
        ipts = list_folder[3]
        self.parent._current_ipts = ipts
        self.parent._final_auto_reduce_template_folder = "/".join(list_folder[0:4]) + '/shared/autoreduce/'
        return ipts
    
    def closeEvent(self, event=None):
        self.close()
        
    def accept(self):
        self.parent._replace_auto_template(self.full_file_name)
        self.parent.closeEvent()
        self.closeEvent()
        
    def reject(self):
#        self.parent.closeEvent()
        self.closeEvent()