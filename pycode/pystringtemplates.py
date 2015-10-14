from string import Template

class MyTemplate(Template):
    delimiter = '#'


s = MyTemplate("#name likes #food")
n = s.substitute(dict(name='gaurav', food='pasta', seasoning='italian'))
print(n)
