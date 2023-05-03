# Notes
By default, the probe will NOT dock automatically after homing. It will remember that the probe was already attached so if you home again, it will not try to reattach, it will automatically go to home Z. The fact that the probe is attached will be remembered even if the printer is turned off. Be careful not to move Z too low while it is attached or it may mess up the switch. You can even start a print with the probe attached **as long as you call BED_MESH_CALIBRATE**, it will dock the probe after taking bed mesh. If you don't call BED_MESH_CALIBRATE, then **make sure you update user variables to dock after home**.

# Pre-Requisites
1. Make sure your sensorless homing works well
2. Make sure your X axis homes to the right. This is setup in [stepper_x]. Both position_max and position_endstop should be setup properly.

# Instructions
1. Identify and separate different polarity magnets. There should be 6 of each. Same polarity will stack on top of each other. Flat side of one magnet sits on concave side of another. Different polarity magnets will attract on both concave sides.
2. Bridge this jumper to enable LED since we are using 5v
* <img src="https://github.com/tanaes/whopping_Voron_mods/blob/main/pcb_klicky/Images/5v.jpeg" width=400>
3. Add 3x heat set inserts to Connection_Fanhead_Klicky.stl
4. Add 3x heat set inserts to probe-heatset.stl
5. Add 1x M3 screw from the FYSETC kit into the hole in probe-heatset.stl
6. Insert main PCB into Connection_Fanhead_Klicky.stl
7. Insert magnet and screw into main PCB, you don't have to know the exact polarity of the magnets, but make sure you are using opposite polarities when diagram shows N/S
* <img src="https://github.com/tanaes/whopping_Voron_mods/blob/main/pcb_klicky/Images/magnets.jpeg" width=400>
8. Insert probe-heatset.stl onto the switch PCB
9. Insert magnet and screw into switch PCB, following diagram from step 7
10. If magnets were attached properly, both PCBs should attract each other
11. Attach Connection_Fanhead_Klicky.stl to your toolhead
12. Use JST crimp to crimp and attach wires to [BLtouch pins](https://github.com/bigtreetech/SKR-Pico/blob/master/Hardware/BTT%20SKR%20Pico%20V1.0-PIN.pdf) if using SKR Pico
13. Setup [probe] section in klipper. Use [probe.cfg](https://github.com/cpxazn/klipper_config/blob/main/backups/fluidd-100/probe.cfg) as example
14. While the probe is attached, the LED should light blue if you followed step 2
15. Use QUERY_ENDSTOPS command to test the switch. Resting state should show OPEN. Press the switch and it should show TRIGGERED. Detach the probe and it should show TRIGGERED
16. Attach KlickyMount.stl to the frame with M3x20mm
17. Attach any magnet to the rear of dock-front_insert.stl. This magnet attracts the screw on probe-heatset.stl for docking
18. Use 2x M3x40mm screws and nuts to secure dock-front_insert.stl and MountSpacer.stl to the mount
19. Adjust the height so it has a couple mm clearance below the magnets on Connection_Fanhead_Klicky.stl
20. Manually move the Y axis backwards to test whether it is able to attach the probe
21. Manually move the Y axis backwards to see if the probe can easily be seated back in the dock, then move the toolhead sideways to release
22. Once you are satisfied with the dock position, add [homing.cfg](https://github.com/cpxazn/klipper_config/blob/main/backups/fluidd-100/homing.cfg) macros to your config
23. Create a [variables.cfg](https://github.com/cpxazn/klipper_config/blob/main/backups/fluidd-100/variables.cfg). Remove last_probe and prints_til_probe unless you are also using all of my [other macros](https://github.com/cpxazn/klipper_config) under macros directory.
24. Adjust the user variables at the top. Update Dock Location if required. You may want to lower some speeds until you have everything setup correctly
25. (Optional) Add [screws.cfg](https://github.com/cpxazn/klipper_config/blob/main/backups/fluidd-100/screws.cfg) to enable additional functionality. Adjust according to your bed
26. Run G28 to home all axis. Get ready to power off in case anything goes wrong
27. You can run a DOCK_PROBE command to test docking
28. Run ATTACH_PROBE command to reattach after the printer is already homed
29. Once you are satisfied with attaching and docking, when the probe is attached, setup the probe Z-offset by using PROBE_CALIBRATE command. Once it probes the bed, use your hands to manually detatch the probe, then continue lower the nozzle until you have setup the offset. Then you can reattach the probe. and run a SAVE_CONFIG.
