# Python - Date and Time
import time;    # This is required to include time module

ticks = time.time()
print("Number of ticks since 12:00am, January 1, 1970:", ticks)

localtime = time.localtime(time.time())
print("Local time:", localtime)

# Gatting calendar for a month
import calendar

cdr = calendar.month(2013, 9)
print(cdr)

# The clock() method example
# import time

def proc():
    time.sleep(2.5) # suspend execution for 2.5 seconds

# Measure process time
t0 = time.clock()
proc()
print(time.clock() - t0, "seconds process time")

# Measure wall time
t0 = time.time()
proc()
print(time.time() - t0, "seconds wall time")

# Method sleep() test
print("Start:", time.ctime())
time.sleep(5)
print("  End:", time.ctime())

# ========== time.strftime(fmt[,tupletime]) ===========
# The method strftime() converts a tuple or struct_time representing a time as
# returned by gmtime() or localtime() to a string as specified by the format argument.
# If t is not provided, the current time as returned by localtime() is used. format must
# be a string. An exception ValueError is raised if any field in t is outside of the allowed
# range.
#
# Syntax
# Following is the syntax for strftime() method:
#       time.strftime(format[, t])
#
# Parameters
#        t -- This is the time in number of seconds to be formatted.
#        format -- This is the directive which would be used to format given time. The
#                   following directives can be embedded in the format string:
#
# Directive
#    %a - abbreviated weekday name
#    %A - full weekday name
#    %b - abbreviated month name
#    %B - full month name
#    %c - preferred date and time representation
#    %C - century number (the year divided by 100, range 00 to 99)
#    %d - day of the month (01 to 31)
#    %D - same as %m/%d/%y
#    %e - day of the month (1 to 31)
#    %g - like %G, but without the century
#    %G - 4-digit year corresponding to the ISO week number (see %V).
#    %h - same as %b
#    %H - hour, using a 24-hour clock (00 to 23)
#    %I - hour, using a 12-hour clock (01 to 12)
#    %j - day of the year (001 to 366)
#    %m - month (01 to 12)
#    %M - minute
#    %n - newline character
#    %p - either am or pm according to the given time value
#    %r - time in a.m. and p.m. notation
#    %R - time in 24 hour notation
#    %S - second
#    %t - tab character
#    %T - current time, equal to %H:%M:%S
#    %u - weekday as a number (1 to 7), Monday = 1.
#          Warning: In Sun Solaris: Sunday = 1.
#    %U - week number of the current year, starting with the first Sunday as the
#          first day of the first week
#    %V - The ISO 8601 week number of the current year (01 to 53), where week
#          1 is the first week that has at least 4 days in the current year, and with Monday
#          as the first day of the week
#    %W - week number of the current year, starting with the first Monday as the
#          first day of the first week
#    %w - day of the week as a decimal, Sunday = 0.
#    %x - preferred date representation without the time
#    %X - preferred time representation without the date
#    %y - year without a century (range 00 to 99)
#    %Y - year including the century
#    %Z or %z - time zone or name or abbreviation
#    %% - a literal % character
#
#   Return Value
#   This method does not return any value.

t = (2009, 2, 17, 17, 3, 38, 1, 48, 0)
t = time.mktime(t)
print(time.strftime("%b %d %Y %H:%M:%S", time.gmtime(t)))

# ======= time.strptime(str, fmt='%a %b %d %H:%M:%S %Y') =======
# The method strptime() parses a string representing a time according to a format.
# The return value is a struct_time as returned by gmtime() or localtime().
# The format parameter uses the same directives as those used by strftime(); it
# defaults to "%a %b %d %H:%M:%S %Y" which matches the formatting returned by
# ctime().
# If string cannot be parsed according to format, or if it has excess data after parsing,
# ValueError is raised.
#
# Syntax
# Following is the syntax for strptime() method:
#       time.strptime(string[, format])
# Parameters
#        string -- This is the time in string format which would be parsed based on the
#                   given format.
#        format -- This is the directive which would be used to parse the given string.
#
# The following directives can be embedded in the format string:
#    %a - abbreviated weekday name
#    %A - full weekday name
#    %b - abbreviated month name
#    %B - full month name
#    %c - preferred date and time representation
#    %C - century number (the year divided by 100, range 00 to 99)
#    %d - day of the month (01 to 31)
#    %D - same as %m/%d/%y
#    %e - day of the month (1 to 31)
#    %g - like %G, but without the century
#    %G - 4-digit year corresponding to the ISO week number (see %V).
#    %h - same as %b
#    %H - hour, using a 24-hour clock (00 to 23)
#    %I - hour, using a 12-hour clock (01 to 12)
#    %j - day of the year (001 to 366)
#    %m - month (01 to 12)
#    %M - minute
#    %n - newline character
#    %p - either am or pm according to the given time value
#    %r - time in a.m. and p.m. notation
#    %R - time in 24 hour notation
#    %S - second
#    %t - tab character
#    %T - current time, equal to %H:%M:%S
#    %u - weekday as a number (1 to 7), Monday = 1.
#          Warning: In Sun Solaris, Sunday = 1.
#    %U - week number of the current year, starting with the first Sunday as the
#          first day of the first week
#    %V - The ISO 8601 week number of the current year (01 to 53), where week
#          1 is the first week that has at least 4 days in the current year, and with Monday
#          as the first day of the week.
#    %W - week number of the current year, starting with the first Monday as the
#          first day of the first week.
#    %w - day of the week as a decimal, Sunday = 0.
#    %x - preferred date representation without the time
#    %X - preferred time representation without the date
#    %y - year without a century (range 00 to 99)
#    %Y - year including the century
#    %Z or %z - time zone or name or abbreviation
#    %% - a literal % character
#
#   Return Value
#       This return value is struct_time as returned by gmtime() or localtime().

struct_time = time.strptime("21 Jul 17", "%d %b %y")
print("Returned tuple:", struct_time)

# Example of time()
print(time.time())
print(time.asctime())




