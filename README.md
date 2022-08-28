# Python Calendar Calculations
Calendrical calculations allowing date conversion between the [Gregorian](https://en.wikipedia.org/wiki/Gregorian_calendar), [Revised Julian \(Milanković\)](https://en.wikipedia.org/wiki/Revised_Julian_calendar), and [Julian](https://en.wikipedia.org/wiki/Julian_calendar) calendars.


These functions use the concept of a Chronological Julian Day Number \(CJDN\). Using these functions, a date on any of the Gregorian, Revised Julian (Milanković), or Julian calendars may be converted to a date on one of the other of those calendars.

The Chronological Julian Day Number is a whole number representing a day.
 Its day begins at 00:00 Local Time. The zero point for a Julian Date \(JD 0.0\) corresponds to 12.00 UTC, 1 January -4712 \(i.e. 4713&nbsp;BC\). The zero point for the CJDN is 1 January -4712 \(the whole day in local time\). For more information see: [Julian Day](http://aa.quae.nl/en/reken/juliaansedag.html) .

* Conversations from a calendar date to a CJDN
  * `pGregorianToCJDN` : expects Year, Month, Day as strings or integers. Outputs a Chronological Julian Day Number \(CJDN\) for the given date on the Gregorian calendar.
  * `pMilankovicToCJDN` : expects Year, Month, Day as strings or integers. Outputs a Chronological Julian Day Number \(CJDN\) for the given date on the Revised Julian \(or Milanković\) calendar.
  * `pJulianToCJDN` : expects Year, Month, Day as strings or integers. Outputs a Chronological Julian Day Number \(CJDN\) for the given date on the Julian calendar.
* Converstions from CJDN to calendar dates
  * `pCJDNToGregorian` : Expects a CJDN. There are also three optional parameters, which all default to False. This function usually returns a date on the Gregorian calendar for a given CJDN. The date is a string in ISO 8601 YYYY-MM-DD format. If, however, one of the optional parameters is set to True \(in order: Year, Month, Day\), that part of the date \(i.e. the year, the month, or the day\) is returned as an integer.
  * `pCJDNToMilankovic` : Expects a CJDN. There are also three optional parameters, which all default to False. This function usually returns a date on the Revised Julian \(or Milanković\) calendar for a given CJDN. The date is a string in ISO 8601 YYYY-MM-DD format. If, however, one of the optional parameters is set to True \(in order: Year, Month, Day\), that part of the date \(i.e. the year, the month, or the day\) is returned as an integer.
  * `pCJDNToJulian` : Expects a CJDN. There are also three optional parameters, which all default to False. This function usually returns a date on the Julian calendar for a given CJDN. The date is a string in ISO 8601 YYYY-MM-DD format. If, however, one of the optional parameters is set to True \(in order: Year, Month, Day\), that part of the date \(i.e. the year, the month, or the day\) is returned as an integer.

* `DoW` : expects a CJDN and the calendar to use. It returns the day of the week for the given CJDN on the requested calendar. If the calendar is not supplied, the function defaults to calculating the day of the week on the Gregorian calendar. As elsewhere, 1 = the Julian calendar, 2 = the Revised Julian \(Milanković\) calendar, and 3 = the Gregorian calendar. The day of the week is returned as an ISO 8601 integer, where Monday = 1 and Sunday = 7.

This Python script imports `datetime` and two functions \(`floor` and `fmod`\) from the `math` package. The script is written in Python 3 \(minimum version 0x030000F0\). As most of it consists of mathematical calculations, I do not envisage any issues using the functions in an earlier version of Python.

