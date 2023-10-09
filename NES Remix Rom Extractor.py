import os

newpath = r"./roms" 
if not os.path.exists(newpath):
    os.makedirs(newpath)

def nesfix(x,y):
    # load rom
    with open(x, 'rb') as f:
        data = f.read()
    # remove header and footer
    data = data[64:]
    data = data[:-32]
    # save fixed rom
    with open("roms/"+y, 'wb') as f:
        f.write(data)

def fdsfix(a,b):
    # load rom
    with open(a, 'rb') as f:
        data = f.read()
    # remove header and footer
    data = data[48:]
    data = data[:-8224]
    # save fixed rom
    with open("roms/"+b, 'wb') as f:
        f.write(data)

romnames = [
    "F_DOCTORJ.bin",
    "F_GOLFJ.bin",
    "F_ICEHOCKEYJ.bin", #fds title
    "F_PUNCHOUTJ.bin", 
    "FACJ.bin",
    "FAHJ.bin",
    "FAJE.bin",
    "FAKE.bin",
    "FALE.bin",
    "FALJ.bin",
    "FAME.bin",
    "FAMJ.bin",
    "FANJ.bin",
    "FAPE.bin",
    "FAPJ.bin",
    "FCWE.bin",
    "FESJ.bin",
    "FEUJ.bin",
    "FGFE.bin",
    "WUP-FA4J.bin",
    "WUP-FA8E.bin",
    "WUP-FA8J.bin", #fds title
    "WUP-FA9J.bin", #fds title
    "WUP-FAAJ.bin",
    "WUP-FABJ.bin",
    "WUP-FACE.bin",
    "WUP-FACJ.bin",
    "WUP-FADE.bin",
    "WUP-FADJ.bin",
    "WUP-FAEJ.bin",
    "WUP-FAFJ.bin",
    "WUP-FAGJ.bin",
    "WUP-FAHE.bin",
    "WUP-FAHJ.bin",
    "WUP-FAJE.bin",
    "WUP-FAJJ.bin",
    "WUP-FAKE.bin",
    "WUP-FAME.bin",
    "WUP-FAMJ.bin",
    "WUP-FAWJ.bin",
    "WUP-FBAE.bin",
    "WUP-FBAJ.bin", #fds title
    "WUP-FBBE.bin",
    "WUP-FBBJ.bin", #fds title
    "WUP-FBCE.bin",
    "WUP-FBCJ.bin", #fds title
    "WUP-FBJE.bin",
    "WUP-FBJJ.bin"
    ]

romdata = {
    "F_DOCTORJ.bin" : "Dr. Mario (Japan, USA) (Rev 1).nes",
    "F_GOLFJ.bin" : "Golf (Japan) (En).nes",
    "F_ICEHOCKEYJ.bin" : "Ice Hockey (Japan).qd", #fds title
    "F_PUNCHOUTJ.bin" : "Punch-Out!! (Japan) (Gold Edition).nes",
    "FACJ.bin" : "Pinball (Japan, USA).nes",
    "FAHJ.bin" : "Tennis (Japan, USA).nes",
    "FAJE.bin" : "Ice Hockey (USA).nes",
    "FAKE.bin" : "Zelda no Densetsu 1 - The Hyrule Fantasy (Japan).nes",
    "FALE.bin" : "Baseball (USA, Europe).nes",
    "FALJ.bin" : "Baseball (Japan) (En).nes",
    "FAME.bin" : "Wario's Woods (USA).nes",
    "FAMJ.bin" : "Wario no Mori (Japan) (En).nes",
    "FANJ.bin" : "Urban Champion (World).nes",
    "FAPE.bin" : "NES Open Tournament Golf (USA).nes",
    "FAPJ.bin" : "Mario Open Golf (Japan) (Rev 1).nes",
    "FCWE.bin" : "Super Mario Bros. 3 (USA) (Rev 1).nes",
    "FESJ.bin" : "Clu Clu Land (World).nes",
    "FEUJ.bin" : "Donkey Kong 3 (World).nes",
    "FGFE.bin" : "Golf (USA).nes",
    "WUP-FA4J.bin" : "Wrecking Crew (World).nes",
    "WUP-FA8E.bin" : "Metroid (USA).nes",
    "WUP-FA8J.bin" : "Metroid (Japan) (Rev 3) (Wii and Wii U Virtual Console).qd", #fds title
    "WUP-FA9J.bin" : "Super Mario Bros. 2 (World) (GameCube, Wii and Wii U Virtual Console).qd", #fds title
    "WUP-FAAJ.bin" : "Super Mario Bros. (World).nes",
    "WUP-FABJ.bin" : "Super Mario Bros. 3 (Japan) (Rev 1).nes",
    "WUP-FACE.bin" : "Ice Climber (USA, Europe, Korea).nes",
    "WUP-FACJ.bin" : "Ice Climber (Japan) (En).nes",
    "WUP-FADE.bin" : "Kirby's Adventure (USA) (Rev 1).nes",
    "WUP-FADJ.bin" : "Hoshi no Kirby - Yume no Izumi no Monogatari (Japan).nes",
    "WUP-FAEJ.bin" : "Mario Bros. (World).nes",
    "WUP-FAFJ.bin" : "Donkey Kong (World) (Rev 1).nes",
    "WUP-FAGJ.bin" : "Excitebike (Japan, USA).nes",
    "WUP-FAHE.bin" : "Super Mario Bros. 2 (USA) (Rev 1).nes",
    "WUP-FAHJ.bin" : "Super Mario USA (Japan).nes",
    "WUP-FAJE.bin" : "Balloon Fight (USA).nes",
    "WUP-FAJJ.bin" : "Balloon Fight (Japan) (En).nes",
    "WUP-FAKE.bin" : "Punch-Out!! (USA).nes",
    "WUP-FAME.bin" : "Yoshi (USA).nes",
    "WUP-FAMJ.bin" : "Yoshi no Tamago (Japan).nes",
    "WUP-FAWJ.bin" : "Donkey Kong Jr. (World) (Rev 1).nes",
    "WUP-FBAE.bin" : "Legend of Zelda, The (USA).nes",
    "WUP-FBAJ.bin" : "Zelda no Densetsu - The Hyrule Fantasy (Japan) (Collector's Edition).qd", #fds title
    "WUP-FBBE.bin" : "Kid Icarus (USA, Europe) (Rev 1).nes",
    "WUP-FBBJ.bin" : "Hikari Shinwa - Palthena no Kagami (Japan).qd", #fds title
    "WUP-FBCE.bin" : "Zelda II - The Adventure of Link (USA).nes",
    "WUP-FBCJ.bin" : "Link no Bouken - The Legend of Zelda 2 (Japan) (Rev 1) (Collector's Edition).qd", #fds title
    "WUP-FBJE.bin" : "Yoshi's Cookie (USA).nes",
    "WUP-FBJJ.bin" : "Yoshi no Cookie (Japan).nes"
}

for i in range (len(romnames)):
    if i == 2 or i == 21 or i == 22 or i == 41 or i == 43 or i == 45:
        try:
            fdsfix(romnames[i], romdata[romnames[i]])
        except:
            print("Couldn't find "+romnames[i])
        else:
            print("Extracted "+romdata[romnames[i]])
    else:
        try:
            nesfix(romnames[i], romdata[romnames[i]])
        except:
            print("Couldn't find "+romnames[i])
        else:
            print("Extracted "+romdata[romnames[i]])

