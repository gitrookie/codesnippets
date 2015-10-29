import dbus

session_bus = dbus.SessionBus()
proxy_method = session_bus.get_object('com.gaurav.sood', "/com/gaurav/sood")
print(dir(proxy_method))

print(proxy_method.test("This is dbus client example"))
print("Calling Foo...")
print(proxy_method.foo("This is foo"))
