---
title: 'time tracking with google calendar'
date: '2014-07-27T18:53:01-07:00'
status: publish
permalink: /2014/07/time-tracking-google-calendar
author: sarah
excerpt: ''
type: post
id: 5160
category:
    - code
tag: []
post_format: []
---
I just created a very lightweight time tracking system where we can use a Google Calendar to track who does what when and then get a spreadsheet that shows all of the hours worked by individuals.

It goes with a spreadsheet where the first row has a header like this:  
Date Meeting Sarah Paul Glen

[![Screen Shot 2014-07-27 at 6.47.14 PM](../../../uploads/2014/07/Screen-Shot-2014-07-27-at-6.47.14-PM.png)](https://www.ultrasaurus.com/wp-content/uploads/2014/07/Screen-Shot-2014-07-27-at-6.47.14-PM.png)

The we just make events on Google calendar and invite whoever is working together at that time — could be a team meeting or one of us working on our own. Time will be tracked by first name of email address  
(paul@whatever.com and paul@yahoo.com would all get tracked in the “Paul” column). Currently the script doesn’t support two different people who share the same email name before ‘@’.

You just have to fill in your calendar id, which you can find if you choose Calendar Settings and scroll to the bottom of the first page (in Calendar Address section).

```

// add menu
function onOpen() {
  var ss = SpreadsheetApp.getActiveSpreadsheet();
  var menuEntries = [{name:"Calculate Hours", functionName: "calculateHours"}];
  ss.addMenu("Hours", menuEntries);
  // calcular al iniciar
  calculateHours();
}
 

function meetingSummary(cal_id){
  var hours = 0;
  var cal = CalendarApp.getCalendarById(cal_id);
  Logger.log(cal);
  Logger.log('The calendar is named "%s".', cal.getName());

  var this_year = new Date(2013,0,1);
  var now = new Date()
  var events = cal.getEvents(this_year, now);
  var results = []
  
  for ( i = 0 ; i < events.length ; i++){
    var event = events[i];
    title = event.getTitle();
    Logger.log(title);
    var start = event.getStartTime() ;
    var end =  event.getEndTime();
    start = new Date(start);
    end = new Date(end);
    hours = ( end - start ) / ( 1000 * 60 * 60 );
    guests = event.getGuestList();
    
    data = {meeting:title};
    for (g in guests) {
      var email = guests[g].getEmail();
      var name = email.split('@')[0];
      Logger.log(email, name);
      data[name] = hours;
    }
    data['date'] = start.toDateString();
    results.push(data)
  }
  
  Logger.log(results);
  return results;
}

function calculateHours(){
  Logger.clear();
  Logger.log("calculateHours");
  var cal_id = "put your cal id here";
  var ss = SpreadsheetApp.getActiveSpreadsheet();
  var s = ss.getSheets()[0];
  var headerValues = s.getRange("A1:F1").getValues();
  Logger.log(headerValues[0].length);
  var columns = {}
  var num_columns = headerValues[0].length;
  for (i=0; i < num_columns; i++) {
    columns[headerValues[0][i].toLowerCase()] = i+1;
  }
  Logger.log(columns);
  //{'glen':5, 'paul':4, 'description':6, 'meeting':2, 'sarah':3, 'date':1}
  var title_column = 2;
  
  // from second row
  var results = meetingSummary(cal_id);
  Logger.log("results.length="+results.length);

  for ( var row_number = 1; row_number < results.length+1 ; row_number ++){
    var result = results[row_number-1];
    Logger.log("row_number="+row_number);
    Logger.log(result);
    for (name in columns) {
      Logger.log("..."+name+"   "+result[name]);
      if (typeof result[name] == 'undefined') result[name] = "";
      s.getRange(row_number+1, columns[name]).setValue(result[name]);
    }
  }
}
```