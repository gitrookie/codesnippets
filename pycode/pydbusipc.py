import sys
import dbus
import gobject
from dbus.mainloop.qt import DBusQtMainLoop
from dbus import service
# from gi._gobject import MainLoop
from dbus.mainloop.glib import DBusGMainLoop
from PyQt4.QtCore import QCoreApplication

class DBusServer(service.Object):
    def __init__(self, name, object_path):
        # super(service.Object, self).__init__(name, object_path)
        dbus.service.Object.__init__(self, name, object_path)

    @dbus.service.method("com.gaurav.sood", in_signature='s', out_signature="s")

    def test(self, args):
        return args + " Sent by dbus client"

    @dbus.service.method("com.gaurav.sood", in_signature='s', out_signature="s")
    def foo(self, args):
        return "foo"

bus_loop = DBusQtMainLoop(set_as_default=True)
session_bus = dbus.SessionBus()
session_name = service.BusName("com.gaurav.sood", session_bus)
try:
    dbus_server = DBusServer(session_name, "/com/gaurav/sood")
except RuntimeError:
    pass


loop = gobject.MainLoop()
# loop = QCoreApplication(sys.argv)

try:
    loop.run()
except KeyboardInterrupt:
    loop.quit()
