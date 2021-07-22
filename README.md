# task_1
LVM automation 

Commands used 

#to create physical volume 
  sudo pvcreate /dev/sdc1 /dev/sdb1
#to destroy physical volume 
  sudo pvremove /dev/sdc1 /dev/sdb1
  
#to create volume group 
  sudo vgcreate /dev/sdc1 /dev/sdb1
#to destroy volume group 
  sudo vgremove vg_name
  
#to create logical volume 
  sudo lvcreate -n lv_name --size 1G vg_name
#to destroy logical volume
  sudo lvremove -ff lv_name 
  
#execution commands
  physical volume test 
    sudo python3 cli.py --disk /dev/sdc1 /dev/sdb1
    
  volume group test 
    sudo python3 cli.py --disk /dev/sdc1 /dev/sdb1 --vg_name vg_name
  
  logical volume 
    sudo python3 cli.py --disk /dev/sdc1 /dev/sdb1 --vg_name vg_name --lv_name lv_name --lv_size 1G 
