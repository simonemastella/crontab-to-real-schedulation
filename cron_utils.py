def month_converter(cron_month):
    result=""
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    if(cron_month == '*'):
        result += ("every month, ") #OUTPUT
    elif (cron_month.isnumeric()):
        result += ("in "+months[int(cron_month)]+" ") #OUTPUT
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
            result += ("from "+months[int(start)]+" to "+months[int(end)]+" ") #OUTPUT
        else:
            end,every=end.split("/")
            assert start.isnumeric() and end.isnumeric()
            result += ("from "+months[int(start)]+" to "+months[int(end)]+"every "+every+" months, ") #OUTPUT
    else: 
        raise Exception('month','error while parsing')
    return result #OUTPUT

def dow_converter(cron_dow, cron_day):
    result=""
    days = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Saturday"]
    if(cron_day == "*"):
        if(cron_dow.isnumeric()):
            result += ("every "+days[int(cron_dow)]+" ") #OUTPUT
        elif(',' in cron_dow):
            for current_day in sorted(cron_dow.split(',')):
                result += (dow_converter(current_day)+" and ") #OUTPUT
            result=result[:-5]+", " #OUTPUT
        elif(cron_dow[:2] == "*/"):
            cron_dow=cron_dow[2:]
            if cron_dow.isnumeric() and int(cron_dow)>0:
                if (int(cron_dow)>1):

                    result+= ("every "+cron_dow+" days, ") #OUTPUT
                else:
                    result+= ("every day, ") #OUTPUT
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
            raise Exception('day','error while parsing')
    return result #OUTPUT
