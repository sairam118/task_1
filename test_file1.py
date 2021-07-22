import unittest 
import cli
from runner import subp

class Test_pv_create(unittest.TestCase):
    
    def setUp(self):
        print("step 1 : creating PV")
        subp(f"sudo pvcreate {cli.disk}")

    def tearDown(self):
        print("step 3 : removing pv")
        subp("sudo pvremove {cli.disk}")

    def testpv(self):
        print("step 2 : ")
        for i in cli.d:
            print(f"Test to chech {i} physical volume is created")
            self.assertRegex(subp("sudo pvdisplay").stdout, i)


class Test_vg_create(unittest.TestCase):

    def setUp(self):
        print("step 1 : creating pv and vg")
        subp(f"sudo pvcreate {cli.disk}")
        subp(f"sudo vgcreate {cli.vg_name} {cli.disk}")

    def tearDown(self):
        print("step 3 : deleting pv and vg")
        subp(f"sudo vgremove {cli.vg_name}")
        subp(f"sudo pvremove {cli.disk}")

    def testvg(self):
        print(f"Step 2 : Test to check {cli.vg_name} volume group is created")
        self.assertRegex(subp("sudo vgdisplay").stdout, cli.vg_name) 

class Test_lv_create(unittest.TestCase):

    def setUp(self):
        print("step 1 : creating pv and vg")
        subp(f"sudo pvcreate {cli.disk}")
        subp(f"sudo vgcreate {cli.vg_name} {cli.disk}")
        subp(f"sudo lvcreate -n {cli.lv_name} --size {cli.lv_size}G {cli.vg_name}")
       
    def tearDown(self):
        print("step 3 : deleting pv vg lv")
        subp(f"sudo lvremove -ff {cli.vg_name}")
        subp(f"sudo vgremove {cli.vg_name}")
        subp(f"sudo pvremove {cli.disk}")


    def testlv(self):
        print(f"Step 2 : Test to check {cli.lv_name} logical volume is created")
        self.assertRegex(subp(f"sudo lvdisplay").stdout, cli.lv_name)

    
