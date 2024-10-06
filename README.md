# Pixxy (Raspberry Pi Pico)

Pixxy is a physical remote control for PixMob bracelets using a custom PCB. The PCB design is available in the 
[pixxy-kicad](pixxy-kicad) folder. I used KiCad 8 to design this PCB. There are currently two variations/revisions of 
this project. You're currently looking at the revision based on the Raspberry Pi Pico. This version is cheaper to 
manufacturer (since the soldering job is easier, and can be done manually). 

There is also a revision based on the RP2040 chip. This version requires machine assembly, which makes it more expensive
but offers a larger flash size (up to 128Mbit instead of 16Mbit) and uses USB-C instead of micro-USB. This revision can
be found [here](https://github.com//wouterdedroog/pixxy/tree/main). The MicroPython sourcecode found in the 
[src branch](https://github.com/wouterdedroog/pixxy/tree/src) is compatible with both hardware variations.

## Branches
- [main](https://github.com/wouterdedroog/pixxy/tree/main) - Full project details and PCB design based on the RP2040 chip (has USB-C)
- [pico](https://github.com//wouterdedroog/pixxy/tree/pico) - PCB design based on the Raspberry Pi Pico (cheaper and easier to assemble)
- [src](https://github.com/wouterdedroog/pixxy/tree/src) - MicroPython source, compatible with both variations of Pixxy device

## Schematic of Pico-based version
The PCB and schematic were made using KiCad 8. The project files are available in the
[pixxy-kicad directory](pixxy-kicad). A screenshot of the schematic can be found below:

![Schematic of Pixxy PCB](media/pixxy-schematic-rev1.png)
