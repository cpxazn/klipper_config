# Pre-Requisites
1. Make sure your sensorless homing works well
2. Make sure your X axis homes to the right. This is setup in [stepper_x]. Both position_max and position_endstop should be setup properly.

# Instructions
1. Identify and separate different polarity magnets. There should be 6 of each. Same polarity will stack on top of each other (Flat side of one magnet sits on concave side of another). Different polarity magnets will attract on both concave sides.
2. Bridge this jumper to enable LED since we are using 5v
* <img src="https://github.com/tanaes/whopping_Voron_mods/blob/main/pcb_klicky/Images/5v.jpeg" width=400>
4. Add 3x heat set inserts to Connection_Fanhead_Klicky.stl
5. Add 3x heat set inserts to probe-heatset.stl
6. Add 1x M3 screw from the FYSETC kit into the hole in probe-heatset.stl
7. Insert main PCB into Connection_Fanhead_Klicky.stl
8. Insert magnet and screw into main PCB, you don't have to know the exact polarity of the magnets, but make sure you are using opposite polarities when diagram shows N/S
* <img src="https://github.com/tanaes/whopping_Voron_mods/blob/main/pcb_klicky/Images/magnets.jpeg" width=400>
10. Insert probe-heatset.stl onto the switch PCB
11. Insert magnet and screw into switch PCB, following diagram from step 7
12. If magnets were attached properly, both PCBs should attract each other
13. Attach Connection_Fanhead_Klicky.stl to your toolhead
14. Use JST crimp to crimp and attach wires to [BLtouch pins](https://github.com/bigtreetech/SKR-Pico/blob/master/Hardware/BTT%20SKR%20Pico%20V1.0-PIN.pdf) if using SKR Pico
15. Setup [probe] section in klipper. Use [probe.cfg](https://github.com/cpxazn/klipper_config/blob/main/backups/fluidd-100/probe.cfg) as example
16. While the probe is attached, the LED should light blue if you followed step 2
17. Use QUERY_ENDSTOPS command to test the switch. Resting state should show OPEN. Press the switch and it should show TRIGGERED. Detach the probe and it should show TRIGGERED.
18. Attach KlickyMount.stl to the frame with M3x20mm
19. Attach any magnet to the rear of dock-front_insert.stl. This magnet attracts the screw on probe-heatset.stl for docking.
20. Use 2x M3x40mm screws and nuts to secure dock-front_insert.stl and MountSpacer.stl to the mount
21. Adjust the height so it has a couple mm clearance below the magnets on Connection_Fanhead_Klicky.stl
22. Manually move the Y axis backwards to test whether it is able to attach the probe
23. Manually move the Y axis backwards to see if the probe can easily be seated back in the dock, then move the toolhead sideways to release
24. Once you are satisfied with the dock position, add [homing.cfg](https://github.com/cpxazn/klipper_config/blob/main/backups/fluidd-100/homing.cfg) macros to your config
25. Adjust the user variables at the top. Update Dock Location if required. You may want to lower some speeds until you have everything setup correctly.
26. (Optional) Add [screws.cfg](https://github.com/cpxazn/klipper_config/blob/main/backups/fluidd-100/screws.cfg) to enable additional functionality. Adjust according to your bed.
