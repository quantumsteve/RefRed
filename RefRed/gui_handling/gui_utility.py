from PyQt4.QtCore import Qt

class GuiUtility(object):
    
    parent = None
    
    def __init__(self, parent=None):
        self.parent = parent
        
    def data_norm_tab_widget_row_to_display(self):
        return self.parent.current_table_reduction_row_selected
    
    #def data_norm_tab_widget_tab_selected(self):
        #return self.parent.ui.dataNormTabWidget.currentIndex()

    def get_current_table_reduction_check_box_checked(self):
        nbr_row_table_reduction = self.parent.nbr_row_table_reduction
        for row in range(nbr_row_table_reduction):
            _widget = self.parent.ui.reductionTable.cellWidget(row, 0)
            _state = _widget.checkState()
            if _state == Qt.Checked:
                return row
        return -1
    
    def get_data_norm_tab_selected(self):
        return self.parent.ui.dataNormTabWidget.currentIndex()
    
    def is_auto_tof_range_radio_button_selected(self):
        return self.parent.ui.dataTOFautoMode.isChecked()
    
    #def data_peak_and_back_validation(self, with_plot_update = True):
        #self.data_peak_spinbox_validation(with_plot_update = with_plot_update)
        #self.data_back_spinbox_validation(with_plot_update = with_plot_update)
##        CheckErrorWidgets(self)
##	self.fileHasBeenModified()
    
    #def data_peak_spinbox_validation(self, with_plot_update = True):
        #'''
        #This function, reached when the user is done editing the
        #spinboxes (ENTER, leaving the spinbox) 
        #will make sure the min value is < max value    
        #'''

        #bigTableData = self.bigTableData
        ##[row,col] = self.getCurrentRowColumnSelected()
        #row = self._cur_row_selected
        #col = self._cur_column_selected
        #if col != 0:
            #col = 1
        #data = bigTableData[row,col]
        #data = data.active_data

        #peak1 = self.ui.dataPeakFromValue.value()
        #peak2 = self.ui.dataPeakToValue.value()

        #if (peak1 > peak2):
            #peak_min = peak2
            #peak_max = peak1
        #else:
            #peak_min = peak1
            #peak_max = peak2

        #data.peak = [str(peak_min),str(peak_max)]
        #self.active_data = data

        #self.ui.dataPeakFromValue.setValue(peak_min)
        #self.ui.dataPeakToValue.setValue(peak_max)

        ## refresh plots
        #if withPlotUpdate:
            #self.plot_overview_REFL(plot_ix=True, plot_yt=True, plot_yi=True)

        ## save new settings
        #self.save_new_settings()

        #CheckErrorWidgets(self)
        #self.fileHasBeenModified()
        #self.checkRunReductionButton()	

    ## data back spinboxes
    #def data_back_spinbox_validation(self, withPlotUpdate=True):
        #r = self._cur_row_selected
        #c = self._cur_column_selected
        #if c != 0:
            #c = 1
        #_data = self.bigTableData[r,c]
        #if _data is None:
            #return
        #data = _data.active_data

        #back1 = self.ui.dataBackFromValue.value()
        #back2 = self.ui.dataBackToValue.value()

        #if (back1 > back2):
            #back_min = back2
            #back_max = back1
        #else:
            #back_min = back1
            #back_max = back2

        #data.back = [str(back_min),str(back_max)]

        #_data.active_data = data
        #self.bigTableData[r,c] = _data

        #self.ui.dataBackFromValue.setValue(back_min)
        #self.ui.dataBackToValue.setValue(back_max)

        ## save new settings
        #self.save_new_settings()

        ## refresh plots
        #self.plot_overview_REFL(plot_ix=True, plot_yt=True, plot_yi=True)

        #CheckErrorWidgets(self)
        #self.fileHasBeenModified()
        #self.checkRunReductionButton()
    
    #def tofValidation( self, tof_auto_switch_status, tof1, tof2):
        #self.ui.dataTOFautoMode.setChecked(tof_auto_switch_status)
        #self.ui.dataTOFmanualMode.setChecked(not tof_auto_switch_status)
        #bigTableData = self.bigTableData
        #row = self._cur_row_selected
        #col = self._cur_column_selected
        #if col != 0:
            #col = 1
        #data = bigTableData[row, col]
        #_active_data =  data.active_data
        #tof1 = str(float(tof1)*1000)
        #tof2 = str(float(tof2)*1000)
        #if tof_auto_switch_status:
            #_active_data.tof_range_auto = [tof1, tof2]
        #else:
            #_active_data.tof_range = [tof1, tof2]
        #data.active_data = _active_data
        #bigTableData[row, col] = data
        #self.bigTableData = bigTableData
        #self.auto_tof_switch(tof_auto_switch_status)
        #self.fileHasBeenModified()
    