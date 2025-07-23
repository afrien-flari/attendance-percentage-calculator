def cal_percentage(num_workdays, num_period, num_misseddays, num_periodsmissed):
    total_periods = num_workdays * num_period
    missedperiods = (num_misseddays * num_period) + num_periodsmissed
    attended_periods = total_periods - missedperiods
    #calculate attendance percentage
    attended_percentage = round((attended_periods / total_periods) * 100, 2)
    print(f'your current attendance percentage: {attended_percentage}')
    #no. of leaves that can be taken without lowering below 75%
    if attended_percentage >= 75.00:
        safeperiods_leave = (attended_periods-0.75*total_periods)/0.75
        safeday_leave = round(safeperiods_leave/num_period, 2)
        print(f"you can take {safeday_leave} days leave without lowering below 75%")
    #no. of days to attend to rise above 75%
    else:
        needed_periods = (0.75*total_periods-attended_periods)/0.25
        needed_days = round(needed_periods/num_period, 2)
        print(f"you need to attend {needed_days} more days to rise your attendance above 75%")
    return attended_percentage
    

def main():
    num_workdays = int(input("enter the number of working days: "))
    num_period = int(input("enter the number of periods per day: "))
    num_misseddays = int(input("enter the number of missed full days: "))
    num_periodsmissed = int(input("enter the number of periods missed(don't include the full days): "))
    cal_percentage(num_workdays, num_period, num_misseddays, num_periodsmissed)

main()
    




