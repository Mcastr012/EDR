// imports all nodejs product dependencies
const express = require('express');
const bodyParser = require('body-parser');
const request = require('request');
var path = require('path');

// integrates express and bodyparsing dependencies
const app = express();
app.use(bodyParser.urlencoded({ extended: false }));
app.use(bodyParser.json());

// sets the original server startup
// date as a global variable
var original_date = "";

// sets the default total cisa score
var cisa_total = 0;

// sets the total number of cisa levels
var cisa_levels = 0;

// sets the default server IP address
// (set to production cloud server)
var external_client_ip = "http://vm02.cluster.never.eu.org:5000";

// sets the default endpoint device
// (set to production user device)
var external_device_name = "DESKTOP-3LRRD6K";

// minified algorithm that calculates CISA cyberthreat score
// (see threat_score_algorithm.js for the expanded version)
function calculateThreatScore(T){var C=0,a=80,r=0,c=0;"T1003"==T&&(C=100,a=100,r=80,c=100),"T1004"==T&&(C=20,r=20,c=50),"T1028"==T&&(C=100,r=70,c=50),"T1035"==T&&(C=35,r=20,c=50),"T1042"==T&&(C=35,r=20,c=50),"T1053"==T&&(C=35,r=20,c=75),"T1059"==T&&(C=35,r=20,c=50),"T1060"==T&&(C=0,r=20,c=75),"T1064"==T&&(C=0,r=20,c=75),"T1070"==T&&(C=60,r=70,c=75),"T1037"==T&&(C=0,r=20,c=50),"T1076"==T&&(C=0,r=20,c=50),"T1085"==T&&(C=0,r=20,c=50),"T1086"==T&&(C=35,r=50,c=75),"T1088"==T&&(C=60,r=50,c=75),"T1101"==T&&(C=35,r=20,c=50),"T1103"==T&&(C=0,r=20,c=50),"T1117"==T&&(C=0,r=20,c=50),"T1122"==T&&(C=0,r=20,c=50),"T1128"==T&&(C=0,r=20,c=50),"T1131"==T&&(C=60,r=80,c=50),"T1138"==T&&(C=0,r=20,c=50),"T1140"==T&&(C=60,r=70,c=75),"T1170"==T&&(C=0,r=20,c=50),"T1180"==T&&(C=0,r=20,c=50),"T1182"==T&&(C=0,r=20,c=50),"T1183"==T&&(C=0,r=20,c=50),"T1191"==T&&(C=0,r=20,c=50),"T1196"==T&&(C=0,r=20,c=50),"T1197"==T&&(C=0,r=20,c=50),"T1202"==T&&(C=0,r=20,c=50),"T1216"==T&&(C=60,r=50,c=75),"T1218"==T&&(C=60,r=20,c=50),"T1220"==T&&(C=0,r=20,c=50),"T1223"==T&&(C=0,r=0,c=50),"C1000"==T&&(C=35,r=20,c=50),"C1001"==T&&(C=35,r=50,c=75),"C1002"==T&&(C=0,r=20,c=50),"C1003"==T&&(C=60,r=20,c=75),"C1004"==T&&(C=0,r=50,c=50),"C1005"==T&&(C=35,r=50,c=75),"C1006"==T&&(C=0,r=20,c=50);var e=(C*(6/34)+a*(5/34)+4/34*50+4/34*50+r*(2/34)+4/34*40+3/34*35+c*(6/34)-31)/69*100;console.log("threat detected with cisa level of " + Math.ceil(e));return Math.ceil(e)}

// gets the current utc date in yy-mm-dd format
function get_date()
{
	var current_date = new Date();
	var month = current_date.getUTCMonth() + 1;
	var day = current_date.getUTCDate();
	var year = current_date.getUTCFullYear();
	var today = year + "-" + month + "-" + day;
	return today;
}

// checks if current session is active
function check_session(session_id)
{
	var options = {
	  'method': 'GET',
	  'url': external_client_ip + '/api/user',
	  'headers': {
	    'Content-Type': 'application/json'
	  },
	  body: JSON.stringify({"sessionID": session_id})
	};
	request(options, function (error, response) { 
	  if (error) throw new Error(error);
	  var logs = JSON.parse(response.body);
	  console.log(logs);
	  return logs.success;
	});
}

// calculates threat level based on attack id from client
app.get('/behavior/level', function(request, response)
{
	var session_id = String(request.query.session_id);
	var session_status = check_session(session_id);
	if (session_status == false)
	{
		resp.header("X-Content-Type-Options", "nosniff");
	  	return resp.jsonp({"error": "session inactive"});
	}
	var attack_id = String(request.query.attack_id);
	response.header("X-Content-Type-Options", "nosniff");
	var threat_score = calculateThreatScore(attack_id);
	cisa_total += threat_score; cisa_levels += 1;
	return response.jsonp({"success": threat_score});
});

// calculates threat level based on attack id from client
app.get('/behavior/level/average', function(request, response)
{
	var session_id = String(request.query.session_id);
	var session_status = check_session(session_id);
	if (session_status == false)
	{
		resp.header("X-Content-Type-Options", "nosniff");
	  	return resp.jsonp({"error": "session inactive"});
	}
	response.header("X-Content-Type-Options", "nosniff");
	return response.jsonp({"success": Math.ceil(cisa_total / cisa_levels)});
});

// creates a new user based on registration input
app.get('/user/create', function(req, res)
{
	var name = String(req.query.name);
	var email = String(req.query.email);
	var password = String(req.query.password);
	var phone = String(req.query.phone);
	var options = {
	  'method': 'POST',
	  'url': external_client_ip + '/api/user',
	  'headers': {
	    'Content-Type': 'application/json'
	  },
	  body: JSON.stringify(
	  	{"name": name,
	  	"email": email,
	  	"phone": phone,
	  	"password": password})

	};
	request(options, function (error, response) { 
	  if (error) throw new Error(error);
	  res.header("X-Content-Type-Options", "nosniff");
	  return res.jsonp({"success": "success"});
	});

});

// gets current user session information
app.get('/user', function(req, res)
{
	var session_id = String(req.query.session_id);
	var session_status = check_session(session_id);
	if (session_status == false)
	{
		res.header("X-Content-Type-Options", "nosniff");
	  	return res.jsonp({"error": "session inactive"});
	}
	var options = {
	  'method': 'GET',
	  'url': external_client_ip + '/api/user',
	  'headers': {
	    'Content-Type': 'application/json'
	  },
	  body: JSON.stringify({"sessionID": session_id})
	};
	request(options, function (error, response) { 
	  if (error) throw new Error(error);
	  var logs = JSON.parse(response.body);
	  res.header("X-Content-Type-Options", "nosniff");
	  return res.jsonp({"success": logs.content.name});
	});
});

// logs the user out of an active session
app.get('/logout', function(req, resp)
{
	var session_id = String(req.query.session_id);
	var request = require('request');
	var options = {
	  'method': 'DELETE',
	  'url': external_client_ip + '/api/session',
	  'headers': {
	    'Content-Type': 'application/json'
	  },
	  body: JSON.stringify({"sessionID": session_id})

	};
	request(options, function (error, response) { 
	  if (error) throw new Error(error);
	  console.log(response.body);
	});

	resp.header("X-Content-Type-Options", "nosniff");
	return resp.jsonp({"success": "success"});
});

// logs the user into an active session
app.get('/login', function(req, resp)
{
	var username = String(req.query.username);
	var password = String(req.query.password);
	var options = {
	  'method': 'POST',
	  'url': external_client_ip + '/api/session',
	  'headers': {
	    'Content-Type': 'application/json'
	  },
	  body: JSON.stringify({"email":username,"password":password})

	};
	request(options, function (error, response) { 
	  console.log(response.body);
	  if (error) throw new Error(error);
	  var logs = JSON.parse(response.body);
	  if (logs.errMsg == null)
	  {
	  	resp.header("X-Content-Type-Options", "nosniff");
	  	return resp.jsonp({"success": logs.content.sessionID});
	  } else {
	  	resp.header("X-Content-Type-Options", "nosniff");
	  	return resp.jsonp({"failure": "failure"});
	  }
	});

});

// gets all registry behaviors from endpoint logs
app.get('/behavior/registry', function(req, resp)
{
	var session_id = String(req.query.session_id);
	var session_status = check_session(session_id);
	if (session_status == false)
	{
		resp.header("X-Content-Type-Options", "nosniff");
	  	return resp.jsonp({"error": "session inactive"});
	}
	var options = {
	  'method': 'GET',
	  'url': external_client_ip + '/api/behavior',
	  'headers': {
	    'Content-Type': ['application/json', 'application/json']
	  },
	  body: JSON.stringify({"behaviorType":"RegistryBehavior",
	  	"endpointID": external_device_name,"startDate": original_date,
	  	"endDate": get_date(),"pageSize":"10","pageIndex":"0"})

	};
	request(options, function (error, response) { 
	  if (error) throw new Error(error);
	  var logs = JSON.parse(response.body);
	  console.log(logs.content);
	  resp.header("X-Content-Type-Options", "nosniff");
	  return resp.jsonp({"success": JSON.stringify(logs.content)});
	});

});

// gets all network behaviors from endpoint logs
app.get('/behavior/network', function(req, resp)
{
	var session_id = String(req.query.session_id);
	var session_status = check_session(session_id);
	if (session_status == false)
	{
		resp.header("X-Content-Type-Options", "nosniff");
	  	return resp.jsonp({"error": "session inactive"});
	}
	var options = {
	  'method': 'GET',
	  'url': external_client_ip + '/api/behavior',
	  'headers': {
	    'Content-Type': ['application/json', 'application/json']
	  },
	  body: JSON.stringify({"behaviorType":"NetworkBehavior",
	  	"endpointID": external_device_name,"startDate": original_date,
	  	"endDate": get_date(),"pageSize":"10","pageIndex":"0"})

	};
	request(options, function (error, response) { 
	  if (error) throw new Error(error);
	  var logs = JSON.parse(response.body);
	  console.log(logs.content);
	  resp.header("X-Content-Type-Options", "nosniff");
	  return resp.jsonp({"success": JSON.stringify(logs.content)});
	});

});

// gets all file behaviors from endpoint logs
app.get('/behavior/file', function(req, resp)
{
	var session_id = String(req.query.session_id);
	var session_status = check_session(session_id);
	if (session_status == false)
	{
		resp.header("X-Content-Type-Options", "nosniff");
	  	return resp.jsonp({"error": "session inactive"});
	}
	var options = {
	  'method': 'GET',
	  'url': external_client_ip + '/api/behavior',
	  'headers': {
	    'Content-Type': ['application/json', 'application/json']
	  },
	  body: JSON.stringify({"behaviorType":"FileBehavior",
	  	"endpointID": external_device_name,
	  	"startDate": original_date,"endDate": get_date(),
	  	"pageSize":"10","pageIndex":"0"})
	};
	request(options, function (error, response) { 
	  if (error) throw new Error(error);
	  var logs = JSON.parse(response.body);
	  console.log(logs.content);
	  resp.header("X-Content-Type-Options", "nosniff");
	  return resp.jsonp({"success": JSON.stringify(logs.content)});
	});

});

// gets all process behaviors from endpoint logs
app.get('/behavior/process', function(req, resp)
{
	var session_id = String(req.query.session_id);
	var session_status = check_session(session_id);
	if (session_status == false)
	{
		resp.header("X-Content-Type-Options", "nosniff");
	  	return resp.jsonp({"error": "session inactive"});
	}
	var options = {
	  'method': 'GET',
	  'url': external_client_ip + '/api/behavior',
	  'headers': {
	    'Content-Type': ['application/json', 'application/json']
	  },
	  body: JSON.stringify({"behaviorType":"ProcessBehavior",
	  	"endpointID": external_device_name,"startDate": original_date,
	  	"endDate": get_date(),"pageSize":"10","pageIndex":"0"})
	};
	request(options, function (error, response) {
		if (error) throw new Error(error);
		var logs = JSON.parse(response.body);
		console.log(logs.content);
		resp.header("X-Content-Type-Options", "nosniff");
		return resp.jsonp({"success": JSON.stringify(logs.content)});
	});

});

// gets abnormal behavior from endpoint logs
app.get('/behavior/abnormal', function(req, resp)
{
	var session_id = String(req.query.session_id);
	var session_status = check_session(session_id);
	if (session_status == false)
	{
		resp.header("X-Content-Type-Options", "nosniff");
	  	return resp.jsonp({"error": "session inactive"});
	}
	var options = {
	  'method': 'GET',
	  'url': external_client_ip + '/api/abnormal',
	  'headers': {
	    'Content-Type': ['application/json', 'application/json']
	  },
	  body: JSON.stringify({"behaviorType":"ProcessBehavior",
	  	"endpointID": external_device_name,"startDate": original_date,
	  	"endDate": get_date(),"pageSize":"10","pageIndex":"0"})
	};
	request(options, function (error, response) { 
	  if (error) throw new Error(error);
	  var logs = JSON.parse(response.body);
	  console.log(logs.content);
	  resp.header("X-Content-Type-Options", "nosniff");
	  return resp.jsonp({"success": JSON.stringify(logs.content)});
	});
});

// routes "/" with the dashboard page
app.get('/', function(req, res) {
    res.sendFile(__dirname + '/index.html');
});

// routes "/done" with the login page
app.get('/done', function(req, res) {
    res.sendFile(__dirname + '/login.html');
});

// routes "/" with directory for resources
app.use('/', express.static(__dirname));

// starts server on port 3000
app.listen(3000, function(){
  console.log("Server up on port 3000...");
  // logs original date the server starts
  original_date = get_date();
});
