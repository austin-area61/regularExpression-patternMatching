def isPhoneNumber(text):
    if len(text) != 12:
        return False
    for i in range(0, 3):
        if not text[i].isdecimal():
            return False
    if text[3] != '-':
        return False
    for i in range(4, 7):
        if not text[i].isdecimal():
            return False
    if text[7] != '-':
        return False
    for i in range(8, 12):
        if not text[i].isdecimal():
            return False
    return True

#print('415-555-4242 is a phone number:')
#print(isPhoneNumber('415-555-4242'))  # Output: True
#print('Moshu Moshu is a phone number:')
#print(isPhoneNumber('Moshu Moshu'))  # Output: False

message = 'Call ne at 455-555-1011 tomorrow. 455-555-999 es mi officina.'
for i in range(len(message)):
    chunk = message[i:i + 12]
    if isPhoneNumber(chunk):
        print('phone number found: '+ chunk)
print('Done!')