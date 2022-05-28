class Date:
    '''class to represent a date'''

    def __init__(self,month,day,year):
        '''Date(month,day,year) -> Date'''
        self.month = month
        self.day = day
        self.year = year

    def __str__(self):
        '''str(Date) -> str
        returns date in readable format'''
        # list of strings for the months
        months = ['','Jan','Feb','Mar','Apr','May','Jun','Jul',
                  'Aug','Sep','Oct','Nov','Dec']
        output = months[self.month] + ' ' # month
        output += str(self.day) + ', '  # day
        output += str(self.year)
        return output

    def go_to_next_day(self):
        '''Date.go_to_next_day()
        advances the date to the next day'''
        # list with the days in the month
        daysInMonth = [0,31,28,31,30,31,30,31,31,30,31,30,31]
        # check for leap year
        isLeapYear = self.year%4 == 0 and \
                     (self.year%100 != 0 or self.year%400 == 0)
        if isLeapYear :
            daysInMonth[2] = 29
        else :
            daysInMonth[2] = 28
        if daysInMonth[self.month] == self.day :
            self.month += 1
            if self.month > 12 :
                self.month = self.month % 12
                self.year += 1
            self.day = 1
        else :
            self.day += 1

# d = Date(1, 31, 2004)
# # should give Feb 1, 2004
# d = Date(2, 29, 2004)
# # should give Mar 1, 2004
# d = Date(2, 28, 2004)
# # should give Feb 29, 2004
d = Date(12, 31, 2004)
# should give Jan 1, 2005
d.go_to_next_day()
print(d)
