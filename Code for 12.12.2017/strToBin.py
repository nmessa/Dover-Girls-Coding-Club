s = ''
testString = 'Girls Coding Club'
for ch in testString:
    s += '{0:08b}'.format(ord(ch))
print(s)
