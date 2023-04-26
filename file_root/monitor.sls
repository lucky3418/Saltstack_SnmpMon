#
# salt <minion> state.apply monitor pillar='{"agent":"192.168.1.54", "community":"public", "version":"1"}'
#

#install_required:
#  pip.installed:
#    - name: pysnmp

#Update modules:
#  watch:
#    - pip: install_required
#  module.run:
#    - name: saltutil.sync_modules

{% for devname, devparam in pillar.items() %}
{% if devname | regex_match('snmp_dev(.*)', ignorecase=True) != None %}

{% set agent_key = [devname, 'agent'] | join(':') %}
{% set agent = salt.pillar.get(agent_key) %}
{% set community_key = [devname, 'community'] | join(':') %}
{% set community = salt.pillar.get(community_key) %}
{% set version_key = [devname, 'version'] | join(':') %}
{% set version = salt.pillar.get(version_key) %}
{% set control_key = [devname, 'control'] | join(':') %}

update_st_snmp_{{ devname }}:
  event:
    - send
    - name: st/snmp/update
    - data:
      {% for oid, method in salt.pillar.get(control_key).items() %}
      {% if method == 'getNext' %}
        {% set snmp = salt[ 'snmpctl.getNext' ](agent, oid, community, version) %}
      {% else %}
        {% set snmp = salt[ 'snmpctl.get' ](agent, oid, community, version) %}
      {% endif %}
      snmp_{{ oid }}: {{ snmp | json }}
      {% endfor %}

{% endif %}
{% endfor %}
