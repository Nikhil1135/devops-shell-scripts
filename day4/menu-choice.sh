##/bin/bash

echo "choose an action that you need to perform : "
echo "1.Show Date"
echo "2.Show Uptime"
echo "Show Disk Usage"
read -p "Enter your Choice [1:3]: " choice

case $choice in 
1)
date
;;
2)
uptime
;;
3)
df -h
;;
*)
echo "Invalid Choice"
;;
esac

