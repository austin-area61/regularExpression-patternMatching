import re
phoneNumberRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumberRegex.search('Mi numero de telefono es 415-666-4343.')
print('Phone number found: ' +mo.group())