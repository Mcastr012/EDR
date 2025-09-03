# -*- coding: utf-8 -*-
from utils.common import *
from entity.behavior import *


class SysmonData(object):

    @classmethod
    def process_create_process(cls, eid, mid, props):
        """
        Event ID - 1
        <data name="RuleName" inType="win:UnicodeString" outType="xs:string" />
        <data name="UtcTime" inType="win:UnicodeString" outType="xs:string" />
        <data name="ProcessGuid" inType="win:GUID" />
        <data name="ProcessId" inType="win:UInt32" outType="win:PID" />
        <data name="Image" inType="win:UnicodeString" outType="xs:string" />
        <data name="FileVersion" inType="win:UnicodeString" outType="xs:string" />
        <data name="Description" inType="win:UnicodeString" outType="xs:string" />
        <data name="Product" inType="win:UnicodeString" outType="xs:string" />
        <data name="Company" inType="win:UnicodeString" outType="xs:string" />
        <data name="OriginalFileName" inType="win:UnicodeString" outType="xs:string" />
        <data name="CommandLine" inType="win:UnicodeString" outType="xs:string" />
        <data name="CurrentDirectory" inType="win:UnicodeString" outType="xs:string" />
        <data name="User" inType="win:UnicodeString" outType="xs:string" />
        <data name="LogonGuid" inType="win:GUID" />
        <data name="LogonId" inType="win:HexInt64" />
        <data name="TerminalSessionId" inType="win:UInt32" />
        <data name="IntegrityLevel" inType="win:UnicodeString" outType="xs:string" />
        <data name="Hashes" inType="win:UnicodeString" outType="xs:string" />
        <data name="ParentProcessGuid" inType="win:GUID" />
        <data name="ParentProcessId" inType="win:UInt32" outType="win:PID" />
        <data name="ParentImage" inType="win:UnicodeString" outType="xs:string" />
        <data name="ParentCommandLine" inType="win:UnicodeString" outType="xs:string" />
        """
        return ProcessBehavior({
            'parent': {
                'image': props[20],
                'cmdline': props[21],
                'guid': props[18],
            },
            'current': {
                'guid': props[2],
                'image': props[4],
                'cmdline': props[10],
                'user': props[12],
            },
            'file': {
                'hash': pickup_md5(props[17]),
                'sig': props[9],
                'path': props[11],
            },
            'datetime': datetime.strptime(props[1].split('.')[0], '%Y-%m-%d %H:%M:%S').isoformat(),
            'endpoint': {
                'uuid': mid,
            },
            'relation': 'create',
        })

    @classmethod
    def process_timestomp(cls, eid, mid, props):
        """
        Event ID - 2
        <data name="RuleName" inType="win:UnicodeString" outType="xs:string" />
        <data name="UtcTime" inType="win:UnicodeString" outType="xs:string" />
        <data name="ProcessGuid" inType="win:GUID" />
        <data name="ProcessId" inType="win:UInt32" outType="win:PID" />
        <data name="Image" inType="win:UnicodeString" outType="xs:string" />
        <data name="TargetFilename" inType="win:UnicodeString" outType="xs:string" />
        <data name="CreationUtcTime" inType="win:UnicodeString" outType="xs:string" />
        <data name="PreviousCreationUtcTime" inType="win:UnicodeString" outType="xs:string" />
        """
        return FileBehavior({
            'process': {
                'guid': props[2],
                'image': props[4],
            },
            'file': {
                'path': props[5],
            },
            'datetime': datetime.strptime(props[1].split('.')[0], '%Y-%m-%d %H:%M:%S').isoformat(),
            'endpoint': {
                'uuid': mid,
            },
            'relation': 'timestomp',
        })

    @classmethod
    def process_network(cls, eid, mid, props):
        """
        Event ID - 3
        <data name="RuleName" inType="win:UnicodeString" outType="xs:string" />
        <data name="UtcTime" inType="win:UnicodeString" outType="xs:string" />
        <data name="ProcessGuid" inType="win:GUID" />
        <data name="ProcessId" inType="win:UInt32" outType="win:PID" />
        <data name="Image" inType="win:UnicodeString" outType="xs:string" />
        <data name="User" inType="win:UnicodeString" outType="xs:string" />
        <data name="Protocol" inType="win:UnicodeString" outType="xs:string" />
        <data name="Initiated" inType="win:Boolean" />
        <data name="SourceIsIpv6" inType="win:Boolean" />
        <data name="SourceIp" inType="win:UnicodeString" outType="xs:string" />
        <data name="SourceHostname" inType="win:UnicodeString" outType="xs:string" />
        <data name="SourcePort" inType="win:UInt16" />
        <data name="SourcePortName" inType="win:UnicodeString" outType="xs:string" />
        <data name="DestinationIsIpv6" inType="win:Boolean" />
        <data name="DestinationIp" inType="win:UnicodeString" outType="xs:string" />
        <data name="DestinationHostname" inType="win:UnicodeString" outType="xs:string" />
        <data name="DestinationPort" inType="win:UInt16" />
        <data name="DestinationPortName" inType="win:UnicodeString" outType="xs:string" />
        """
        return NetworkBehavior({
            'process': {
                'image': props[4],
                'user': props[5],
                'guid': props[2],
            },
            'network': {
                'protocol': props[6],
                'clientip': props[9],
                'clientport': props[11],
                'rip': props[14],
                'rhost': props[15],
                'rport': props[16],
            },
            'file': {
                'path': props[4],
            },
            'datetime': datetime.strptime(props[1].split('.')[0], '%Y-%m-%d %H:%M:%S').isoformat(),
            'endpoint': {
                'uuid': mid,
                'ip': props[9],
            },
            'relation': 'socket',
        })

    @classmethod
    def process_driver(cls, eid, mid, props):
        """
        Event ID - 6
        <data name="RuleName" inType="win:UnicodeString" outType="xs:string" />
        <data name="UtcTime" inType="win:UnicodeString" outType="xs:string" />
        <data name="ImageLoaded" inType="win:UnicodeString" outType="xs:string" />
        <data name="Hashes" inType="win:UnicodeString" outType="xs:string" />
        <data name="Signed" inType="win:UnicodeString" outType="xs:string" />
        <data name="Signature" inType="win:UnicodeString" outType="xs:string" />
        <data name="SignatureStatus" inType="win:UnicodeString" outType="xs:string" />
        """
        return FileBehavior({
            'process': {
                'image': props[2],
            },
            'file': {
                'path': props[2],
                'hash': pickup_md5(props[3]),
                'sig': props[5],
                'type': 'driver',
            },
            'datetime': datetime.strptime(props[1].split('.')[0], '%Y-%m-%d %H:%M:%S').isoformat(),
            'endpoint': {
                'uuid': mid,
            },
            'relation': 'load',
        })

    @classmethod
    def process_imageload(cls, eid, mid, props):
        """
        Event ID - 7
        <data name="RuleName" inType="win:UnicodeString" outType="xs:string" />
        <data name="UtcTime" inType="win:UnicodeString" outType="xs:string" />
        <data name="ProcessGuid" inType="win:GUID" />
        <data name="ProcessId" inType="win:UInt32" outType="win:PID" />
        <data name="Image" inType="win:UnicodeString" outType="xs:string" />
        <data name="ImageLoaded" inType="win:UnicodeString" outType="xs:string" />
        <data name="FileVersion" inType="win:UnicodeString" outType="xs:string" />
        <data name="Description" inType="win:UnicodeString" outType="xs:string" />
        <data name="Product" inType="win:UnicodeString" outType="xs:string" />
        <data name="Company" inType="win:UnicodeString" outType="xs:string" />
        <data name="OriginalFileName" inType="win:UnicodeString" outType="xs:string" />
        <data name="Hashes" inType="win:UnicodeString" outType="xs:string" />
        <data name="Signed" inType="win:UnicodeString" outType="xs:string" />
        <data name="Signature" inType="win:UnicodeString" outType="xs:string" />
        <data name="SignatureStatus" inType="win:UnicodeString" outType="xs:string" />
        """
        return FileBehavior({
            'process': {
                'image': props[4],
                'guid': props[2],
            },
            'file': {
                'path': props[5],
                'hash': pickup_md5(props[11]),
                'sig': props[13],
                'type': 'image',
            },
            'datetime': datetime.strptime(props[1].split('.')[0], '%Y-%m-%d %H:%M:%S').isoformat(),
            'endpoint': {
                'uuid': mid,
            },
            'relation': 'load',
        })

    @classmethod
    def process_remotethread(cls, eid, mid, props):
        """
        Event ID - 8
        <data name="RuleName" inType="win:UnicodeString" outType="xs:string" />
        <data name="UtcTime" inType="win:UnicodeString" outType="xs:string" />
        <data name="SourceProcessGuid" inType="win:GUID" />
        <data name="SourceProcessId" inType="win:UInt32" outType="win:PID" />
        <data name="SourceImage" inType="win:UnicodeString" outType="xs:string" />
        <data name="TargetProcessGuid" inType="win:GUID" />
        <data name="TargetProcessId" inType="win:UInt32" outType="win:PID" />
        <data name="TargetImage" inType="win:UnicodeString" outType="xs:string" />
        <data name="NewThreadId" inType="win:UInt32" />
        <data name="StartAddress" inType="win:UnicodeString" outType="xs:string" />
        <data name="StartModule" inType="win:UnicodeString" outType="xs:string" />
        <data name="StartFunction" inType="win:UnicodeString" outType="xs:string" />
        """
        return ProcessBehavior({
            'parent': {
                'image': props[4],
                'guid': props[2],
            },
            'current': {
                'image': props[7],
                'guid': props[5],
                'calltrace': '{}!{}'.format(props[10], props[11])
            },
            'file': {
                'path': props[7],
            },
            'datetime': datetime.strptime(props[1].split('.')[0], '%Y-%m-%d %H:%M:%S').isoformat(),
            'endpoint': {
                'uuid': mid,
            },
            'relation': 'inject',
        })

    @classmethod
    def process_readfile(cls, eid, mid, props):
        """
        Event ID - 9
        <data name="RuleName" inType="win:UnicodeString" outType="xs:string" />
        <data name="UtcTime" inType="win:UnicodeString" outType="xs:string" />
        <data name="ProcessGuid" inType="win:GUID" />
        <data name="ProcessId" inType="win:UInt32" outType="win:PID" />
        <data name="Image" inType="win:UnicodeString" outType="xs:string" />
        <data name="Device" inType="win:UnicodeString" outType="xs:string" />
        """
        return FileBehavior({
            'process': {
                'image': props[4],
                'guid': props[2],
            },
            'file': {
                'path': props[5],
            },
            'datetime': datetime.strptime(props[1].split('.')[0], '%Y-%m-%d %H:%M:%S').isoformat(),
            'endpoint': {
                'uuid': mid,
            },
            'relation': 'read',
        })

    @classmethod
    def process_access_process(cls, eid, mid, props):
        """
        Event ID - 10
        <data name="RuleName" inType="win:UnicodeString" outType="xs:string" />
        <data name="UtcTime" inType="win:UnicodeString" outType="xs:string" />
        <data name="SourceProcessGUID" inType="win:GUID" />
        <data name="SourceProcessId" inType="win:UInt32" outType="win:PID" />
        <data name="SourceThreadId" inType="win:UInt32" />
        <data name="SourceImage" inType="win:UnicodeString" outType="xs:string" />
        <data name="TargetProcessGUID" inType="win:GUID" />
        <data name="TargetProcessId" inType="win:UInt32" outType="win:PID" />
        <data name="TargetImage" inType="win:UnicodeString" outType="xs:string" />
        <data name="GrantedAccess" inType="win:HexInt32" />
        <data name="CallTrace" inType="win:UnicodeString" outType="xs:string" />
        """
        return ProcessBehavior({
            'parent': {
                'image': props[5],
                'guid': props[2],
            },
            'current': {
                'image': props[8],
                'guid': props[6],
                'calltrace': props[10],
            },
            'file': {
                'path': props[5],
            },
            'datetime': datetime.strptime(props[1].split('.')[0], '%Y-%m-%d %H:%M:%S').isoformat(),
            'endpoint': {
                'uuid': mid,
            },
            'relation': 'access',
        })

    @classmethod
    def process_create_file(cls, eid, mid, props):
        """
        Event ID - 11
        <data name="RuleName" inType="win:UnicodeString" outType="xs:string" />
        <data name="UtcTime" inType="win:UnicodeString" outType="xs:string" />
        <data name="ProcessGuid" inType="win:GUID" />
        <data name="ProcessId" inType="win:UInt32" outType="win:PID" />
        <data name="Image" inType="win:UnicodeString" outType="xs:string" />
        <data name="TargetFilename" inType="win:UnicodeString" outType="xs:string" />
        <data name="CreationUtcTime" inType="win:UnicodeString" outType="xs:string" />

        Event ID - 15
        <data name="RuleName" inType="win:UnicodeString" outType="xs:string" />
        <data name="UtcTime" inType="win:UnicodeString" outType="xs:string" />
        <data name="ProcessGuid" inType="win:GUID" />
        <data name="ProcessId" inType="win:UInt32" outType="win:PID" />
        <data name="Image" inType="win:UnicodeString" outType="xs:string" />
        <data name="TargetFilename" inType="win:UnicodeString" outType="xs:string" />
        <data name="CreationUtcTime" inType="win:UnicodeString" outType="xs:string" />
        <data name="Hash" inType="win:UnicodeString" outType="xs:string" />
        """
        _data = {
            'process': {
                'image': props[4],
                'guid': props[2],
            },
            'file': {
                'path': props[5],
            },
            'datetime': datetime.strptime(props[1].split('.')[0], '%Y-%m-%d %H:%M:%S').isoformat(),
            'endpoint': {
                'uuid': mid,
            },
            'relation': 'create',
        }
        if eid == '15':
            _data['file']['type'] = 'stream'
            _data['file']['hash'] = pickup_md5(props[7])

        return FileBehavior(_data)

    @classmethod
    def process_reg(cls, eid, mid, props):
        """
        Event ID - 12
        <data name="RuleName" inType="win:UnicodeString" outType="xs:string" />
        <data name="EventType" inType="win:UnicodeString" outType="xs:string" />
        <data name="UtcTime" inType="win:UnicodeString" outType="xs:string" />
        <data name="ProcessGuid" inType="win:GUID" />
        <data name="ProcessId" inType="win:UInt32" outType="win:PID" />
        <data name="Image" inType="win:UnicodeString" outType="xs:string" />
        <data name="TargetObject" inType="win:UnicodeString" outType="xs:string" />

        Event ID - 13
        <data name="RuleName" inType="win:UnicodeString" outType="xs:string" />
        <data name="EventType" inType="win:UnicodeString" outType="xs:string" />
        <data name="UtcTime" inType="win:UnicodeString" outType="xs:string" />
        <data name="ProcessGuid" inType="win:GUID" />
        <data name="ProcessId" inType="win:UInt32" outType="win:PID" />
        <data name="Image" inType="win:UnicodeString" outType="xs:string" />
        <data name="TargetObject" inType="win:UnicodeString" outType="xs:string" />
        <data name="Details" inType="win:UnicodeString" outType="xs:string" />

        Event ID - 14
        <data name="RuleName" inType="win:UnicodeString" outType="xs:string" />
        <data name="EventType" inType="win:UnicodeString" outType="xs:string" />
        <data name="UtcTime" inType="win:UnicodeString" outType="xs:string" />
        <data name="ProcessGuid" inType="win:GUID" />
        <data name="ProcessId" inType="win:UInt32" outType="win:PID" />
        <data name="Image" inType="win:UnicodeString" outType="xs:string" />
        <data name="TargetObject" inType="win:UnicodeString" outType="xs:string" />
        <data name="NewName" inType="win:UnicodeString" outType="xs:string" />
        """
        _data = {
            'process': {
                'image': props[5],
                'guid': props[3],
            },
            'reg': {
                'path': props[6],
            },
            'file': {
                'path': props[5],
            },
            'datetime': datetime.strptime(props[2].split('.')[0], '%Y-%m-%d %H:%M:%S').isoformat(),
            'endpoint': {
                'uuid': mid,
            },
        }

        if eid == '12':
            _data['relation'] = 'open'
        elif eid == '13':
            _data['relation'] = 'update'
            _data['reg']['key'] = props[7]
        else:
            _data['relation'] = 'rename'
            _data['reg']['key'] = props[7]

        return RegistryBehavior(_data)

    @classmethod
    def process_pipe(cls, eid, mid, props):
        """
        Event ID - 17
        <data name="RuleName" inType="win:UnicodeString" outType="xs:string" />
        <data name="EventType" inType="win:UnicodeString" outType="xs:string" />
        <data name="UtcTime" inType="win:UnicodeString" outType="xs:string" />
        <data name="ProcessGuid" inType="win:GUID" />
        <data name="ProcessId" inType="win:UInt32" outType="win:PID" />
        <data name="PipeName" inType="win:UnicodeString" outType="xs:string" />
        <data name="Image" inType="win:UnicodeString" outType="xs:string" />

        Event ID - 18
        <data name="RuleName" inType="win:UnicodeString" outType="xs:string" />
        <data name="EventType" inType="win:UnicodeString" outType="xs:string" />
        <data name="UtcTime" inType="win:UnicodeString" outType="xs:string" />
        <data name="ProcessGuid" inType="win:GUID" />
        <data name="ProcessId" inType="win:UInt32" outType="win:PID" />
        <data name="PipeName" inType="win:UnicodeString" outType="xs:string" />
        <data name="Image" inType="win:UnicodeString" outType="xs:string" />
        """
        _data = {
            'process': {
                'image': props[6],
                'guid': props[3],
            },
            'file': {
                'path': props[5],
                'type': 'pipe',
            },
            'datetime': datetime.strptime(props[1].split('.')[0], '%Y-%m-%d %H:%M:%S').isoformat(),
            'endpoint': {
                'uuid': mid,
            },
        }
        if eid == '17':
            _data['relation'] = 'create'
        else:
            _data['relation'] = 'communicate'

        return FileBehavior(_data)

    @classmethod
    def process_wmi(cls, eid, mid, props):
        return None

    @classmethod
    def eventid_behavior_mappings(cls, eid):
        mappings = {
            '1': cls.process_create_process,
            '2': cls.process_timestomp,
            '3': cls.process_network,
            '6': cls.process_driver,
            '7': cls.process_imageload,
            '8': cls.process_remotethread,
            '9': cls.process_readfile,
            '10': cls.process_access_process,
            '11': cls.process_create_file,
            '12': cls.process_reg,
            '13': cls.process_reg,
            '14': cls.process_reg,
            '15': cls.process_create_file,
            '17': cls.process_pipe,
            '18': cls.process_pipe,
            '19': cls.process_wmi,
            '20': cls.process_wmi,
            '21': cls.process_wmi,
        }
        if eid in mappings.keys():
            return mappings[eid]
        else:
            return None
