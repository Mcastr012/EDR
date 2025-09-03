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

// gathers and downloads alert logs to client
function download_alerts()
{
	$.ajax({
    url: "http://localhost:3000/behavior/abnormal",
    dataType: "jsonp",
    data: {"session_id": localStorage['sessionID']},
    success: function(result){
      var alert_logs = JSON.parse(result.success);
      download_file("ml_threats.json", JSON.stringify(alert_logs));
      window.close();
  }});
}

// launches download alerts process
download_alerts();
