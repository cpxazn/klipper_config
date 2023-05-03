# Pre-Requisites
1. Make sure your sensorless homing works well
2. Make sure your X axis homes to the right. This is setup in [stepper_x]. Both position_max and position_endstop should be setup properly.

# Instructions
1. Identify and separate different polarity magnets. There should be 6 of each. Same polarity will stack on top of each other (Flat side of one magnet sits on concave side of another). Different polarity magnets will attract both concave sides.
2. Bridge this jumper to enable LED since we are using 5v
![5v jumper](https://github.com/tanaes/whopping_Voron_mods/blob/main/pcb_klicky/Images/5v.jpeg)
3. Add 3x heat set inserts to Connection_Fanhead_Klicky.stl
4. Add 3x heat set inserts to probe-heatset.stl
5. Add 1x M3 screw from the FYSETC kit into the hole in probe-heatset.stl
6. Insert main PCB into Connection_Fanhead_Klicky.stl
7. Insert magnet and screw into main PCB, you don't have to know the exact polarity of the magnets, but make sure you are using opposite polarities when diagram shows N/S
https://github.com/tanaes/whopping_Voron_mods/blob/main/pcb_klicky/Images/magnets.jpeg
8. Insert probe-heatset.stl onto the switch PCB
9. Insert magnet and screw into switch PCB, following diagram from step 7
10. If magnets were attached properly, both PCBs should attract each other
11. Attach Connection_Fanhead_Klicky.stl to your toolhead
12. Use JST crimp to crimp wires for BLtouch pins if using SKR Pico
13. Setup probe in klipper. Use above probe.cfg as example
14. While the probe is attached, the LED should light blue if you followed step 2
15. Use QUERY_ENDSTOPS command to test the switch. Resting state should show OPEN. Press the switch and it should show TRIGGERED. Detach the probe and it should show TRIGGERED.
16. Attach KlickyMount.stl to the frame with M3x20mm
17. Attach any magnet to the rear of dock-front_insert.stl
18. Use M3x40mm screw and nuts to secure dock-front_insert.stl and MountSpacer.stl to the mount
19. Adjust the height so it has a couple mm clearance
