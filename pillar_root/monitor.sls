#
# salt <minion> state.apply monitor
#

snmp_dev1:
  agent: '10.70.1.54'
  community: 'public'
  version: '1'
  control:
    '1.3.6.1.2.1.1.1.0': get
    '1.3.6.1.2.1.1.2.0': get
    '1.3.6.1.2.1.2': getNext
    '1.3.6.1.4.1.674.10895.5000.2.6132.1.1.1.1.4.1': get
    '1.3.6.1.4.1.674.10895.5000.2.6132.1.1.1.1.4.2': get
    '1.3.6.1.4.1.674.10895.5000.2.6132.1.1.1.1.4.3': get
    '1.3.6.1.4.1.674.10895.5000.2.6132.1.1.1.1.4.3.1.1': get
    '1.3.6.1.4.1.674.10895.5000.2.6132.1.1.1.1.4.3.1.2': get
    '1.3.6.1.4.1.674.10895.5000.2.6132.1.1.1.1.4.4.0': get
    '1.3.6.1.4.1.674.10895.5000.2.6132.1.1.1.1.4.9': get
