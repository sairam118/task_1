import argparse
import unittest

parser = argparse.ArgumentParser() 
parser.add_argument("--disk", nargs='+', help="disk path")
parser.add_argument("--vg_name", help="volume group name")
parser.add_argument("--lv_name", help="logical volume name")
parser.add_argument("--lv_size", help="logical volume size", type = int)
parser.add_argument("--test", help="test name",choices=["Test_pv_create", "Test_vg_create", "Test_lv_create"])
args = parser.parse_args()
d = args.disk
disk = " ".join(args.disk)
vg_name = args.vg_name
lv_name = args.lv_name
lv_size = args.lv_size
test = args.test

if __name__ == '__main__':
    import test_file1
    testLoad = unittest.TestLoader()
    testSuite = testLoad.loadTestsFromName(test, module=test_file1)
    runner = unittest.TextTestRunner()
    runner.run(testSuite)

