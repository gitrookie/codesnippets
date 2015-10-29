import dbus
import gobject
from dbus import service
# from gi._gobject import MainLoop
from dbus.mainloop.glib import DBusGMainLoop

class DBusServer(service.Object):
    def __init__(self, name, object_path):
        # super(service.Object, self).__init__(name, object_path)
        dbus.service.Object.__init__(self, name, object_path)

    @dbus.service.method("com.gaurav.sood", in_signature='s', out_signature="s")
                         # async_callbacks=('reply_handler', 'error_handler'))
    def test(self, args):
        return args + " Sent by dbus client"

    @dbus.service.method("com.gaurav.sood", in_signature='s', out_signature="s")
    def foo(self, args):
        return "foo"

def reply_handler():
    print "In reply handler"

bus_loop = DBusGMainLoop(set_as_default=True)
session_bus = dbus.SessionBus()
session_name = service.BusName("com.gaurav.sood", session_bus)
dbus_server = DBusServer(session_name, "/com/gaurav/sood")

loop = gobject.MainLoop()

try:
    loop.run()
except KeyboardInterrupt:
    loop.quit()
