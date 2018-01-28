# Author:Sneha Mohan
# Program:TO turn LED On using GPIO

echo 2 > /sys/class/gpio/export
ls /sys/class/gpio/
echo "out" > /sys/class/gpio/gpio2/direction
echo 1 > /sys/class/gpio/gpio2/value
sleep 6
echo 0 > /sys/class/gpio/gpio2/value
echo 2 > /sys/class/gpio/unexport

