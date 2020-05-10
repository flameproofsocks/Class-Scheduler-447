DEPART = 0
COURSE_NUM = 1
COURSE_NAME = 2
SECTION = 4
INSTRUCTORF = 5
TIME = 6
CAP = 7
INSTRUCTORL = 6
TIME2 = 7
CAP2 = 8

def insertRoomBuild(arr):
    command = "INSERT INTO rooms Values("
    for i in arr:
        command += str(i)
        
        # For all elements except the last element
        if i != arr[len(arr) - 1]:
            command += ", " # Add the comma separator for the addition of values
        
    #for j in range(len(arr)):
        #command += str(arr[j])
    command += ") ON CONFLICT DO NOTHING"

    # Output will match: INSERT INTO table VALUES (Variable, Length, Values) ON CONFLICT DO NOTHING
    return command
    #INSERT INTO rooms VALUES(3, 'Bio', 202, 30, 'Classroom') ON CONFLICT DO NOTHING;

def insertCommandBuild(table, arr):
    table = str(table)
    command = "INSERT INTO " + table + " Values("
    for i in arr:
        command += str(i)
        
        # For all elements except the last element
        if i != arr[len(arr) - 1]:
            command += ", " # Add the comma separator for the addition of values
        
    #for j in range(len(arr)):
        #command += str(arr[j])
    command += ") ON CONFLICT DO NOTHING"
    
    '''if table == "rooms":
    elif table == "Class":
    elif table == "prof":'''
    
    # Output will match: INSERT INTO table VALUES (Variable, Length, Values) ON CONFLICT DO NOTHING
    return command

# Disassemble a line into its comma separated values
def scheduleRead(line, delimiter):
    temp = ""
    store = []
    
    for i in line:
        if i != delimiter:
            temp += i
        else:
            store.append(temp)
            temp = ""
    store.append(temp.strip()) # This is to account for the last string that does not have a comma after it
    return store

def sPrint(x):
    
    for i in x:
        s = ""
        for j in i:
            s += j + " "
        print(s)

# Extracts all columns of data in the CSV file data for schedule
def scheduleExtractor(sch):

    #DEPART = 0
    #COURSE_NUM = 1
    #COURSE_NAME = 2
    #SECTION = 4
    #INSTRUCTOR = 5
    #TIME = 6
    #CAP = 7

    departments = []
    course_nums = []
    course_names = []
    sections = []
    instructors = []
    times = []
    capacities = []

    for i in range(len(sch)):
        departments.append(sch[i][DEPART])
        course_nums.append(sch[i][COURSE_NUM])
        course_names.append(sch[i][COURSE_NAME])
        sections.append(sch[i][SECTION])
        instructors.append(sch[i][INSTRUCTORF])
        times.append(sch[i][TIME])
        capacities.append(sch[i][CAP])

    departments.pop(0)
    course_nums.pop(0)
    course_names.pop(0)
    sections.pop(0)
    instructors.pop(0)
    times.pop(0)
    capacities.pop(0)
    
    return departments, course_nums, course_names, sections, instructors, times, capacities
        
def main():

    #array = ["a","b","c"]
    #print(insertRoomBuild(array))
    #print(insertCommandBuild("professor", array))

    f = open("ClassData.csv", "r")
    buff = f.readlines()
    schedule = []
    for line in buff:
        schedule.append(scheduleRead(line, ','))
    
    #sPrint(schedule)
    #print(schedule[1])

    departments, course_nums, course_names, sections, instructors, times, capacities = scheduleExtractor(schedule)
    #print(departments)
    #print(course_nums)
    #print(course_names)
    #print(sections)
    #print(instructors)
    #print(times)
    #print(capacities)

    # All columns of data are now in their respective data arrays
    # Now, the next step will be using these arrays and their information to load the right tables with their respective elements and data



    
main()
