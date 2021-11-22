# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
import json
# from jsonschema import validate
# from jsonschema.validators import Draft4Validator


def getNetmaskToRoutingPrefix(netmask):
    # print ("netmask test: ", type(netmask), len(netmask))
    if netmask:
        # print ("yes")
        netmaskSplit = netmask.split(".")
        binary_str = ''
        for octet in netmaskSplit:
          # print("octet is:", octet)
          binary_str += bin(int(octet))[2:].zfill(8)
          # print (binary_str)
        return str(len(binary_str.rstrip('0')))
    return
def addressInNetwork(ip, net):
    print ("perform addressInnetowork test")
    print (ip, net, type(net))
    if ip != None and len(ip) > 0 and net != None and len(net) > 0:
        ipaddr = int(''.join([ '%02x' % int(x) for x in ip.split('.') ]), 16)

        netstr, bits = net.split('/')
        print ("netstr and bits", netstr, bits, type(netstr), len(netstr))
        # if bits is not None:
        #     print ("yes")
        # else:
        #     print ("NO")
        # if netstr != "None" and len(netstr) > 0 and bits != "None" and len(bits) >0:
        if netstr and bits != "None" and len(bits) >0:
            print ("execute options")
            netaddr = int(''.join([ '%02x' % int(x) for x in netstr.split('.') ]), 16)
            mask = (0xffffffff << (32 - int(bits))) & 0xffffffff
            print ("netaddr and mask is:", netaddr, mask)
            return (ipaddr & mask) == (netaddr & mask)
        return False
    return False


def test(h):
    for i in h['interfaces']: # get from tsnodes item in tss_gen/tsn_gen/tsn_gen_tsn_configuration.json
        print(i)
        if 'ip' in i and len(i['ip']) > 0:
            # print (i['ip'])
            print (stpbbNet['network'],getNetmaskToRoutingPrefix(stpbbNet['netmask']))
            if addressInNetwork(i['ip'],"{!s}/{!s}".format(stpbbNet['network'],getNetmaskToRoutingPrefix(stpbbNet['netmask']))):
                return i
        if 'vlanifs' in i and len(i['vlanifs'])>0:
            for vlanif in i['vlanifs']:
              if 'ip' in vlanif and len(vlanif['ip'])>0:
                if addressInNetwork(vlanif['ip'],"{!s}/{!s}".format(stpbbNet['network'],getNetmaskToRoutingPrefix(stpbbNet['netmask']))):
                  #create a new temp interface for this vlan
                  tmpif = {}
                  tmpif["ip"]     = vlanif['ip']
                  tmpif["ifname"] = "{!s}.{:d}".format(i['ifname'], vlanif['vid'])
                  tmpif["vid"]    = vlanif['vid']
                  tmpif["rawdev"] = i['ifname']
                  if 'routing' in vlanif:
                    tmpif["routing"] = vlanif['routing']
                  if 'vips' in vlanif:
                    tmpif["vips"] = vlanif['vips']
                  print (tmpif)
                  return tmpif

    return None

# def _validateConfig(repose_data):
#   """
#   Validates json_cnf with json_schema, raise ConfigError if validation is not ok
#   otherwise it will return True
#   """
#   with open("test1.json", 'r') as k:
#       repose_data = json.load(k)
#   with open("schem1.json", 'r') as f:
#       dict_schema = json.load(f)
#   va = Draft4Validator(dict_schema)
#   va.validate(repose_data)
# # Press the green button in the gutter to run the script.
#
# def _readFileToJson(cnf_file):
#   """
#   Load cnf_file as a json string. Raise InstallerError
#   """
#   jstr = ""
#   try:
#     #read tni config
#     with open("{!s}".format(cnf_file)) as f:
#       jstr = json.load(f)
#   except Exception as e:
#     raise InstallerError("File {!s}: {!s}".format(os.path.basename(cnf_file),str(e)))
#
#   return jstr
if __name__ == '__main__':

    # json_obj = json.loads(qresult[0])
    tni_service_config_file="test1.json"
    tni_json_service_schema="schem1.json"
    stpbbNet={"netmask": "", "name": "internal", "network": "192.168.75.0"}
    h={"interfaces": [{
			"ip": "192.168.75.11",
			"mac": "",
			"ifname": "eth0"
		}, {
			"ip": "",
			"mac": "fa:16:3e:14:be:47",
			"ifname": "eth1"
		}, {
			"ip": "",
			"mac": "fa:16:3e:a1:58:45",
			"ifname": "eth2"
		}]}
    print (getNetmaskToRoutingPrefix(stpbbNet['netmask']), type(getNetmaskToRoutingPrefix(stpbbNet['netmask'])))
    test(h)
    # tni_json_service_cnf = _readFileToJson("{!s}".format(tni_service_config_file))
    #
    # _validateConfig()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
