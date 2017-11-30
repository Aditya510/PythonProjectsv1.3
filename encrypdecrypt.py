import base64
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import base64

MESSAGE = '''
GkMaARoCBhsSSlBJQUMOBhwAF09NTVcQDggFERgGFg1GTUpTRgEaABwEDg0FSlxTRgEPEhYTFxtG TUpTRg0HFwsEBwEDARVUTUROFRoJCg0XCB0WDxBOVENBRB0PAR8QCgENU1VBRBoADxIaFRdOVENB RBsACxVUTUROEhYOREhbTVcECApIUwQ=
'''

KEY = 'aditya.bansal'


text = (base64.b64decode(MESSAGE))
print(text)


def xor(data, key): 
    return bytearray(a^b for a, b in zip(*map(bytearray, [data, key])))

print(xor(text,KEY))
