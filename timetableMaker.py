''' Generate timetable '''

import sys
import os
import json
import urllib.request
import csv #??
from datetime import datetime, time

#use base URL and term_id

#start/endTime of interval
schedule_startTime_str = " " #datetime looks like "2015-06-01T00:00:00+02:00"
schedule_endTime_str = " "

input_file = " "
course_file = " " #scan details by spaces/cols?

output_file = " "

#I think I wrote these backwards (Sunday is Day 6; Monday is Day 0)
weekdays = {1: "Sunday", 2: "Monday", 3: "Tuesday", 4: "Wednesday", 5:"Thursday", 6:"Friday", 7:"Saturday"}
weekdaysShort = {1: "Sun",2:"Mon",3:"Tues",4:"Wed",5:"Thurs",6:"Fri",7:"Sat"}


#startTime of blocks
table_blocks = [{'time':time(hour=8,minute=0), 'block':1},
				{'time': time(hour=9,minute=0), 'block':2},
				{'time':time(hour=10,minute=0),'block':3},
				{'time':time(hour=11,minute=0),'block':4},
				{'time':time(hour=12,minute=0),'block':5},
				{'time':time(hour=13,minute=0),'block':6},
				{'time':time(hour=14,minute=0),'block':7},
				{'time':time(hour=15,minute=0),'block':8},
				{'time':time(hour=16,minute=0),'block':9},
				{'time':time(hour=17,minute=0),'block':10},
				{'time':time(hour=18,minute=0),'block':11}]

fontFamily = "Arial"
fontsizeName = "12pt"
fontSize = "10pt"
fontsizeHeader = "20pt"

#blockBorder = "2pt solid #000000"
#blockBorderCourse = " "

class Course: #creates course object and info
	def __init__(self,id,lecID,name,profs):
		self.id = int(id)
		self.lecID = int(lecID)
		self.name = name
		self.nameShort = ""
		self.categ = ""
		#self.profs =
		self.courses = []
		self.events = [] #rename

class Classes:
	def __init__(self,start,end,room):
		self.start = start
		self.end = end
		self.room = room

	def within_period(self):
		return self.start > schedule_startTime and self.start < schedule_endTime

	def get_block(self):
		count = len(table_blocks)
		for i in range(0,count):
			if self.start.time() >= table_blocks[i]['time'] and (i==count-1 or self.start.time() < table_blocks[i+1]['time']):
				return table_blocks[i]['block']

# def get_courses(classnumbers): #download data of all courses into subdir

#def get_course(course_lecID): #download data in json format in one course

def build_table():
	#repeat for all courses
	for course_lecID, course in courses.items():
		find_classes = False
		#repeat for all events
		for classes in course.classes:
			if classes.within_period():
				find_classes = True

				#get info about position in table
				weekday = classes.start.isoweekday() #if using datetime object
				block.classes.get_block()

				#append data to list of dates
				if course_lecID not in timetable[weekday][block]:
					timetable[weekday][block][course_lecID] = []
				timetable[weekday][block][course_lecID].append(classes)

				#append this to list of events
				if [weekday,block] not in course.events:
					course.events.append([weekday,block])
			if not find_class:
				courses_missed[course.lecID]=course

courses = {} #holds all courses as objects with courses.lecID
courses_missed = {} #courses for which no event/time was found

schedule_startTime = parse_datetime(schedule_startTime_str)
schedule_endTime = parse_datetime(schedule_endTime_str)

#hold all the days; all blocks and then all courses
timetable = {}
for day in range(1,6):
	blocks = {}
	for block in range(1,9):
		blocks[block] = {}
	timetable[day] = blocks

#assemble
build_table()
#spreadsheet columns and rows start at 1 but leave 1st empty
startCol = 2
startRow = 3
#per entry
courseWidth = 2
courseHeight = 3

#get max num of courses into each block; minimum = 1
blockHeight = {}
for block in range(1,9):
	blockHeight[block] = 1

for block in range(1,9):
	for weekday in range(1,6):
		newHeight = len(timetable[weekday][block])
		if newHeight > blockHeight[block]:
			blockHeight[block] = newHeight

#print first column
currentRow = startRow+1
for block in range(1,9):
	printCell(sheetTable, currentRow, startCol, str(block))
	currentRow += blockHeight[block]*courseHeight

#print timetable
printCell(sheetTable, 1, startCol +1, "Schedule", fontsizeHeader)
printCell(sheetTable,1, startCol + 4, "{0} until {1}".format(schedule_startTime.strftime("%d.%m."), schedule_endTime.strftime("%d.%m.")), fontsizeHeader)

for weekday in range(1,6):
	printTable("{0}".format(weekdays[weekday]))
	weekdayCol = startCol + 1 + (weekday-1)*courseWidth
	block_startRow = startRow + 1
	printCell(sheetTable, startRow, weekdayCol, weekdays[weekday], fontsizeName)
	for block in range(1,9):
		printTable(

#set borders
