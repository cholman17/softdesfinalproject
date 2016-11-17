''' 3:43 11/17 - Christina
this function is designed to pull courses (and make timetables)

'''

''' FOR TIMETABLES:
Create dictionaries (week); HTML text formatting,
display_week; update_week;
>>index.py: html_table; matrix; rows and columns

'''

#set a base url (pagesource of CourseListing)
baseurl= view-source:https://fusionmx.babson.edu/CourseListing/index.cfm?fuseaction=CourseListing.DisplayCourseListing&blnShowHeader=true&program=Undergraduate&semester=Spring+2017&sort_by=course_number&btnSubmit=Display+Courses

def browse():
    '''Open in browser (chrome)'''

    '''Click the search button for recent semester'''

    '''Look through the HTML codes to find
    TITLE, DAY, TIMES, PROFESSOR LASTNAME, COURSE NO.'''

    ''' Add to list of coursecodes '''

    '''IF NO MORE CODES: WRITE list into txt file'''

    ''' Organize text file into table-like format ''' #remove duplicates

    ''' Print length of list = # of classes '''

    ''' print "DONE browsing course list" '''
