import subprocess
from optparse import OptionParser
import re

parser = OptionParser()


def user_interface():
    parser.add_option("-i", "--interface", dest="interface", help="change to interface")
    parser.add_option("-m", "--mac_address", dest="mac_address", help="mac_address to change")
    return parser.parse_args()


def mac_change(user_interface1, user_mac):
    subprocess.call(["ifconfig", user_interface1, "down"])
    subprocess.call(["ifconfig", user_interface1, "hw", "ether", user_mac])
    subprocess.call(["ifconfig", user_interface1, "up"])


def control_new_mac(interface):
    ifconfig = subprocess.check_output(["ifconfig", interface])
    new_mac=re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w",str(ifconfig))
    if new_mac:
        return new_mac.group(0)
    else:
        return None


(user_input, args) = user_interface()

mac_change(user_input.interface, user_input.mac_address)
finalized_mac=control_new_mac(str(user_input.interface))
if finalized_mac== user_input.mac_address:
    print("Success!")
else:
    print("Error!")
