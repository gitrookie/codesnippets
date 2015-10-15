import re

patt = re.compile("^Subject: (.*)", re.IGNORECASE)
match = patt.search("Subject: Regarding leave application")
print(match.group(1))


# Lazy Qunatifiers
patt = re.compile("<(.*)>", re.IGNORECASE)
match = patt.search("<h1>Introduction</h1>")



# Alternation
patt = re.compile("(abcde|abc)", re.IGNORECASE)
match = patt.search("abcde")

# Positive Look Ahead
patt = re.sub("(?<=\d{3})", ",", "1002003004005", count=1)

patt = re.compile("(?P<name>abcd)\s(?P=name)", re.IGNORECASE)
# patt = re.compile("(abcd) \1", re.IGNORECASE)
match = patt.search("abcd abcde")


thou = re.sub("(\d)(?=(\d{3})+(?!\d))", r"\1,", "123456789")
# patt = re.compile("(\d)(?=(\d{3})+(?!\d))")
# match = patt.search("12345678")
