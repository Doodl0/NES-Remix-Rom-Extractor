# NES Remix Rom Extractor
A simple Python script to extract the roms from NES Remix and NES Remix 2
The script just removes the custom header and footer of the rom to make them playable, then adds an NES 2.0 header if the database file is added
I have only tested this on the European versions and I have not tested NES Remix Pack.
If you have tested this on other versions, please let me know.

# Usage
Simply place any of the 3 Python files in #\content\emu\rom (# being the directory to your dump of the game, e.g. "mlc01\usr\title\00050000\10146100").
Then run the file with Python, and a folder called "roms" should be generated, with the fixed roms inside.

If you are using an emulator that requires iNES headers, you will need to download <a href="https://forums.nesdev.org/viewtopic.php?f=3&t=19940">this database<a>. Place it in the same folder as the Python file and run it in Python and all the .nes roms should have headers added.

# Roms
## Note: 
Famicom Disk System games are in a .qd format, which won't be read by most emulators. You can convert them to .fds with a tool like  <a href="https://gist.github.com/einstein95/6545066905680466cdf200c4cc8ca4f0">qd2fds.py<a>, which you use by placing it in the same directory as the .qd files, opening the command line there and typing `python qd2fds.py <ROM>`. You can also do `python qd2fds.py -h` to read all options.

## NES Remix
In NES Remix there are 36 roms.
The full list is:
```
Balloon Fight (Japan) (En).nes
Balloon Fight (USA).nes
Baseball (Japan) (En).nes
Baseball (USA, Europe).nes
Clu Clu Land (World).nes
Donkey Kong (World) (Rev 1).nes
Donkey Kong 3 (World).nes
Donkey Kong Jr. (World) (Rev 1).nes
Dr. Mario (Japan, USA) (Rev 1).nes
Excitebike (Japan, USA).nes
Golf (Japan) (En).nes
Golf (USA).nes
Hikari Shinwa - Palthena no Kagami (Japan).qd
Hoshi no Kirby - Yume no Izumi no Monogatari (Japan).nes
Ice Climber (Japan) (En).nes
Ice Climber (USA, Europe, Korea).nes
Ice Hockey (Japan).qd
Legend of Zelda, The (USA).nes
Link no Bouken - The Legend of Zelda 2 (Japan) (Rev 1) (Collector's Edition).qd
Mario Bros. (World).nes
Mario Open Golf (Japan) (Rev 1).nes
Metroid (Japan) (Rev 3) (Wii and Wii U Virtual Console).qd
Pinball (Japan, USA).nes
Punch-Out!! (Japan) (Gold Edition).nes
Super Mario Bros. (World).nes
Super Mario Bros. 2 (World) (GameCube, Wii and Wii U Virtual Console).qd
Super Mario Bros. 3 (Japan) (Rev 1).nes
Super Mario USA (Japan).nes
Tennis (Japan, USA).nes
Urban Champion (World).nes
Wario no Mori (Japan) (En).nes
Wrecking Crew (World).nes
Yoshi no Cookie (Japan).nes
Yoshi no Tamago (Japan).nes
Zelda no Densetsu - The Hyrule Fantasy (Japan) (Collector's Edition).qd
Zelda no Densetsu 1 - The Hyrule Fantasy (Japan).nes
```
## NES Remix 2
In NES Remix there are 47 roms. Included in that are all NES Remix roms except `Punch-Out!! (Japan) (Gold Edition).nes`, as they are also in the files of the game.
The full list is:
```
Balloon Fight (Japan) (En).nes
Balloon Fight (USA).nes
Baseball (Japan) (En).nes
Baseball (USA, Europe).nes
Clu Clu Land (World).nes
Donkey Kong (World) (Rev 1).nes
Donkey Kong 3 (World).nes
Donkey Kong Jr. (World) (Rev 1).nes
Dr. Mario (Japan, USA) (Rev 1).nes
Excitebike (Japan, USA).nes
Golf (Japan) (En).nes
Golf (USA).nes
Hikari Shinwa - Palthena no Kagami (Japan).qd
Hoshi no Kirby - Yume no Izumi no Monogatari (Japan).nes
Ice Climber (Japan) (En).nes
Ice Climber (USA, Europe, Korea).nes
Ice Hockey (Japan).qd
Ice Hockey (USA).nes
Kid Icarus (USA, Europe) (Rev 1).nes
Kirby's Adventure (USA) (Rev 1).nes
Legend of Zelda, The (USA).nes
Link no Bouken - The Legend of Zelda 2 (Japan) (Rev 1) (Collector's Edition).qd
Mario Bros. (World).nes
Mario Open Golf (Japan) (Rev 1).nes
Metroid (Japan) (Rev 3) (Wii and Wii U Virtual Console).qd
Metroid (USA).nes
NES Open Tournament Golf (USA).nes
Pinball (Japan, USA).nes
Punch-Out!! (USA).nes
Super Mario Bros. (World).nes
Super Mario Bros. 2 (USA) (Rev 1).nes
Super Mario Bros. 2 (World) (GameCube, Wii and Wii U Virtual Console).qd
Super Mario Bros. 3 (Japan) (Rev 1).nes
Super Mario Bros. 3 (USA) (Rev 1).nes
Super Mario USA (Japan).nes
Tennis (Japan, USA).nes
Urban Champion (World).nes
Wario no Mori (Japan) (En).nes
Wario's Woods (USA).nes
Wrecking Crew (World).nes
Yoshi (USA).nes
Yoshi no Cookie (Japan).nes
Yoshi no Tamago (Japan).nes
Yoshi's Cookie (USA).nes
Zelda II - The Adventure of Link (USA).nes
Zelda no Densetsu - The Hyrule Fantasy (Japan) (Collector's Edition).qd
Zelda no Densetsu 1 - The Hyrule Fantasy (Japan).nes
```
