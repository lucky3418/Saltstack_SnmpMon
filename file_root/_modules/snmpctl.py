'''
Module for controlling the SNMP agent
'''
import pysnmp
from pysnmp.entity.rfc3413.oneliner import cmdgen

def get(agent, oid='1.3.6.1.2.1.1.1.0', community='public', version='1'):
    '''
    Run a SNMP GET

    Args:
        agent (str) : IP address of SNMP agent
        oid (str) : MIB OID to get value, default '1.3.6.1.2.1.1.1.0' - 'sysDescr.0'
        community (str) : SNMP community. default 'public'
        version (int) : SNMP version. v2 if '2', otherwise v1. default v1

    Returns:
        data or error message
    '''

    agent = str(agent)
    oid = str(oid)
    community = str(community)
    version = str(version)

    oid_value = []
    for item in oid.split('.'):
        if item.strip():
            oid_value.append(int(item))
    if len(oid_value) < 2:
        return ("Error: invalid oid")

    if int(version) == 2:
        snmp_version = 1 # 1 means version SNMP v2c
    else:
        snmp_version = 0 # 0 means SNMP v1

    generator = cmdgen.CommandGenerator()
    comm_data = cmdgen.CommunityData('server', community, snmp_version) 
    transport = cmdgen.UdpTransportTarget((agent, 10161))

    real_fun = getattr(generator, 'getCmd')
    res = (errorIndication, errorStatus, errorIndex, varBinds)\
        = real_fun(comm_data, transport, (oid_value))

    if not errorIndication is None  or errorStatus is True:
        return ("Error: %s" % errorIndication)
    else:
        #return ('\n'.join([ '%s' % varBind for varBind in varBinds]))
        return ('\n'.join([ '%s = %s' % (oid, val) for oid, val in varBinds]))


def getNext(agent, oid='1.3.6.1.2.1.2.2.1', community='public', version='1'):
    '''
    Run a SNMP GETNEXT

    Args:
        agent (str) : IP address of SNMP agent
        oid (str) : MIB OID to get value, default '1.3.6.1.2.1.1.1.0' - 'sysDescr.0'
        community (str) : SNMP community. default 'public'
        version (int) : SNMP version. v2 if '2', otherwise v1. default v1

    Returns:
        data or error message
    '''

    agent = str(agent)
    oid = str(oid)
    community = str(community)
    version = str(version)

    oid_value = []
    for item in oid.split('.'):
        if item.strip():
            oid_value.append(int(item))
    if len(oid_value) < 2:
        return ("Error: invalid oid")

    if int(version) == 2:
        snmp_version = 1 # 1 means version SNMP v2c
    else:
        snmp_version = 0 # 0 means SNMP v1

    generator = cmdgen.CommandGenerator()
    comm_data = cmdgen.CommunityData('server', community, snmp_version) 
    transport = cmdgen.UdpTransportTarget((agent, 10161))

    real_fun = getattr(generator, 'nextCmd')
    res = (errorIndication, errorStatus, errorIndex, varBinds)\
        = real_fun(comm_data, transport, (oid_value))

    if not errorIndication is None  or errorStatus is True:
        return ("Error: %s" % errorIndication)
    else:
        #return ('\n'.join([ '%s' % (' = '.join(['%s' % x for x in varBind])) for varBind in varBinds]))
        return ('\n'.join([ ('\n'.join([ '%s = %s' % (oid, val) for oid, val in varBind])) for varBind in varBinds]))


def dump(msg) :
    return msg
