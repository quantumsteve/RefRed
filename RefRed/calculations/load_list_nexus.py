import time

from mantid.simpleapi import *
from RefRed.calculations.load_nexus import LoadNexus

class LoadListNexus(object):

    list_nexus = None
    list_run = None

    list_wks_loaded = []
    list_run_loaded = []
    list_nxs_loaded = []
    
    def __init__(self, list_nexus=None, list_run=None, metadata_only=False):
        if list_nexus is None:
            return
        self.list_nexus = list_nexus
        self.list_run = list_run
        self.number_of_runs = len(list_run)
        
        self.init_parameters()
        
        for index, nexus_name in enumerate(list_nexus):
            filename = list_nexus[index]
            _run = list_run[index]
            _ws_name = "_data_file_%s" %_run
            wks_object = LoadNexus(filename = filename, 
                                   output_wks = _ws_name,
                                   metadata_only = True)
            if (wks_object.workspace):
                self.list_wks_loaded.append(wks_object.workspace)
                self.list_run_loaded.append(_run)
                self.list_nxs_loaded.append(nexus_name)

    def init_parameters(self):
        self.list_wks_loaded = []
        self.list_run_loaded = []
        self.list_nxs_loaded = []


        