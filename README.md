## Adds klipper macros for
- Email on completion
- Email on filament runout
- Git add, commit, push, pull
- Idle power off
- M600, Filament runout, pause, resume
- Creating new bed mesh after every X prints
  
## Pre-requisite
gcode_shell_command.sh required from https://github.com/th33xitus/kiauh/tree/master/scripts. Place in ~/klipper/klippy/extras.

## Configure Email
- Update vars.sh with your email details.
- Can use email to sms as well if you want a text message (varies between providers, search on google).
- Recipients are comma delimited

## Filament Sensor
- Configure filament sensor to call email macro by adding runout_code to your filament sensor section, then call M600 to perform runout actions to pause and eject filament
```
Sample Filament Motion Sensor

[filament_motion_sensor btt_sensor]
detection_length: 100.0
extruder: extruder
switch_pin: PA4
pause_on_runout: false
runout_gcode:
  {action_respond_info("RUNOUT: Filament runout")}
  RUN_SHELL_COMMAND CMD=SEND_EMAIL_RUNOUT
  M600
```

## Slicer settings
- Slicer start/end gcode should have START_PRINT and END_PRINT
- START_PRINT requires hotend temp and bed temp parameters passed in
```
Sample Cura START_PRINT
START_PRINT HOTEND={material_print_temperature_layer_0} BED={material_bed_temperature_layer_0}
```
- END_PRINT requires machine depth (Max Y) passed in.
```
Sample Cura END_PRINT
END_PRINT MACHINE_DEPTH={machine_depth}
```

## Add power device
- Add a power device in moonraker.conf in order for auto power off to work
```
Sample Tasmota Device

[power tasmota]
type: tasmota
address: tasmota-ender
restart_klipper_when_powered: True
```

## Configure git repository
- If you want to utilize the git pull/push macros, setup your git repository in ~/klipper_config
- Create directory with your hostname in ~/klipper_config/backups/<hostname> where it will backup your printer specific config files
  
## Re-create bed mesh after X prints
- Update prints_til_probe value in variables.cfg in order set your preferred X number of probes before re-creating bed mesh
