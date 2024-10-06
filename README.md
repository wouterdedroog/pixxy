# Pixxy

Pixxy is a physical remote control for PixMob bracelets using a custom PCB, based on a Raspberry Pi Pico and
MicroPython. The PCB design is available in the [pixxy-kicad](pixxy-kicad) folder. I used KiCad 8 to design this PCB.

## Branches
- [main](/wouterdedroog/pixxy/tree/main) - Full project details and PCB design based on the RP2040 chip (has USB-C)
- [pico](/wouterdedroog/pixxy/tree/pico) - PCB design based on the Raspberry Pi Pico (cheaper and easier to assemble)
- [src](/wouterdedroog/pixxy/tree/src) - MicroPython source, compatible with both variations of Pixxy device

## Current state
I ordered an initial version of the PCB which worked by soldering a Raspberry Pi Pico to the back, which worked 
perfectly. After this, I started working on a version that works using only the Raspberry Pi Pico chip, the RP2040. I
ordered a prototype PCB from JLCPCB and got it partially assembled (all SMD components were assembled there). This
worked great, and is the 'main' variation of the project.

Apart from the microcontroller part, the old PCB is identical to the new, RP2040 based, variation (that is in this 
branch) and has a 4×4 button array. Nine of these buttons are used for selecting colours. The ninth button selects a 
custom colour, using the three potentiometers above the buttons (RV1, RV2 and RV3). The input from these potentiometers
will be used to send an RGB colour.

The Fade and Flash buttons are used to send the command to the IR LED (connected to a 2N3904 transistor). The Once /
Repeat selector can be used to send the command once or continuously.

For X2 bracelets (the ones being used at Taylor Swift concerts), it is possible to set a colour indefinitely. The On and
Off buttons are used for this. The Taylor End button sends the end/go home signal used at concerts, which causes the
bracelet to loop through a set of colours until the battery runs out. The rainbow effect does the same effect, but with
all colours of the rainbow in order.

When the Speed Set button is held down, the value of the RV3 potentiometer influences the speed of the commands. This
means the potentiometer influences how long a fade or flash command lasts, and how much time is in between these
commands if the switch is in the repeat position.

![RP2040-based revision of the PCB](media/pixxy-pcb-render-rev2.png)

## Schematic
The PCB and schematic were made using KiCad 8. The project files are available in the
[pixxy-kicad directory](pixxy-kicad). A screenshot of the schematic can be found below:

![Schematic of Pixxy PCB](media/pixxy-schematic-rev2.png)

## Thanks
This project wouldn't have been possible without the research available in the
[pixmob-ir-reverse-engineering](https://github.com/danielweidman/pixmob-ir-reverse-engineering/) and 
[PixMob_IR](https://github.com/jamesw343/PixMob_IR/) repositories. The knowledge available in the
[PIXMOD Discord](https://discord.com/invite/UYqTjC7xp3) has also been super helpful.
