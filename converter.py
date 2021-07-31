from datetime import date, datetime

def converter(cron_string):
    converted=""
    cron_minutes, cron_hour, cron_day, cron_month, cron_dof = cron_string.split(' ')
    print(cron_minutes, cron_hour, cron_day, cron_month, cron_dof)
    assert (cron_minutes == '*')  or (int(cron_minutes)>=0 and int(cron_minutes)<=59)
    assert (cron_hour =='*'    )  or (int(cron_hour)>=0    and int(cron_hour)<=23   )   
    assert (cron_day =='*'     )  or (int(cron_day)>=1     and int(cron_day)<=31    )    
    assert (cron_month =='*'   )  or (int(cron_month)>=1   and int(cron_month)<=12  )  
    assert (cron_dof =='*'     )  or (int(cron_dof)>=0     and int(cron_dof)<=6     )    
    
    #month
    if(cron_month == '*'):
        converted += ("Every month, ")
    elif(cron_month.isnumeric()):
        months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
        converted += ("In "+months[int(cron_month)]+", ")

    #dof
    dof_flag=False
    days = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Saturday"]
    if(cron_dof != '*' and cron_day == "*"):
        converted += ("every "+days[int(cron_dof)]+", ")
        dof_flag = True
    elif(cron_dof != '*'):
        converted += ("every "+days[int(cron_dof)]+" and ")
        dof_flag = True


    #day
    if(cron_day == '*' and not dof_flag):
        converted+=("every day, ")
    elif(cron_day.isnumeric()):
        if(  int(cron_day) > 1):
            converted+=("every "+cron_day+" days, ")
        else:
            converted+=("every "+cron_day+" day, ")

    #hour:minutes
    if(cron_hour.isnumeric() and cron_minutes.isnumeric()):
        converted += ("at {:02d}:{:02d}".format(int(cron_hour),int(cron_minutes)))
        return converted
    else:

        #hour
        if(cron_hour == '*'):
            converted += ("every hour, ")
        elif(cron_hour.isnumeric()):
            converted += ("at hour "+cron_day+", ")

        #minute
        if(cron_minutes == '*'):
            converted += ("every minute")
        elif(cron_minutes.isnumeric()):
            converted += ("at minute "+cron_minutes)
        return converted

if __name__ == "__main__":
    print(datetime.now())
    print(converter("4 * 5 7 *"))
    print(converter("4 1 2 3 4"))
    print(converter("* * * * 2"))