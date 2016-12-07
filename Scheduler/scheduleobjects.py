import copy, random
from fetchcourses import *

''' TO DO: separate file for flask --> setup timetable visuals;
 ==> Import all modules into one main.py file
'''

"""
CSV to List of course objects == List of audits needed:
--> list of lists: [[FME1000-01, 02....], [CS-01, 02], [C3]...]
*Problem Solver: loop thru A01, B01, C01 until no time conflicts
    ^No priority?
    ^List of candidates/possibiliteis
    ^Return first one that runs True
"""

class Scheduler(object):
	def __init__(self,codes,semester, options, timeperiod):

		pass

	def startschedule(self):


		pass

	def findtimetable(self, index):

		pass

	def update(self, timetable):

		pass

	def findcourseinfo(self):

		pass

	def rateAll(self, prefs):

		pass

	def loopSection(self, recursion, opp, prefs):

		pass

	def loopLab(self, recursion, opp, sections, prefs):

		pass

	def noPref(self, x=None):
		return random.rantint(0,99)

	def morningClass(self, timetable):

		pass

	def eveningClass(self, timetable):

		pass

	def filterTimeperiod(self):

		pass

	def filterDay(self):

		pass

	def applyFilter(self,filtering, filterVar):


		pass

	def timeFilter(self,classtime,var):

		pass

	def dayFilter(self, classtime, restday):
		pass

	def Nothing(self):
		#shows error message when no possible schedules

class Timetable(object):

	def __init__(self, registered, preferences):
		self.classes = registered
		self.score = preferences(self)

	def calcScore(self):
		return self.score
	def registered(self):
		return self.classes
	def makeString(self):
		string = ""
		for c in self.classes:
			#string += #shows details to User in one long string
		return string

class onlineSchedule(object):
	def __init__(self, totalCourses):
		self.days = {}
		self.days['M'] = []
		self.days['T'] = []
		self.days['W'] = []
		self.days['R'] = []
		self.days['F'] = []
		self.classes = []

	def addCourse(self, classtime):
		#interval time?
		#interval =

		#make sure no conflicting timeslots
		for day in classtime.findDays():
			if len()[i in intervals if i in self.days[day]]) > 0:
				return False

		#add intervals to respective days, return True

	def toRegister(self):
		return copy.deepcopy(self.classes)
