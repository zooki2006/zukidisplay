# zdm.py
a python script

how it works 
that looks in $HOME/.config/zdm/ and $HOME/.config/zdm/way/
for shell scripts lists them out and scripts in $HOME/.config/zdm/
when seleced it runs with sx <https://github.com/Earnestly/sx> or xinit with -x flag eg "sx sh script" and if there in $HOME/.config/zdm/way/
it runs "sh script" for wayland

how to use 
make the following dirs
$HOME/.config/zdm/
$HOME/.config/zdm/way/
then place scripts to run i3 or other xorg wm in the $HOME/.config/zdm/ folder
and if you use wayland place scripts to run wayland wm in $HOME/.config/zdm/way/

# zxdm.py
a python script that does the same as zdm.py but without wayland option and wayland cli flags
# zxdm
a shell script that lists files in $HOME/.config/zdm/
then runs with with sx <https://github.com/Earnestly/sx>
