def month_converter(cron_month):
    result=""
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    if(cron_month == '*'):
        result += ("every month, ") #OUTPUT
    elif (cron_month.isnumeric()):
        if (int(cron_month)>=1 or int(cron_month)<=12 ):
            result += ("in "+months[int(cron_month)-1]+" ") #OUTPUT
    elif(',' in cron_month):
        for current_month in sorted(cron_month.split(',')):
            result += (month_converter(current_month)+" and ") #OUTPUT
        result=result[:-5]+", " #OUTPUT
    elif(cron_month[:2] == "*/"):
        cron_month=cron_month[2:]
        if cron_month.isnumeric() and int(cron_month)>0:
            if (int(cron_month)>1):
                result+= ("every "+cron_month+" months, ") #OUTPUT
            else:
                result+= ("every month, ") #OUTPUT
        else :
            raise Exception('*/ month','error while parsing')
    elif("-" in cron_month):
        start,end=cron_month.split("-")
        if("/" not in end):
            assert start.isnumeric() and end.isnumeric()
            result += ("from "+months[int(start)-1]+" to "+months[int(end)-1]+" ") #OUTPUT
        else:
            end,every=end.split("/")
            assert start.isnumeric() and end.isnumeric()
            result += ("from "+months[int(start)-1]+" to "+months[int(end)-1]+"every "+every+" months, ") #OUTPUT
    else: 
        raise Exception('month','error while parsing')
    return result #OUTPUT

def dow_converter(cron_dow, cron_day):
    result=""
    days = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Saturday"]
    if(cron_day == "*"):
        if(cron_dow.isnumeric()):
            if (int(cron_dow)>=0 or int(cron_dow)<=7 ):
                result += ("every "+days[int(cron_dow)]+" ") #OUTPUT
        elif(cron_dow == "*"):
            pass
        elif(',' in cron_dow):
            for current_day in sorted(cron_dow.split(',')):
                result += (dow_converter(current_day, cron_day)+" and ") #OUTPUT
            result=result[:-5]+", " #OUTPUT
        elif(cron_dow[:2] == "*/"):
            cron_dow=cron_dow[2:]
            if cron_dow.isnumeric() and int(cron_dow)>0:
                if (int(cron_dow)>1):
                    result+= ("every "+cron_dow+" days, ") #OUTPUT
            else :
                raise Exception('*/ day','error while parsing')
        elif("-" in cron_dow):
            start,end=cron_dow.split("-")
            if("/" not in end):
                assert start.isnumeric() and end.isnumeric()
                result += ("from "+days[int(start)]+" to "+days[int(end)]+" ") #OUTPUT
            else:
                end,every=end.split("/")
                assert start.isnumeric() and end.isnumeric()
                result += ("from "+days[int(start)]+" to "+days[int(end)]+"every "+every+" days, ") #OUTPUT
        else: 
            raise Exception('dow','error while parsing')
    return result #OUTPUT

def day_converter(cron_day, cron_dow):
    result=""
    if(cron_day == '*' and cron_dow == "*"):
        result+=("every day, ")
    elif(cron_day == '*' and cron_dow != "*"):
        pass
    elif(cron_day.isnumeric()):
        if (int(cron_day)>=0 or int(cron_day)<=7 ):
            result += ("on day "+cron_day) #OUTPUT
    elif(',' in cron_day):
        for current_day in sorted(cron_day.split(',')):
            result += (day_converter(current_day, cron_dow)+" and, ") #OUTPUT
        result=result[:-6]+", " #OUTPUT
    elif(cron_day[:2] == "*/"):
        cron_day=cron_day[2:]
        if cron_day.isnumeric() and int(cron_day)>0:
            if (int(cron_day)>1):
                result+= ("every "+cron_day+" days") #OUTPUT
            else:
                result+= ("every day") #OUTPUT
        else :
            raise Exception('*/ day','error while parsing')
    elif("-" in cron_day):
        start,end=cron_day.split("-")
        if("/" not in end):
            assert start.isnumeric() and end.isnumeric()
            result += ("from day "+(start)+" to day "+end) #OUTPUT
        else:
            end,every=end.split("/")
            assert start.isnumeric() and end.isnumeric()
            result += ("from day "+start+" to day "+end+" every "+every+" days") #OUTPUT
    else: 
        raise Exception('day','error while parsing')
    return result #OUTPUT


def hour_minute_converter(cron_hour, cron_minute):
    result=""
    if(cron_hour.isnumeric() and cron_minute.isnumeric()):
            result += ("at {:02d}:{:02d}".format(int(cron_hour),int(cron_minute)))
    else:
        #hour
        result+= hour_converter(cron_hour=cron_hour)
        #minute
        result+= minute_converter(cron_minute=cron_minute)
    return result #OUTPUT

def hour_converter(cron_hour):
    result=""
    if(cron_hour == '*'):
        result+=("every hour, ")
    elif(cron_hour == '*'):
        pass
    elif(cron_hour.isnumeric()):
        if (int(cron_hour)>=0 or int(cron_hour)<=23 ):
            result += ("at {:02d}".format(int(cron_hour))) #OUTPUT
    elif(',' in cron_hour):
        for current_hour in sorted(cron_hour.split(',')):
            result += (hour_converter(current_hour)+" and ") #OUTPUT
        result=result[:-5]+", " #OUTPUT
    elif(cron_hour[:2] == "*/"):
        cron_hour=cron_hour[2:]
        if cron_hour.isnumeric() and int(cron_hour)>0:
            if (int(cron_hour)>1):
                result+= ("every {} hours".format(int(cron_hour)))#OUTPUT
            else:
                result+= ("every hour") #OUTPUT
        else :
            raise Exception('*/ hour','error while parsing')
    elif("-" in cron_hour):
        start,end=cron_hour.split("-")
        if("/" not in end):
            assert start.isnumeric() and end.isnumeric()
            result += ("from hour {:02d} to hour {:02d}".format(int(start),int(end))) #OUTPUT
        else:
            end,every=end.split("/")
            assert start.isnumeric() and end.isnumeric()
            result += ("from hour {:02d} to hour {:02d} every {:02d} hours").format(int(start),int(end), int(every)) #OUTPUT
    else: 
        raise Exception('hour','error while parsing')
    return result #OUTPUT

def minute_converter(cron_minute):
    result=""
    if(cron_minute == '*'):
        result+=("every minute, ")
    elif(cron_minute == '*'):
        pass
    elif(cron_minute.isnumeric()):
        if (int(cron_minute)>=0 or int(cron_minute)<=23 ):
            result += ("at minute {:02d}".format(int(cron_minute))) #OUTPUT
    elif(',' in cron_minute):
        for current_hour in sorted(cron_minute.split(',')):
            result += (hour_converter(current_hour)+" and ") #OUTPUT
        result=result[:-5]+", " #OUTPUT
    elif(cron_minute[:2] == "*/"):
        cron_minute=cron_minute[2:]
        if cron_minute.isnumeric() and int(cron_minute)>0:
            if (int(cron_minute)>1):
                result+= ("every {} minutes".format(int(cron_minute)))#OUTPUT
            else:
                result+= ("every minute") #OUTPUT
        else :
            raise Exception('*/ minute','error while parsing')
    elif("-" in cron_minute):
        start,end=cron_minute.split("-")
        if("/" not in end):
            assert start.isnumeric() and end.isnumeric()
            result += ("from minute {:02d} to minute {:02d}".format(int(start),int(end))) #OUTPUT
        else:
            end,every=end.split("/")
            assert start.isnumeric() and end.isnumeric()
            result += ("from minute {:02d} to minute {:02d} every {:02d} minutes").format(int(start),int(end), int(every)) #OUTPUT
    else: 
        raise Exception('minute','error while parsing')
    return result #OUTPUT