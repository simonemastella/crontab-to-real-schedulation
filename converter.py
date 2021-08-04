#from datetime import date, datetime
import traceback
import cron_utils

def converter(cron_string):
    try:
        converted=""
        if (cron_string.count(' ')!=4):
            raise Exception('cron string','wrong format')
        cron_minute, cron_hour, cron_day, cron_month, cron_dow = cron_string.split(' ')
        print(cron_minute, cron_hour, cron_day, cron_month, cron_dow)
        
        #month
        converted+=cron_utils.month_converter(cron_month)

        #dow
        converted+=cron_utils.dow_converter(cron_dow= cron_dow, cron_day= cron_day)

        #day
        converted+=cron_utils.day_converter(cron_dow= cron_dow, cron_day= cron_day)

        #hour:minutes
        return converted+cron_utils.hour_minute_converter(cron_hour=cron_hour, cron_minute=cron_minute)
    except:
        traceback.print_exc()

if __name__ == "__main__":
    #print(datetime.now())
    # print(converter("4 * 5 7 *"))
    # print(converter("4 1 2 3 4"))
    print(converter("4 1 5-20/3,*/2 3 4"))
    print(converter("4 2,8,*/5 * * *"))
    # print(converter("4 1 2 3 4"))
    # print(converter("* * * */2 2"))
    # print(converter("* * * 1,4,2,6 2"))

