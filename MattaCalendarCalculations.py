#!/usr/bin/env python3
'''
Created on 27/01/2013

@author: matta

Contains functions for finding the date of Easter according to the
   Gregorian, Julian, and Orthodox calendars.
'''


import datetime
from math import floor
from math import fmod

def pGregorianToCJDN(sYear, sMonth, sDay):
    ''' Converts a Gregorian date passed in a three strings (year, month, day) to a
           Chronological Julian Day Number.
        The Chronological Julian Day Number is a whole number representing a day.
        Its day begins at 00:00 Local Time.
        The zero point for a Julian Date (JD 0.0) corresponds to 12.00 UTC, 1 January -4712.
        The zero point for the CJDN is 1 January -4712 (the whole day in local time).
        From: http://aa.quae.nl/en/reken/juliaansedag.html .
    '''
    iYear = int(sYear)
    iMonth = int(sMonth)
    iDay = int(sDay)

    iC0 = floor((iMonth - 3) / 12)
    iX4 = iYear + iC0
    iX3 = floor(iX4 / 100)
    iX2 = int(fmod(iX4, 100))
    iX1 = iMonth - (12 * iC0) - 3
    iJ = floor((146097 * iX3) / 4) + floor((36525 * iX2) / 100) + floor(((153 * iX1) + 2) / 5) + iDay + 1721119

    return iJ

def pCJDNToGregorian(iCJDN, bDoYear=False, bDoMonth=False, bDoDay=False):
    ''' Returns a Gregorian date is ISO 8601 YYYY-MM-DD format from a given
        Chronological Julian Day Number (CJDN).
        If only part of the date is required (e.g. just the day), this is returned as an integer.
    '''

    if not isinstance(iCJDN, int):
        return False

    #Perform the calculation
    iK3 = (4 * (iCJDN - 1721120)) + 3
    iX3 = floor(iK3 / 146097)
    iK2 = (100 * floor(int(fmod(iK3, 146097)) / 4)) + 99
    iX2 = floor(iK2 / 36525)
    iK1 = (5 * floor(int(fmod(iK2, 36525)) / 100)) + 2
    iX1 = floor(iK1 / 153)
    iC0 = floor((iX1 + 2) / 12)
    iYear = (100 * iX3) + iX2 + iC0
    iMonth = (iX1 - (12 * iC0)) + 3
    iDay = floor(int(fmod(iK1, 153)) / 5) + 1

    #Return integer part, if only one part of the date is required.
    #Start at year, and rudely ignore any subsequent integers requested.
    if bDoYear:
        return iYear
    if bDoMonth:
        return iMonth
    if bDoDay:
        return iDay

    #Return the ISO 8601 date string
    sISO8601Date = ('0000' + str(iYear))[-4:] + '-' + ('00' + str(iMonth))[-2:] + '-' + ('00' + str(iDay))[-2:]
    return sISO8601Date

def pMilankovicToCJDN(sYear, sMonth, sDay):
    ''' Converts a Revised Julian or Milanković date passed in a three strings (year, month, day) to a
           Chronological Julian Day Number.
        The Chronological Julian Day Number is a whole number representing a day.
        Its day begins at 00:00 Local Time.
        The zero point for a Julian Date (JD 0.0) corresponds to 12.00 UTC, 1 January -4712.
        The zero point for the CJDN is 1 January -4712 (the whole day in local time).
        From: http://aa.quae.nl/en/reken/juliaansedag.html .
    '''
    iYear = int(sYear)
    iMonth = int(sMonth)
    iDay = int(sDay)

    iC0 = floor((iMonth - 3) / 12)
    iX4 = iYear + iC0
    iX3 = floor(iX4 / 100)
    iX2 = int(fmod(iX4, 100))
    iX1 = iMonth - (12 * iC0) - 3
    iJ = floor(((328718 * iX3) + 6) / 9) + floor((36525 * iX2) / 100) + floor(((153 * iX1) + 2) / 5) + iDay + 1721119

    return iJ

def pCJDNToMilankovic(iCJDN, bDoYear=False, bDoMonth=False, bDoDay=False):
    ''' Returns a Revised Julian date is ISO 8601 YYYY-MM-DD format from a given
        Chronological Julian Day Number (CJDN).
        If only part of the date is required (e.g. just the day), this is returned as an integer.
    '''

    if not isinstance(iCJDN, int):
        return False

    #Perform the calculation
    iK3 = (9 * (iCJDN - 1721120)) + 2
    iX3 = floor(iK3 / 328718)
    iK2 = (100 * floor(int(fmod(iK3, 328718)) / 9)) + 99
    iX2 = floor(iK2 / 36525)
    iK1 = (5 * floor(int(fmod(iK2, 36525)) / 100)) + 2
    iX1 = floor(iK1 / 153)
    iC0 = floor((iX1 + 2) / 12)
    iYear = (100 * iX3) + iX2 + iC0
    iMonth = (iX1 - (12 * iC0)) + 3
    iDay = floor(int(fmod(iK1, 153)) / 5) + 1

    #Return integer part, if only one part of the date is required.
    #Start at year, and rudely ignore any subsequent integers requested.
    if bDoYear:
        return iYear
    if bDoMonth:
        return iMonth
    if bDoDay:
        return iDay

    #Return the ISO 8601 date string
    sISO8601Date = ('0000' + str(iYear))[-4:] + '-' + ('00' + str(iMonth))[-2:] + '-' + ('00' + str(iDay))[-2:]
    return sISO8601Date

def pJulianToCJDN(sYear, sMonth, sDay):
    ''' Converts a Julian date passed in a three strings (year, month, day) to a
           Chronological Julian Day Number.
        The Chronological Julian Day Number is a whole number representing a day.
        Its day begins at 00:00 Local Time.
        The zero point for a Julian Date (JD 0.0) corresponds to 12.00 UTC, 1 January -4712.
        The zero point for the CJDN is 1 January -4712 (the whole day in local time).
        From: http://aa.quae.nl/en/reken/juliaansedag.html .
    '''
    iYear = int(sYear)
    iMonth = int(sMonth)
    iDay = int(sDay)

    iJ0 = 1721117
    iC0 = floor((iMonth - 3) / 12)
    iJ1 = floor(((iC0 + iYear) * 1461) / 4)
    iJ2 = floor(((153 * iMonth) - (1836 * iC0) - 457) / 5)
    iJ = iJ1 + iJ2 + iDay + iJ0

    return iJ

def pCJDNToJulian(iCJDN, bDoYear=False, bDoMonth=False, bDoDay=False):
    ''' Returns a Julian date is ISO 8601 YYYY-MM-DD format from a given
        Chronological Julian Day Number (CJDN).
        If only part of the date is required (e.g. just the day), this is returned as an integer.
    '''

    if not isinstance(iCJDN, int):
        return False

    #Perform the calculation
    iY2 = iCJDN - 1721118
    iK2 = (4 * iY2) + 3
    iK1 = (5 * floor(int(fmod(iK2, 1461)) / 4)) + 2
    iX1 = floor(iK1 / 153)
    iC0 = floor((iX1 + 2) / 12)
    iYear = floor(iK2 / 1461) + iC0
    iMonth = (iX1 - (12 * iC0)) + 3
    iDay = floor(int(fmod(iK1, 153)) / 5) + 1

    #Return integer part, if only one part of the date is required.
    #Start at year, and rudely ignore any subsequent integers requested.
    if bDoYear:
        return iYear
    if bDoMonth:
        return iMonth
    if bDoDay:
        return iDay

    #Return the ISO 8601 date string
    sISO8601Date = ('0000' + str(iYear))[-4:] + '-' + ('00' + str(iMonth))[-2:] + '-' + ('00' + str(iDay))[-2:]
    return sISO8601Date

def DoW(iCJDN, iEDM=3):
    ''' Calculates the day of the week for a given date, for a given calendar.
        iEDM = 1 for Julian; 2 for Revised Julian, and 3 for Gregorian calendar.
    '''

    #Basic check of parameters
    if not isinstance(iCJDN, int):
        return False
    if not isinstance(iEDM, int):
        return False
    if (iEDM < 1) or (iEDM > 3):
        return False

    #Find the component parts of the date
    if iEDM == 1:
        iYear = pCJDNToJulian(iCJDN, True)
        iMonth = pCJDNToJulian(iCJDN, False, True)
        iDay = pCJDNToJulian(iCJDN, False, False, True)
    elif iEDM == 2:
        iYear = pCJDNToMilankovic(iCJDN, True)
        iMonth = pCJDNToMilankovic(iCJDN, False, True)
        iDay = pCJDNToMilankovic(iCJDN, False, False, True)
    else:
        #Gregorian is the default
        iYear = pCJDNToGregorian(iCJDN, True)
        iMonth = pCJDNToGregorian(iCJDN, False, True)
        iDay = pCJDNToGregorian(iCJDN, False, False, True)

    #Basic parts of calculation
    iA = floor((14 - iMonth) / 12)
    iY = iYear - iA
    iM = (iMonth + (12 * iA) - 2)

    #Per calendar calculations.
    #NB The Revised Julian calendar is the same as the Gregorian until AD 2800.
    if iEDM == 1:
        iD = int(fmod((5 + iDay + iY + floor(iY / 4) + floor((31 * iM) / 12)), 7))
    if (iEDM == 2) and (iYear < 2800):
        iD = int(fmod((((iDay + iY + floor(iY / 4)) - floor(iY / 100)) + floor((iY + 300) / 900) + floor((iY + 700) / 900) + floor((31 * iM) / 12)), 7))
    if (iEDM == 3) or ((iEDM == 2) and (iYear >= 2800)):
        iD = int(fmod((((iDay + iY + floor(iY / 4)) - floor(iY / 100)) + floor(iY / 400) + floor((31 * iM) / 12)), 7))

    #adjust day of week to correct ISO 8601 representation.
    #   Monday = 1; Sunday = 7
    if iD == 0:
        iD = 7

    return iD
