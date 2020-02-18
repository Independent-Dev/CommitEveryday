function getTime(){
    var a_p = "";
    var d = new Date();
    var curr_hour = d.getHours();
    (curr_hour<12) ? a_p = "AM": a_p = "PM", curr_hour -= 12;
    var curr_min = d.getMinutes();
    var curr_sec = d.getSeconds();
    if(curr_min<10) curr_min = "0"+ curr_min;
    if(curr_sec<10) curr_sec = "0"+ curr_sec;
    $("#updatedTime").text(curr_hour+":"+curr_min+":"+curr_sec+" "+a_p);
}

setInterval(getTime, 1000);
