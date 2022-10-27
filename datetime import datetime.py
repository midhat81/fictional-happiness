import datetime
now = datetime.datetime.now()
print ("Current date and time : ")
date = now.strftime("%Y-%m-%d %H:%M:%S")
date = str(date)
date = date.replace(" ","_")
date = date.replace("-","_")
date = date.replace(":","_")
print(date)