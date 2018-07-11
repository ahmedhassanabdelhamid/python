# Define a daysBetweenDates procedure that would produce the
# correct output if there was a correct nextDay procedure.
#
# Note that this will NOT produce correct outputs yet, since
# our nextDay procedure assumes all months have 30 days
# (hence a year is 360 days, instead of 365).
# 

def nextDay(year, month, day):
    """Simple version: assume every month has 30 days"""
    if day < 30:
        return year, month, day + 1
    else:
        if month == 12:
            return year + 1, 1, 1
        else:
            return year, month + 1, 1
            
  def helper(y1,m1,d1,y2,m2,d2):
    i=0
    while y1<=y2:
      next=nextDay(y1,m1,d1)
      y1=next[0]
      m1=next[1]
      d1=next[2]
      i = i+1
      if m1==m2 and d1==d2:
        return i

                

        
def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    
    # YOUR CODE HERE!
    return helper(year1, month1, day1, year2, month2, day2)

def test():
    test_cases = [((2012,9,30,2012,10,30),30), 
                  ((2012,1,1,2013,1,1),360),
                  ((2012,9,1,2012,9,4),3)]
    
    for (args, answer) in test_cases:
        result = daysBetweenDates(*args)
        if result != answer:
            print "Test with data:", args, "failed"
        else:
            print "Test case passed!"

test()
    
