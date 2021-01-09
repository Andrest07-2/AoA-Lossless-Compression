import sys, time, os
start_time = time.time()
if len(sys.argv) == 2:
    print ("no file input")
else:
    path = "sample1.txt"
    fi = open(path,"rb")
    infile = bytearray(fi.read())
    size = len(infile)
    print ("Before Shannon-Fannon Compression the file size is", size, "bytes")
    freq = [0] * 256
    for b in infile:
        freq[b] += 1
    tuplist = []
    for i in range(256):
        tuplist.append([i, freq[i], ''])
    stuplist = sorted(tuplist, key = lambda tup: tup[1], reverse = True)
    for i in range(len(stuplist)):
        if stuplist[i][1] == 0:
            indzero = i
            break
    def finddivide(flist):
        diflist = []
        for k in range(len(flist)):
            sumA = 0
            sumB = 0
            for i in range(k):
                sumA += flist[i][1]
            for i in range(k, len(flist)):
                sumB += flist[i][1]
            dif = abs(sumA - sumB)
            diflist.append((k, dif))
        sdiflist = sorted(diflist, key = lambda dif: dif[1])
        return sdiflist[0][0]
    def sfencoder(list, d):
        if len(list) == 2:
            list[0][2] += '0'
            list[1][2] += '1'
            return True
        if len(list) == 1:
            if d == 'l':    list[0][2] += '0'
            elif d == 'r':  list[0][2] == '1'
            else: print ("illegal parameter")
            return True
        divpos = finddivide(list)
        for i in range(divpos):
            list[i][2] += '0'
        for i in range(divpos, len(list)):
            list[i][2] += '1'
        sfencoder(list[:divpos],'l')
        sfencoder(list[divpos:],'r')
        return list
    encodedlist = sfencoder(stuplist[:indzero],'l')
    sfdic = {}
    for i in range(len(encodedlist)):
        sfdic[encodedlist[i][0]] = encodedlist[i][2]
    newfile = ""
    for bite in infile:
        newfile += sfdic[bite] 
    listofbytes = []
    for i in range(len(newfile)//8):
        listofbytes.append(newfile[(i*8):(i*8+8)])
    lstlen = len(listofbytes[len(listofbytes)-1])
    if lstlen != 8:
        for i in range(8-lstlen):
            listofbytes[len(listofbytes)-1].append('0')
    dcmlst = []
    for strbyte in listofbytes:
        strbyte = bytearray(strbyte,'utf-8')
        u = 0
        for i in range(8):
            u += (strbyte[i]-48)*2**(7-i) 
        dcmlst.append(u)
    flst = bytearray(dcmlst)
    print("Compressed")
    #print (infile) #Uncompressed output
    #print (flst) #Compressed output
    filename, file_extension = os.path.splitext(path)
    output_path = filename + "_compressed_sf.txt"
    fi = open(output_path, "wb")
    fi.write(bytes(flst))
    fi.close()
    print ("After Shannon-Fannon Compression the file size is", len(flst), "bytes")
    try:
        print("Compression Ratio is", os.stat(path).st_size/os.stat(output_path).st_size)
    except:
        print("Compression Ratio is undefined, output size is 0 bytes.")
    print("This program took", time.time() - start_time, "to compress.")