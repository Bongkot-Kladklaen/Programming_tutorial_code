ln = [10, 12, 7, 9, 18]
nb =bytearray(ln)
i_byte = bytes(254)
s_byte = bytes('Python', 'ascii')
filewb =open('bfile.dat', 'wb')
filewb.write(nb)
filewb.write(s_byte)
filewb.write(i_byte)
filewb.close()

filerb = open('bfile.dat', 'rb')
data = filerb.read(30)
print(data)
filerb.close()
