cd ~/klipper_config
rm -f printer-*.cfg
cp -f *.c* config_backups/`uname -n`
git add config_backups
git add macros/*
git commit -m "pushed from klipper"
git push
