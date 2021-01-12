# Naomi-GD-Rom-IP-Patcher

Patches IP.bin to allow for rebuilding a Naomi .GDI with Rebuild GDI's v1.2


# Requirements:

Python installed OR python39.dll in the executable folder.


# How to use:

Open the program and locate *IP.bin* in */bootsector* folder, it will patch + create a backup copy.


# Q&A

*How to extract a Naomi CHD in .GDI?

1) Use Chdman to uncompress a Naomi CHD into .GDI   (*example* "chdman.exe extractcd -i GDS-0008.chd monkeyball.gdi" )
2) Copy all Extracted tracks + GDI on a single folder
3) Drag folder on Extract GDI Image.bat ( Rebuild GDI's v1.2 program ) and it will create a "GAME-Extracted" folder where you'll find the actual binary files.


*How to rebuild a .GDI in CHD?

1) Use Naomi-GD-Rom-IP-Patcher, to patch IP.bin
2) Drag the "GAME-Extracted" folder on Build GDI Image.bat, and it will rebuild the gdi automatically
3) Recompress the gdi with (*example* "chdman.exe createcd -i monkeyball.GDI -o GDS-0008.CHD"

*I cannot see the game data in game binary!

1) Naomi GD roms does not use a filesystem akin to DC, all game resources are usually packed into a huge binary file with decryption on top.
You can decrypt the binary by using GD-Rom explorer or Descrypt providing the appropriate DES key.

# Legal disclaimer:

This project is intended exclusively for educational purposes and has no affiliation with SEGA or any other third party / tools developer. NaomiLib format, Naomi-GD-Rom-IP-Patcher, NLOBJPUT and games using it are exlusive property of SEGA. Blender NaomiLib importer Addon is a recreative project, no compensation has been offered for research and will not be accepted in any form.

