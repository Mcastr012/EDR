# User

## GET /user

Get the profile of the current user using current session id.

### Request

#### Header

```
application/json
```

#### Body

```json
{
    "sessionID" : "f94e7cd0-6e10-11ea-8a3d-000d3a185820"
}
```

### Response

#### Header

```
application/json
```

#### Body

```json
{
    "success": true,
    "errMsg": null,
    "content": 
    {
        "uid": "4",
        "name": "John",
        "email": "aaa@wa.com",
        "phone": "51829838475"
    } 
}
```

## PUT /user

Update the profile of the current user.

### Request

#### Header

```
application/json
```

#### Body

```json
{
    "sessionID": "213123-123-123-213-3123",
    "name": "John",
    "email": "aaa@wa.com",
    "phone": "51829838475",
    "newPassword" : "new123456"
}
```

### Response

#### Header

```
application/json
```

#### Body

```json
{
    "success": true,
    "errMsg": null,
    "content": {}
}
```

## POST /user

Create a new user.

### Request

#### Header

```
application/json
```

#### Body

```json
{
    "name": "John",
    "email": "aaa@wa.com",
    "phone": "51829838475",
    "password" : "123456"
}
```

### Response

#### Header

```
application/json
```

#### Body

```json
{
    "success": true,
    "errMsg": null,
    "content": 
    {
        "msg": "User added successfully"
    }
}
```

## DELETE /user

Delete current user.

### Request

#### Header

```
application/json
```

#### Body

```json
{
    "sessionID": "12312-321-3-12-3",
    "password" : "123456"
}
```

### Response

#### Header

```
application/json
```

#### Body

```json
{
    "success": true,
    "errMsg": null,
    "content": 
    {   
        "uid": "213-2-321-3-12-3",
        "msg": "Failed to delete user."
    }
}
```

# Session

## POST /session

Log in the user account and create the session.

### Request

#### Header

```
application/json
```

#### Body

```json
{
  "email" : "test@gmail.com",
  "password" : "testtest"
}
```

### Response

#### Header

```
application/json
```

#### Body

```json
{
  "success": true,
  "errMsg": null,
  "content": {
    "sessionID": "d635029a-6e16-11ea-b53e-000d3a185820",
    "startTime": "2020-03-24 21:31:35.035596",
    "uid": 2
  }
}
```

## DELETE /session

Log out the user account and end the session.

### Request

#### Header

```
application/json
```

#### Body

```json
{
  "sessionID" : "d635029a-6e16-11ea-b53e-000d3a185820"
}
```

### Response

#### Header

```
application/json
```

#### Body

```json
{
  "success": true,
  "errMsg": null,
  "content": {
    "endTime": "2020-03-24 21:34:24.369808",
    "sessionID": "d635029a-6e16-11ea-b53e-000d3a185820"
  }
}
```

# Behavior
## GET /behavior
Get the behavior records based on endpoint ID. Here are 4 kinds of behavior: ProcessBehavior, RegistryBehavior, NetworkBehavior and FileBehavior. Different type of behavior has different response attributes.
### Request
#### Header
```
application/json
```
#### Body
```json
{
    "behaviorType" : "RegistryBehavior",
    "endpointID" : "DESKTOP-3LRRD6K",
    "startDate" : "2020-04-06",
    "endDate" : "2020-04-06",
    "pageSize" : "10",
    "pageIndex" : "0"
}
```
### Response
#### Header
```
application/json
```
#### Body (RegistryBehavior)
```json
{
    "success": true,
    "errMsg": null,
    "content": [
    {
      "attckids": "",
      "behaviortype": "RegistryBehavior",
      "endpoint.ip": "",
      "endpoint.uuid": "f999ac48f7421fa951545ce34f41a998",
      "file.hash": "",
      "file.name": "",
      "file.path": "C:\\Windows\\System32\\DriverStore\\FileRepository\\nv_dispui.inf_amd64_ff3f7ca38047a5aa\\Display.NvContainer\\NVDisplay.Container.exe",
      "file.sig": "",
      "file.type": "",
      "process.calltrace": "",
      "process.cmdline": "",
      "process.guid": "{3c251a4e-fc36-5e88-0000-00104ed4dc54}",
      "process.image": "C:\\Windows\\System32\\DriverStore\\FileRepository\\nv_dispui.inf_amd64_ff3f7ca38047a5aa\\Display.NvContainer\\NVDisplay.Container.exe",
      "process.pid": "",
      "process.user": "",
      "reg.key": "DWORD (0x00000001)",
      "reg.path": "HKLM\\System\\CurrentControlSet\\Services\\nvlddmkm\\Global\\NVTweak\\PowerMode",
      "reg.value": "",
      "relation": "update",
      "timestamp": "2020-04-06T22:37:26",
      "value": "b'C:\\\\Windows\\\\System32\\\\DriverStore\\\\FileRepository\\\\nv_dispui.inf_amd64_ff3f7ca38047a5aa\\\\Display.NvContainer\\\\NVDisplay.Container.exe' -update-> b'HKLM\\\\System\\\\CurrentControlSet\\\\Services\\\\nvlddmkm\\\\Global\\\\NVTweak\\\\PowerMode' b'DWORD (0x00000001)' "
    },
    {
      "attckids": "",
      "behaviortype": "RegistryBehavior",
      "endpoint.ip": "",
      "endpoint.uuid": "f999ac48f7421fa951545ce34f41a998",
      "file.hash": "",
      "file.name": "",
      "file.path": "C:\\Windows\\system32\\ctfmon.exe",
      "file.sig": "",
      "file.type": "",
      "process.calltrace": "",
      "process.cmdline": "",
      "process.guid": "{3c251a4e-fce5-5e88-0000-00104131e954}",
      "process.image": "C:\\Windows\\system32\\ctfmon.exe",
      "process.pid": "",
      "process.user": "",
      "reg.key": "Binary Data",
      "reg.path": "HKU\\S-1-5-21-3759431645-610626447-2289912213-1001\\Software\\Microsoft\\Input\\Settings\\Insights",
      "reg.value": "",
      "relation": "update",
      "timestamp": "2020-04-06T22:37:26",
      "value": "b'C:\\\\Windows\\\\system32\\\\ctfmon.exe' -update-> b'HKU\\\\S-1-5-21-3759431645-610626447-2289912213-1001\\\\Software\\\\Microsoft\\\\Input\\\\Settings\\\\Insights' b'Binary Data' "
    }
	]
}
```
#### Body (ProcessBehavior)
```json
{
    "success": true,
    "errMsg": null,
    "content": [
    {
      "attckids": "",
      "behaviortype": "ProcessBehavior",
      "current.calltrace": "",
      "current.cmdline": "C:\\Windows\\system32\\svchost.exe -k BcastDVRUserService -s BcastDVRUserService",
      "current.guid": "{3c251a4e-af20-5e8b-0000-00107b606882}",
      "current.image": "C:\\Windows\\System32\\svchost.exe",
      "current.pid": "",
      "current.user": "DESKTOP-3LRRD6K\\liabe",
      "endpoint.ip": "",
      "endpoint.uuid": "f999ac48f7421fa951545ce34f41a998",
      "file.hash": "9520A99E77D6196D0D09833146424113,SHA256",
      "file.name": "",
      "file.path": "C:\\Windows\\system32\\",
      "file.sig": "svchost.exe",
      "file.type": "",
      "parent.calltrace": "",
      "parent.cmdline": "C:\\Windows\\system32\\services.exe",
      "parent.guid": "{3c251a4e-7831-5e85-0000-001079b10000}",
      "parent.image": "C:\\Windows\\System32\\services.exe",
      "parent.pid": "",
      "parent.user": "",
      "relation": "create",
      "timestamp": "2020-04-06T22:37:20",
      "value": "(C:\\Windows\\System32\\services.exe C:\\Windows\\system32\\services.exe) -create-> (C:\\Windows\\System32\\svchost.exe C:\\Windows\\system32\\svchost.exe -k BcastDVRUserService -s BcastDVRUserService)"
    },
    {
      "attckids": "",
      "behaviortype": "ProcessBehavior",
      "current.calltrace": "",
      "current.cmdline": "\"C:\\Windows\\system32\\SearchProtocolHost.exe\" Global\\UsGthrFltPipeMssGthrPipe508_ Global\\UsGthrCtrlFltPipeMssGthrPipe508 1 -2147483646 \"Software\\Microsoft\\Windows Search\" \"Mozilla/4.0 (compatible; MSIE 6.0; Windows NT; MS Search 4.0 Robot)\" \"C:\\ProgramData\\Microsoft\\Search\\Data\\Temp\\usgthrsvc\" \"DownLevelDaemon\" ",
      "current.guid": "{3c251a4e-af2d-5e8b-0000-001078906a82}",
      "current.image": "C:\\Windows\\System32\\SearchProtocolHost.exe",
      "current.pid": "",
      "current.user": "NT AUTHORITY\\SYSTEM",
      "endpoint.ip": "",
      "endpoint.uuid": "f999ac48f7421fa951545ce34f41a998",
      "file.hash": "2EF0A0531B2566153D9A3DF4160F650B,SHA256",
      "file.name": "",
      "file.path": "C:\\Windows\\system32\\",
      "file.sig": "SearchProtocolHost.exe",
      "file.type": "",
      "parent.calltrace": "",
      "parent.cmdline": "C:\\Windows\\system32\\SearchIndexer.exe /Embedding",
      "parent.guid": "{3c251a4e-7839-5e85-0000-00102e170a00}",
      "parent.image": "C:\\Windows\\System32\\SearchIndexer.exe",
      "parent.pid": "",
      "parent.user": "",
      "relation": "create",
      "timestamp": "2020-04-06T22:37:33",
      "value": "(C:\\Windows\\System32\\SearchIndexer.exe C:\\Windows\\system32\\SearchIndexer.exe /Embedding) -create-> (C:\\Windows\\System32\\SearchProtocolHost.exe \"C:\\Windows\\system32\\SearchProtocolHost.exe\" Global\\UsGthrFltPipeMssGthrPipe508_ Global\\UsGthrCtrlFltPipeMssGthrPipe508 1 -2147483646 \"Software\\Microsoft\\Windows Search\" \"Mozilla/4.0 (compatible; MSIE 6.0; Windows NT; MS Search 4.0 Robot)\" \"C:\\ProgramData\\Microsoft\\Search\\Data\\Temp\\usgthrsvc\" \"DownLevelDaemon\" )"
    }
	]
}
```
#### Body (ProcessBehavior)
```json
{
    "success": true,
    "errMsg": null,
    "content": [
    {
      "attckids": "",
      "behaviortype": "NetworkBehavior",
      "endpoint.ip": "2604:6000:1111:a119:6187:1a97:9515:8220",
      "endpoint.uuid": "f999ac48f7421fa951545ce34f41a998",
      "file.hash": "",
      "file.name": "",
      "file.path": "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe",
      "file.sig": "",
      "file.type": "",
      "network.clientip": "2604:6000:1111:a119:6187:1a97:9515:8220",
      "network.clientport": "53816",
      "network.protocol": "udp",
      "network.rhost": "lga25s62-in-x0e.1e100.net",
      "network.rip": "2607:f8b0:4006:81a:0:0:0:200e",
      "network.rport": "443",
      "network.ua": "",
      "network.url": "",
      "process.calltrace": "",
      "process.cmdline": "",
      "process.guid": "{3c251a4e-62c2-5e8b-0000-00107c3cab77}",
      "process.image": "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe",
      "process.pid": "",
      "process.user": "DESKTOP-3LRRD6K\\liabe",
      "relation": "socket",
      "timestamp": "2020-04-06T22:37:35",
      "value": "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe -socket-> lga25s62-in-x0e.1e100.net(2607:f8b0:4006:81a:0:0:0:200e)"
    },
    {
      "attckids": "",
      "behaviortype": "NetworkBehavior",
      "endpoint.ip": "192.168.1.46",
      "endpoint.uuid": "f999ac48f7421fa951545ce34f41a998",
      "file.hash": "",
      "file.name": "",
      "file.path": "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe",
      "file.sig": "",
      "file.type": "",
      "network.clientip": "192.168.1.46",
      "network.clientport": "50414",
      "network.protocol": "tcp",
      "network.rhost": "submitty-srv2.cs.rpi.edu",
      "network.rip": "128.113.28.58",
      "network.rport": "443",
      "network.ua": "",
      "network.url": "",
      "process.calltrace": "",
      "process.cmdline": "",
      "process.guid": "{3c251a4e-62c2-5e8b-0000-00107c3cab77}",
      "process.image": "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe",
      "process.pid": "",
      "process.user": "DESKTOP-3LRRD6K\\liabe",
      "relation": "socket",
      "timestamp": "2020-04-06T22:37:36",
      "value": "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe -socket-> submitty-srv2.cs.rpi.edu(128.113.28.58)"
    }
	]
}
```
#### Body (FileBehavior)
```json
{
    "success": true,
    "errMsg": null,
    "content": [
    {
      "attckids": "",
      "behaviortype": "FileBehavior",
      "endpoint.ip": "",
      "endpoint.uuid": "f999ac48f7421fa951545ce34f41a998",
      "file.hash": "",
      "file.name": "",
      "file.path": "C:\\Users\\liabe\\AppData\\Local\\Google\\Chrome\\User Data\\e9301ee9-92f7-46c0-b0e5-919fa164e8fc.tmp",
      "file.sig": "",
      "file.type": "",
      "process.calltrace": "",
      "process.cmdline": "",
      "process.guid": "{3c251a4e-62c2-5e8b-0000-00101918ab77}",
      "process.image": "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe",
      "process.pid": "",
      "process.user": "",
      "relation": "create",
      "timestamp": "2020-04-06T22:37:30",
      "value": "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe -create-> C:\\Users\\liabe\\AppData\\Local\\Google\\Chrome\\User Data\\e9301ee9-92f7-46c0-b0e5-919fa164e8fc.tmp"
    },
    {
      "attckids": "",
      "behaviortype": "FileBehavior",
      "endpoint.ip": "",
      "endpoint.uuid": "f999ac48f7421fa951545ce34f41a998",
      "file.hash": "",
      "file.name": "",
      "file.path": "C:\\Users\\liabe\\AppData\\Local\\Google\\Chrome\\User Data\\e9301ee9-92f7-46c0-b0e5-919fa164e8fc.tmp",
      "file.sig": "",
      "file.type": "",
      "process.calltrace": "",
      "process.cmdline": "",
      "process.guid": "{3c251a4e-62c2-5e8b-0000-00101918ab77}",
      "process.image": "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe",
      "process.pid": "",
      "process.user": "",
      "relation": "timestomp",
      "timestamp": "2020-04-06T22:37:30",
      "value": "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe -timestomp-> C:\\Users\\liabe\\AppData\\Local\\Google\\Chrome\\User Data\\e9301ee9-92f7-46c0-b0e5-919fa164e8fc.tmp"
    },
    {
      "attckids": "",
      "behaviortype": "FileBehavior",
      "endpoint.ip": "",
      "endpoint.uuid": "f999ac48f7421fa951545ce34f41a998",
      "file.hash": "",
      "file.name": "",
      "file.path": "C:\\Users\\liabe\\AppData\\Local\\Google\\Chrome\\User Data\\Local State~RF1846e926.TMP",
      "file.sig": "",
      "file.type": "",
      "process.calltrace": "",
      "process.cmdline": "",
      "process.guid": "{3c251a4e-62c2-5e8b-0000-00101918ab77}",
      "process.image": "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe",
      "process.pid": "",
      "process.user": "",
      "relation": "create",
      "timestamp": "2020-04-06T22:37:30",
      "value": "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe -create-> C:\\Users\\liabe\\AppData\\Local\\Google\\Chrome\\User Data\\Local State~RF1846e926.TMP"
    }
	]
}
```