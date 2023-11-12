import os 

#create bios folder
newpath = r"./bios"  

if not os.path.exists(newpath): 
    os.makedirs(newpath) 

def fdsbiosfix(x,y): 
    # load rom 
    with open(x, 'rb') as f: 
        data = f.read() 
    # remove rom data and footer
    data=data[131136:] 
    data=data[:-16] 
    # fix different bytes 
    data=data[:569] + b"\x85" + data[569 + 1:]
    data=data[:1030] + b"\x85" + data[1030 + 1:]
    data=data[:1854] + b"\xA2" + data[1854 + 1:]
    data=data[:1855] + b"\xB2" + data[1855 + 1:]
    data=data[:1856] + b"\xCA" + data[1856 + 1:]
    data=data[:1956] + b"\x4C" + data[1956 + 1:]
    data=data[:3828] + b"\xA5" + data[3828 + 1:]
    # save fixed bios
    with open("bios/"+y, 'wb') as f: 
        f.write(data)

try: 
    fdsbiosfix("WUP-FBAJ.bin", "disksys.rom")
except:
    print("Couldn't find WUP-FBAJ.bin") 
else:
    print("Extracted disksys.rom") 