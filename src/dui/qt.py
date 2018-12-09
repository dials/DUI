"""
QT Cross-compatibility for DUI
"""

# Because we *-import as a shim in this file, ignore for flake8 purposes
# flake8: noqa

from __future__ import absolute_import, division, print_function

import logging

logger = logging.getLogger(__name__)


try:
    # Try preferred interface first - PyQt5
    from PyQt5.QtWidgets import *
    from PyQt5.QtCore import *
    from PyQt5.QtGui import *
    from PyQt5.QtWebKit import *
    from PyQt5.QtWebKitWidgets import *

    # Signal implementation changes slightly across implementations
    Signal = pyqtSignal

    QT5 = True

    logger.info("Using PyQt5 for QT")

except ImportError:
    # Fallback to QT4
    try:
        # Primary interface: PyQt4
        from PyQt4.QtGui import *
        from PyQt4.QtCore import *
        from PyQt4.QtWebKit import *

        Signal = pyqtSignal

        QT5 = False
        logger.info("Using PyQt4 for QT")

    except ImportError:
        # Backup: try PySide
        from PySide.QtGui import *
        from PySide.QtCore import *
        from PySide.QtWebKit import *

        QT5 = False
        logger.info("Using PySide for QT")
