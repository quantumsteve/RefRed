from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import Qt
import numpy as np
from RefRed.plot.clear_plots import ClearPlots
from RefRed.gui_handling.gui_utility import GuiUtility
import RefRed.colors
from RefRed.version import window_title


class RefRedInterfaceHandler(object):

    from_row = -1
    to_row = -1
    
    def __init__(self, parent=None):
        self.parent = parent
        
    def full_reset(self):
        self.__clear_plots()
        self.__clear_stitching_table()
        self.__clear_scaling_factor()
        
    def __clear_plots(self):
        ClearPlots(self.parent, 
                   stitched = True)
        
    def __clear_stitching_table(self):
        nbr_row = self.parent.ui.dataStitchingTable.rowCount()
        nbr_col = self.parent.ui.dataStitchingTable.columnCount()
        for _row in range(nbr_row):
            for _col in range(0, nbr_col):
                if not (self.parent.ui.dataStitchingTable.item(_row, _col) is None):
                    self.parent.ui.dataStitchingTable.item(_row, _col).setText("")
        
    def __clear_scaling_factor(self):
        self.parent.ui.scalingFactorFile.setText("")
        _list = ['Select Incident Medium ...']
        self.parent.ui.selectIncidentMediumList.clear()
        self.parent.ui.selectIncidentMediumList.addItems(_list)
        self.parent.full_scaling_factor_file_name = ''
        
        