// logs user out of backend server based on session_id
function logout()
{
	var session_id = localStorage['sessionID'];
	console.log(session_id);
	localStorage['sessionID'] = " ";
	$.ajax({
	    url: "http://localhost:3000/logout",
	    dataType: "jsonp",
	    data: {"session_id": session_id},
	    async: false,
	    success: function(result){
	    	console.log("logout successful.");
	    	location.replace("./done");
	  }});
}