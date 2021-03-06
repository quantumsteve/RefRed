#!/usr/bin/env python
#-*- coding: utf8 -*-
'''
  Small program for quick access to SNS liquids reflectometer raw data.
'''
import os
import sys
# must be imported through qtpy before any other gui imports
from PyQt4.QtGui import QApplication, QSplashScreen, QPixmap
from PyQt4.QtCore import Qt

sys.path.append("/opt/mantidnightly/bin")

# if script was run from commandline
try:
    if os.path.abspath(__file__).endswith('scripts/RefRed'):
        sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
except NameError:
    pass

def _run(argv=[]):
    app=QApplication(argv)
    splash=QSplashScreen(QPixmap(u':/General/logo_refl_hq.png'))
    splash.showMessage(u"""<html>
                       <div style="margin-bottom: 420;"> &nbsp;</div>
                       <div style="font-size: 12pt; margin-bottom: 15;">
                       <b>RefRed</b> Version %s
                       </div>
                       <div>Starting up...</div>
                       </html>"""%version.str_version,
                                 alignment=Qt.AlignBottom|Qt.AlignHCenter)
    splash.show()
    QApplication.processEvents()

    window=MainGui(argv)
    window.show()
    splash.finish(window)
    return app.exec_()

if __name__=='__main__':
    from RefRed import config
    from RefRed import version
    from RefRed.main import MainGui
    
    sys.exit(_run(sys.argv[1:]))