from PyQt4 import QtGui
from RefRed.calculations.run_sequence_breaker import RunSequenceBreaker
from RefRed.check_list_run_compatibility import CheckListRunCompatibility

import colors

class UpdateReductionTable(object):
    
    raw_runs = None
    
    def __init__(self, parent=None, runs=None, row=0, col=1, clear_cell=False):
        self.parent= parent
        self.row = row
        self.col = col
        
        if clear_cell:
            self.clear_cell()
            return
        
        self.raw_runs = str(runs)
        run_breaker = RunSequenceBreaker(run_sequence=self.raw_runs)
        _list_run = run_breaker.final_list
        nxs_loader = CheckListRunCompatibility(list_run=_list_run)

        if nxs_loader.runs_compatible:
            _color = QtGui.QColor(colors.VALUE_OK)
        else:
            _color = QtGui.QColor(colors.VALUE_BAD)
        self.parent.ui.reductionTable.item(row, 8).setBackground(_color)
    
    def clear_cell(self):
        print('in clear cell')
        
    