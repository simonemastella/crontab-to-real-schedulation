def month_converter(cron_month):
    result=""
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    if(cron_month == '*'):
        result += ("every month, ")
    elif (cron_month.isnumeric()):
        result += ("in "+months[int(cron_month)]+" ")
    elif(',' in cron_month):
        for current_month in sorted(cron_month.split(',')):
            result += (month_converter(current_month)+" and ")
        result=result[:-5]+", "
    elif(cron_month[:2] == "*/"):
        cron_month=cron_month[2:]
        if cron_month.isnumeric() and int(cron_month)>0:
            if (int(cron_month)>1):

                result+= ("every "+cron_month+" months, ")
            else:
                result+= ("every month, ")
        else :
            raise Exception('*/ month','error while parsing')
    elif("-" in cron_month):
        start,end=cron_month.split("-")
        if("/" not in end):
            assert start.isnumeric() and end.isnumeric()
            result += ("from "+months[int(start)]+" to "+months[int(end)]+" ")
        else:
            end,every=end.split("/")
            assert start.isnumeric() and end.isnumeric()
            result += ("from "+months[int(start)]+" to "+months[int(end)]+"every "+every+" months, ")
    else: 
        raise Exception('month','error while parsing')
    return result
