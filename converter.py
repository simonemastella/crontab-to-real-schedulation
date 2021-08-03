#from datetime import date, datetime
import traceback
import cron_utils

def converter(cron_string):
    try:
        converted=""
        if (cron_string.count(' ')!=4):
            raise Exception('cron string','wrong format')
        cron_minutes, cron_hour, cron_day, cron_month, cron_dow = cron_string.split(' ')
        print(cron_minutes, cron_hour, cron_day, cron_month, cron_dow)
        
        #month
        converted+=cron_utils.month_converter(cron_month)

        #dow
        converted+=cron_utils.dow_converter(cron_dow= cron_dow, cron_day= cron_day)

        #day
        converted+=cron_utils.day_converter(cron_dow= cron_dow, cron_day= cron_day)

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
    except:
        traceback.print_exc()

if __name__ == "__main__":
    #print(datetime.now())
    # print(converter("4 * 5 7 *"))
    # print(converter("4 1 2 3 4"))
    print(converter("4 1 5-20/3,*/2 3 4"))
    # print(converter("4 1 2 3 4"))
    # print(converter("* * * */2 2"))
    # print(converter("* * * 1,4,2,6 2"))

