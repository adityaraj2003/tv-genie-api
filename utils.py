from datetime import timedelta
from datetime import datetime

def convert24(str1):
     
    # Checking if last two elements of time
    # is AM and first two elements are 12
    if str1[-2:] == "AM" and str1[:2] == "12":
        return "00" + str1[2:-2]
         
    # remove the AM    
    elif str1[-2:] == "AM":
        return str1[:-2]
     
    # Checking if last two elements of time
    # is PM and first two elements are 12
    elif str1[-2:] == "PM" and str1[:2] == "12":
        return str1[:-2]
         
    else:
         
        # add 12 to hours and remove PM
        return str(int(str1[:2]) + 12) + str1[2:8].replace("PM" , "").replace("AM" , "")

def getTimeDifference(time1 , time2):
  t1 = datetime.strptime(time1, "%H:%M:%S")
  t2 = datetime.strptime(time2, "%H:%M:%S")
  delta = t2 - t1
  return (str(delta.total_seconds() / 60)).split(".")[0]


def getTplayTime(time1 , time2 , data):
    # begin = int(data) / 1000
    # naive = str(time.strftime('%Y%m%d', time.localtime(begin)))
    year , month , date = data.split("/")[0].split("-")
    hh, mm, ss = map(int, time1.split(':'))
    hh2 , mm2 , ss2 = map(int, time2.split(':'))
    t1 = timedelta(hours=hh, minutes=mm , seconds=ss)
    t2 = timedelta(hours=hh2, minutes=mm2 , seconds=ss2)
    f = str(t1 - t2)
    
    # if len(f.split(":")[0]) == 1:
    #         g = str(year) + str(month) + str(int(date) - 1) + "T" + "0" + str(f.replace(":" , ""))
    # else:
    #         g = str(year) + str(month) + str(int(date) - 1) + "T" + str(f.replace(":" , ""))
    
    if "-1" in f:
        if len(f.split(":")[0]) == 1:
            date_sub = int(date) - 1
            if int(date_sub) < 10:
                
                g = str(year) + str(month) + "0" + str(date_sub) + "T" + "0" + str(f.replace(":" , ""))
            else:
                g = str(year) + str(month) + str(date_sub) + "T" + "0" + str(f.replace(":" , ""))
        else:
            date_sub = int(date) - 1
            if int(date_sub) < 10:

                g = str(year) + str(month) + "0" + str(date_sub) + "T" + str(f.replace(":" , ""))
            else:
                g = str(year) + str(month) + str(date_sub) + "T" + str(f.replace(":" , ""))
            
        return g.replace("-1 day, " , "")
        
    else:
        if len(f.split(":")[0]) == 1:
            g = str(year) + str(month) + str(date) + "T" + "0" + str(f.replace(":" , ""))
        else:
            g = str(year) + str(month) + str(date) + "T" + str(f.replace(":" , ""))
        return g
