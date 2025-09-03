// downloads file in utf8-format from content
function download_file(file_name, content) {
  var element = document.createElement('a');
  element.style.display = "none";
  element.setAttribute('href', 'data:text/plain;charset=utf-8,' + encodeURIComponent(content));
  element.setAttribute('download', file_name);
  document.body.appendChild(element);
  element.click();
  document.body.removeChild(element);
}

// gathers and downloads endpoint logs to client
function download_endpoints()
{
  // gets alert endpoint logs
	$.ajax({
    url: "http://localhost:3000/behavior/abnormal",
    dataType: "jsonp",
    data: {"session_id": localStorage['sessionID']},
    success: function(result){
      var alert_logs = JSON.parse(result.success);
      var unique_endpoints = [];
      var unique_descriptions = [];
      var unique_date_time = [];
      var unique_status = [];
      
      // gathers information on unique endpoints from logs
      for (var x = 0; x < alert_logs.length; ++x)
      {
        var device_user = alert_logs[x]["current.user"].split("\\")[0];
        var time_stamp = alert_logs[x]["timestamp"];
        var device_name = alert_logs[x]["current.user"].split("\\")[1] + "@deloitte.com";
        if (unique_endpoints.includes(device_user) != true)
        {
          unique_endpoints.push(device_user);
          unique_descriptions.push(device_name);
          unique_date_time.push(time_stamp);
        }
      }
      // saves endpoints with chronological index as ID (data is subset of the ID)
      var export_object = {};
      for (var x = 0; x < unique_endpoints.length; ++x)
      {
        export_object[x.toString()] =
        {
          "email": unique_descriptions[x],
          "description": unique_endpoints[x],
          "current_datetime": unique_date_time[x],
          "status": "Online"
        };
      }
      // downloads machine learning endpoints based on final export object
      download_file("ml_endpoints.json", JSON.stringify(export_object));

      // closes log download tab
      window.close();
  }});
}

// launches download endpoints process
download_endpoints();
