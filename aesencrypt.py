def toHEX(ascii):
    hexa = []
    result = []
    temp = []
    for i in range(len(ascii)):
        ch = ascii[i]
        in1 = ord(ch)
        h = hex(in1).lstrip("0x")
        hexa.append(h)

    if(len(hexa) == 16):
        result.append(hexa)
        result.append(['80', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00'])

    elif(len(hexa) < 16):
        hexa.append('80')
        if(len(hexa) < 16):
            while(len(hexa) < 16):
                hexa.append('00')
        result.append(hexa)

    else:
        for i in range(0, len(hexa), 16):
            if(i+16 < len(hexa)):
                temp.append(hexa[i:i+16])
            else:
                temp.append(hexa[i:len(hexa)])

        flag = 0
        for data in temp:
            if(len(data) == 16):
                result.append(data)
            else:
                data.append('80')
                while(len(data) < 16):
                    data.append('00')
                result.append(data)
                flag = 1

        if(flag == 0):
            result.append(['80', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00'])

    return result

def rotWord(arr):
    result = []
    for i in range(4):
        result.append(arr[(i+1)%4])
    return result

def subWord(arr):
    result = []
    sbox = [['63', '7c', '77', '7b', 'f2', '6b', '6f', 'c5', '30', '01', '67', '2b', 'fe', 'd7', 'ab', '76'],
            ['ca', '82', 'c9', '7d', 'fa', '59', '47', 'f0', 'ad', 'd4', 'a2', 'af', '9c', 'a4', '72','c0'],
            ['b7', 'fd', '93', '26', '36', '3f', 'f7', 'cc', '34', 'a5', 'e5', 'f1', '71', 'd8', '31','15'],
            ['04', 'c7', '23', 'c3', '18', '96', '05', '9a', '07', '12', '80', 'e2', 'eb', '27', 'b2','75'],
            ['09', '83', '2c', '1a', '1b', '6e', '5a', 'a0', '52', '3b', 'd6', 'b3', '29', 'e3', '2f','84'],
            ['53', 'd1', '00', 'ed', '20', 'fc', 'b1', '5b', '6a', 'cb', 'be', '39', '4a', '4c', '58','cf'],
            ['d0', 'ef', 'aa', 'fb', '43', '4d', '33', '85', '45', 'f9', '02', '7f', '50', '3c', '9f','a8'],
            ['51', 'a3', '40', '8f', '92', '9d', '38', 'f5', 'bc', 'b6', 'da', '21', '10', 'ff', 'f3','d2'],
            ['cd', '0c', '13', 'ec', '5f', '97', '44', '17', 'c4', 'a7', '7e', '3d', '64', '5d', '19','73'],
            ['60', '81', '4f', 'dc', '22', '2a', '90', '88', '46', 'ee', 'b8', '14', 'de', '5e', '0b','db'],
            ['e0', '32', '3a', '0a', '49', '06', '24', '5c', 'c2', 'd3', 'ac', '62', '91', '95', 'e4','79'],
            ['e7', 'c8', '37', '6d', '8d', 'd5', '4e', 'a9', '6c', '56', 'f4', 'ea', '65', '7a', 'ae','08'],
            ['ba', '78', '25', '2e', '1c', 'a6', 'b4', 'c6', 'e8', 'dd', '74', '1f', '4b', 'bd', '8b','8a'],
            ['70', '3e', 'b5', '66', '48', '03', 'f6', '0e', '61', '35', '57', 'b9', '86', 'c1', '1d','9e'],
            ['e1', 'f8', '98', '11', '69', 'd9', '8e', '94', '9b', '1e', '87', 'e9', 'ce', '55', '28','df'],
            ['8c', 'a1', '89', '0d', 'bf', 'e6', '42', '68', '41', '99', '2d', '0f', 'b0', '54', 'bb','16']]
    
    for i in range(4):
        if(arr[i][0] == 'a'):
            temp1 = 10
        elif(arr[i][0] == 'b'):
            temp1 = 11
        elif(arr[i][0] == 'c'):
            temp1 = 12
        elif(arr[i][0] == 'd'):
            temp1 = 13
        elif(arr[i][0] == 'e'):
            temp1 = 14
        elif(arr[i][0] == 'f'):
            temp1 = 15
        else:
            temp1 = int(arr[i][0])
        
        if(arr[i][1] == 'a'):
            temp2 = 10
        elif(arr[i][1] == 'b'):
            temp2 = 11
        elif(arr[i][1] == 'c'):
            temp2 = 12
        elif(arr[i][1] == 'd'):
            temp2 = 13
        elif(arr[i][1] == 'e'):
            temp2 = 14
        elif(arr[i][1] == 'f'):
            temp2 = 15
        else:
            temp2 = int(arr[i][1])

        result.append(sbox[temp1][temp2])

    return result

def keyExpansion(Key):
    w = []
    for i in range(4):
        w.append(Key[i])

    for i in range(4, 44):
        f = []
        div = []
        x = []
        temp = w[i-1]
        if(i%4 == 0):
            r = rotWord(temp)
            s = subWord(r)
            div.append(hex(2**((i//4)-1)).lstrip('0x'))
            if(len(div[0]) == 1):
                div[0] = '0' + div[0]
            elif(div[0] == '100'):
                div[0] = '1b'
            elif(div[0] == '200'):
                div[0] = '36'
            div.append('00')
            div.append('00')
            div.append('00')

            for j in range(4):
                x.append(hex(int(s[j], 16) ^ int(div[j], 16)).lstrip('0x'))
                if(len(x[j]) == 1):
                    x[j] = '0' + x[j]
                elif(len(x[j]) == 0):
                    x[j] = '00'
        
        else:
            x = temp
        
        for j in range(4):
            f.append(hex(int(x[j], 16) ^ int(w[i-4][j], 16)).lstrip('0x'))
            if(len(f[j]) == 1):
                f[j] = '0' + f[j]
            elif(len(f[j]) == 0):
                f[j] = '00'

        w.append(f)

    return w

def addRoundKey(state, key):
    result = []
    for r in range(4):
        temp = []
        for c in range(4):
            temp.append(hex(int(state[r][c], 16) ^ int(key[c][r], 16)).lstrip('0x'))
            if(len(temp[c]) == 1):
                temp[c] = '0' + temp[c]
            elif(len(temp[c]) == 0):
                temp[c] = '00'
        result.append(temp)
    return result

def mixColumns(matrix):
    m2 = []
    m3 = []
    mul2 = [['00','02','04','06','08','0a','0c','0e','10','12','14','16','18','1a','1c','1e'],
            ['20','22','24','26','28','2a','2c','2e','30','32','34','36','38','3a','3c','3e'],
            ['40','42','44','46','48','4a','4c','4e','50','52','54','56','58','5a','5c','5e'],
            ['60','62','64','66','68','6a','6c','6e','70','72','74','76','78','7a','7c','7e'],	
            ['80','82','84','86','88','8a','8c','8e','90','92','94','96','98','9a','9c','9e'],
            ['a0','a2','a4','a6','a8','aa','ac','ae','b0','b2','b4','b6','b8','ba','bc','be'],
            ['c0','c2','c4','c6','c8','ca','cc','ce','d0','d2','d4','d6','d8','da','dc','de'],
            ['e0','e2','e4','e6','e8','ea','ec','ee','f0','f2','f4','f6','f8','fa','fc','fe'],
            ['1b','19','1f','1d','13','11','17','15','0b','09','0f','0d','03','01','07','05'],
            ['3b','39','3f','3d','33','31','37','35','2b','29','2f','2d','23','21','27','25'],
            ['5b','59','5f','5d','53','51','57','55','4b','49','4f','4d','43','41','47','45'],
            ['7b','79','7f','7d','73','71','77','75','6b','69','6f','6d','63','61','67','65'],
            ['9b','99','9f','9d','93','91','97','95','8b','89','8f','8d','83','81','87','85'],
            ['bb','b9','bf','bd','b3','b1','b7','b5','ab','a9','af','ad','a3','a1','a7','a5'],
            ['db','d9','df','dd','d3','d1','d7','d5','cb','c9','cf','cd','c3','c1','c7','c5'],
            ['fb','f9','ff','fd','f3','f1','f7','f5','eb','e9','ef','ed','e3','e1','e7','e5']]
    
    mul3 = [['00','03','06','05','0c','0f','0a','09','18','1b','1e','1d','14','17','12','11'],
            ['30','33','36','35','3c','3f','3a','39','28','2b','2e','2d','24','27','22','21'],
            ['60','63','66','65','6c','6f','6a','69','78','7b','7e','7d','74','77','72','71'],
            ['50','53','56','55','5c','5f','5a','59','48','4b','4e','4d','44','47','42','41'],
            ['c0','c3','c6','c5','cc','cf','ca','c9','d8','db','de','dd','d4','d7','d2','d1'],
            ['f0','f3','f6','f5','fc','ff','fa','f9','e8','eb','ee','ed','e4','e7','e2','e1'],
            ['a0','a3','a6','a5','ac','af','aa','a9','b8','bb','be','bd','b4','b7','b2','b1'],
            ['90','93','96','95','9c','9f','9a','99','88','8b','8e','8d','84','87','82','81'],
            ['9b','98','9d','9e','97','94','91','92','83','80','85','86','8f','8c','89','8a'],
            ['ab','a8','ad','ae','a7','a4','a1','a2','b3','b0','b5','b6','bf','bc','b9','ba'],
            ['fb','f8','fd','fe','f7','f4','f1','f2','e3','e0','e5','e6','ef','ec','e9','ea'],
            ['cb','c8','cd','ce','c7','c4','c1','c2','d3','d0','d5','d6','df','dc','d9','da'],
            ['5b','58','5d','5e','57','54','51','52','43','40','45','46','4f','4c','49','4a'],
            ['6b','68','6d','6e','67','64','61','62','73','70','75','76','7f','7c','79','7a'],
            ['3b','38','3d','3e','37','34','31','32','23','20','25','26','2f','2c','29','2a'],
            ['0b','08','0d','0e','07','04','01','02','13','10','15','16','1f','1c','19','1a']]
    
    for i in range(4):
        tr = []
        tr2 = []
        for j in range(4):
            if(matrix[i][j][0] == 'a'):
                temp = 10
            elif(matrix[i][j][0] == 'b'):
                temp = 11
            elif(matrix[i][j][0] == 'c'):
                temp = 12
            elif(matrix[i][j][0] == 'd'):
                temp = 13
            elif(matrix[i][j][0] == 'e'):
                temp = 14
            elif(matrix[i][j][0] == 'f'):
                temp = 15
            else:
                temp = int(matrix[i][j][0])
            
            if(matrix[i][j][1] == 'a'):
                temp2 = 10
            elif(matrix[i][j][1] == 'b'):
                temp2 = 11
            elif(matrix[i][j][1] == 'c'):
                temp2 = 12
            elif(matrix[i][j][1] == 'd'):
                temp2 = 13
            elif(matrix[i][j][1] == 'e'):
                temp2 = 14
            elif(matrix[i][j][1] == 'f'):
                temp2 = 15
            else:
                temp2 = int(matrix[i][j][1])
            tr.append(mul2[temp][temp2])
            tr2.append(mul3[temp][temp2])
        m2.append(tr)
        m3.append(tr2)

    s0c = []
    s1c = []
    s2c = []
    s3c = []
    for c in range(4):
        h1 = hex(int(m2[0][c], 16) ^ int(m3[1][c], 16) ^ int(matrix[2][c], 16) ^ int(matrix[3][c], 16)).lstrip('0x')
        h2 = hex(int(matrix[0][c], 16) ^ int(m2[1][c], 16) ^ int(m3[2][c], 16) ^ int(matrix[3][c], 16)).lstrip('0x')
        h3 = hex(int(matrix[0][c], 16) ^ int(matrix[1][c], 16) ^ int(m2[2][c], 16) ^ int(m3[3][c], 16)).lstrip('0x')
        h4 = hex(int(m3[0][c], 16) ^ int(matrix[1][c], 16) ^ int(matrix[2][c], 16) ^ int(m2[3][c], 16)).lstrip('0x')

        if(len(h1) == 1):
            h1 = '0' + h1
        elif(len(h1) == 0):
            h1 = '00'
        if(len(h2) == 1):
            h2 = '0' + h2
        elif(len(h2) == 0):
            h2 = '00'
        if(len(h3) == 1):
            h3 = '0' + h3
        elif(len(h3) == 0):
            h3 = '00'
        if(len(h4) == 1):
            h4 = '0' + h4
        elif(len(h4) == 0):
            h4 = '00'
        s0c.append(h1)
        s1c.append(h2)
        s2c.append(h3)
        s3c.append(h4)

    result = [s0c, s1c, s2c, s3c]

    return result

def shiftRows(m):
    result = []
    for i in range(4):
        tr = []
        for j in range(4):
            if(i == 0):
                tr.append(m[i][j])
            elif(i == 1):
                tr.append(m[i][(j+1)%4])
            elif(i == 2):
                tr.append(m[i][(j+2)%4])
            else:
                tr.append(m[i][(j+3)%4])
        result.append(tr)
    
    return result

def subBytes(s):
    result = []
    sbox = [['63', '7c', '77', '7b', 'f2', '6b', '6f', 'c5', '30', '01', '67', '2b', 'fe', 'd7', 'ab', '76'],
            ['ca', '82', 'c9', '7d', 'fa', '59', '47', 'f0', 'ad', 'd4', 'a2', 'af', '9c', 'a4', '72','c0'],
            ['b7', 'fd', '93', '26', '36', '3f', 'f7', 'cc', '34', 'a5', 'e5', 'f1', '71', 'd8', '31','15'],
            ['04', 'c7', '23', 'c3', '18', '96', '05', '9a', '07', '12', '80', 'e2', 'eb', '27', 'b2','75'],
            ['09', '83', '2c', '1a', '1b', '6e', '5a', 'a0', '52', '3b', 'd6', 'b3', '29', 'e3', '2f','84'],
            ['53', 'd1', '00', 'ed', '20', 'fc', 'b1', '5b', '6a', 'cb', 'be', '39', '4a', '4c', '58','cf'],
            ['d0', 'ef', 'aa', 'fb', '43', '4d', '33', '85', '45', 'f9', '02', '7f', '50', '3c', '9f','a8'],
            ['51', 'a3', '40', '8f', '92', '9d', '38', 'f5', 'bc', 'b6', 'da', '21', '10', 'ff', 'f3','d2'],
            ['cd', '0c', '13', 'ec', '5f', '97', '44', '17', 'c4', 'a7', '7e', '3d', '64', '5d', '19','73'],
            ['60', '81', '4f', 'dc', '22', '2a', '90', '88', '46', 'ee', 'b8', '14', 'de', '5e', '0b','db'],
            ['e0', '32', '3a', '0a', '49', '06', '24', '5c', 'c2', 'd3', 'ac', '62', '91', '95', 'e4','79'],
            ['e7', 'c8', '37', '6d', '8d', 'd5', '4e', 'a9', '6c', '56', 'f4', 'ea', '65', '7a', 'ae','08'],
            ['ba', '78', '25', '2e', '1c', 'a6', 'b4', 'c6', 'e8', 'dd', '74', '1f', '4b', 'bd', '8b','8a'],
            ['70', '3e', 'b5', '66', '48', '03', 'f6', '0e', '61', '35', '57', 'b9', '86', 'c1', '1d','9e'],
            ['e1', 'f8', '98', '11', '69', 'd9', '8e', '94', '9b', '1e', '87', 'e9', 'ce', '55', '28','df'],
            ['8c', 'a1', '89', '0d', 'bf', 'e6', '42', '68', '41', '99', '2d', '0f', 'b0', '54', 'bb','16']]
    
    for i in range(4):
        tr = []
        for j in range(4):
            if(s[i][j][0] == 'a'):
                temp = 10
            elif(s[i][j][0] == 'b'):
                temp = 11
            elif(s[i][j][0] == 'c'):
                temp = 12
            elif(s[i][j][0] == 'd'):
                temp = 13
            elif(s[i][j][0] == 'e'):
                temp = 14
            elif(s[i][j][0] == 'f'):
                temp = 15
            else:
                temp = int(s[i][j][0])
            
            if(s[i][j][1] == 'a'):
                temp2 = 10
            elif(s[i][j][1] == 'b'):
                temp2 = 11
            elif(s[i][j][1] == 'c'):
                temp2 = 12
            elif(s[i][j][1] == 'd'):
                temp2 = 13
            elif(s[i][j][1] == 'e'):
                temp2 = 14
            elif(s[i][j][1] == 'f'):
                temp2 = 15
            else:
                temp2 = int(s[i][j][1])

            tr.append(sbox[temp][temp2])
        result.append(tr)

    return result

def enc(pt, key):
    cipher = []
    output = []
    aesCipher = []
    hexPT = toHEX(pt)
    ki = keyExpansion(key)
    print('Hex Input:', hexPT)
    print()
    for newPT in hexPT:
        state = [[newPT[r + 4*c] for c in range(4)] for r in range(4)]
        I0 = []
        for r in range(4):
            temp = []
            for c in range(4):
                temp.append(hex(int(state[r][c], 16) ^ int(ki[c][r], 16)).lstrip('0x'))
                if(len(temp[c]) == 1):
                    temp[c] = '0' + temp[c]
                elif(len(temp[c]) == 0):
                    temp[c] = '00'
            I0.append(temp)
        cipher = I0
        for round in range(1, 10):
            I1 = subBytes(cipher)
            I2 = shiftRows(I1)
            I3 = mixColumns(I2)

            rKey = []
            for i in range(4):
                rKey.append(ki[i+(round*4)])

            I4 = addRoundKey(I3, rKey)

            cipher = I4
        f1 = subBytes(cipher)
        f2 = shiftRows(f1)
        rKey = []
        for i in range(4):
            rKey.append(ki[40+i])
        cipher = addRoundKey(f2, rKey)

        output.append(cipher)

    for x in range(len(output)):
        for y in range(len(output[x])):
            for z in range(len(output[x][y])):
                aesCipher.append(output[x][z][y])

    print('AES Cipher:', aesCipher)
    print()

    return output