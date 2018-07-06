#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from icalendar import Calendar, Event
from datetime import *
from dateutil.parser import parse
from pytz import UTC # timezone

cal_file = '/Users/gyyoon/Desktop/pentaa.ics'

MEETING_STR = '[회의]'
TEATIME_STR = '[Tea-Time]'
WORK_STR = '[업무]'
NONWORK_STR = '[비업무]'
LUNCH_STR = '[점심]'
CLUB_STR = '[동호회]'
WORKCLEAN_STR = '[업무정리]'
TALK_STR = '[면담]'
OUTWORK_STR = '[외근]'
BREAK_STR = '[휴식]'
TOGETHER_CTR = '[회식]'
SEATCLEAN_STR = '[자리정리]'
EVENT_STR = '[행사]'

# Count global var
total_cnt = 0
work_cnt = 0
nonwork_cnt = 0
meeting_cnt = 0
lunch_cnt = 0
club_cnt = 0
workclean_cnt = 0
outwork_cnt = 0
unknown_cnt = 0
break_cnt = 0
together_cnt = 0
seatclean_cnt = 0
event_cnt = 0

# Duration global var
work_dur = timedelta(hours=0, minutes=0)
nonwork_dur = timedelta(hours=0, minutes=0)
meeting_dur = timedelta(hours=0, minutes=0)
lunch_dur = timedelta(hours=0, minutes=0)
club_dur = timedelta(hours=0, minutes=0)
workclean_dur = timedelta(hours=0, minutes=0)
outwork_dur = timedelta(hours=0, minutes=0)
break_dur = timedelta(hours=0, minutes=0)
together_dur = timedelta(hours=0, minutes=0)
seatclean_dur = timedelta(hours=0, minutes=0)
event_dur = timedelta(hours=0, minutes=0)


def process_work_event( comp ):
    # Duration global var
    global work_dur

    start_dt = comp.get('dtstart').dt
    end_dt = comp.get('dtend').dt
    duration = end_dt - start_dt

    work_dur += duration


def process_nonwork_event( comp ):
    # Duration global var
    global nonwork_dur

    start_dt = comp.get('dtstart').dt
    end_dt = comp.get('dtend').dt
    duration = end_dt - start_dt

    nonwork_dur += duration


def process_meeting_event( comp ):
    # Duration global var
    global meeting_dur

    start_dt = comp.get('dtstart').dt
    end_dt = comp.get('dtend').dt
    duration = end_dt - start_dt

    meeting_dur += duration


def process_lunch_event( comp ):
    # Duration global var
    global lunch_dur

    start_dt = comp.get('dtstart').dt
    end_dt = comp.get('dtend').dt
    duration = end_dt - start_dt

    lunch_dur += duration


def process_club_event( comp ):
    # Duration global var
    global club_dur

    start_dt = comp.get('dtstart').dt
    end_dt = comp.get('dtend').dt
    duration = end_dt - start_dt

    club_dur += duration


def process_workclean_event( comp ):
    # Duration global var
    global workclean_dur

    start_dt = comp.get('dtstart').dt
    end_dt = comp.get('dtend').dt
    duration = end_dt - start_dt

    workclean_dur += duration


def process_outwork_event( comp ):
    # Duration global var
    global outwork_dur

    start_dt = comp.get('dtstart').dt
    end_dt = comp.get('dtend').dt
    duration = end_dt - start_dt

    outwork_dur += duration


def process_break_event( comp ):
    # Duration global var
    global break_dur

    start_dt = comp.get('dtstart').dt
    end_dt = comp.get('dtend').dt
    duration = end_dt - start_dt

    break_dur += duration


def process_together_event( comp ):
    # Duration global var
    global together_dur

    start_dt = comp.get('dtstart').dt
    end_dt = comp.get('dtend').dt
    duration = end_dt - start_dt

    together_dur += duration


def process_seatclean_event( comp ):
    # Duration global var
    global seatclean_dur

    start_dt = comp.get('dtstart').dt
    end_dt = comp.get('dtend').dt
    duration = end_dt - start_dt

    seatclean_dur += duration


def process_event_event( comp ):
    # Duration global var
    global event_dur

    start_dt = comp.get('dtstart').dt
    end_dt = comp.get('dtend').dt
    duration = end_dt - start_dt

    event_dur += duration


def print_results():
    print('----------------------------------')

    print('total count : ' + str(total_cnt) )
    print('meeting : ' + str(meeting_cnt))
    print('work : ' + str(work_cnt))
    print('nonwork : ' + str(nonwork_cnt))
    print('lunch : ' + str(lunch_cnt))
    print('unknown ' + str(unknown_cnt))

    print('----------------------------------')

    print('workdur : ' + str(work_dur))
    print('nonwork dur : ' + str(nonwork_dur))
    print('meeting dur : ' + str(meeting_dur))
    print('lunch dur : ' + str(lunch_dur))
    print('club dur : ' + str(club_dur))
    print('workclean dur : ' + str(workclean_dur))
    print('outwork dur : ' + str(outwork_dur))
    print('break dur : ' + str(break_dur))
    print('together dur : ' + str(together_dur))
    print('seatclean dur : ' + str(seatclean_dur))
    print('event dur : ' + str(event_dur))

    print('----------------------------------')


class eventProcessor():
    def __init__:
        print('Initialize')

    def calc_event_duration( component ):
        start_dt = component.get('dtstart').dt
        end_dt = component.get('dtend').dt
        duration = end_dt - start_dt

        return duuration


def main():
    # Count global var
    global total_cnt
    global work_cnt
    global nonwork_cnt
    global meeting_cnt
    global lunch_cnt
    global club_cnt
    global workclean_cnt
    global outwork_cnt
    global break_cnt
    global together_cnt
    global seatclean_cnt
    global event_cnt
    global unknown_cnt

    g = open(cal_file,'rb')
    gcal = Calendar.from_ical(g.read())

    for component in gcal.walk():
        if component.name == "VEVENT":
            start_date = component.get('dtstart').dt
            end_date = component.get('dtend').dt

            # I don't know why, but same formatted strs have differecne types,
            # date or datetime, so I unified them to date type(datetime requires
            # timezone set...)
            if type(start_date) != type(date(2018, 4, 4)):
                start_date = start_date.date()

            if type(end_date) != type(date(2018, 4, 4)):
                end_date = end_date.date()


            # 1 Half.
            # Maybe perhaps someday I should get inputs from user that specifies
            # the date range...
            if start_date >= date(2018, 1, 1) and end_date <= date(2018, 6, 30):
                total_cnt += 1

                event_summary = component.get('summary')

                if WORK_STR in event_summary:
                    work_cnt += 1
                    process_work_event( component )

                elif MEETING_STR in event_summary or TEATIME_STR in \
                        event_summary or TALK_STR in event_summary:
                    meeting_cnt += 1
                    process_meeting_event( component )

                elif NONWORK_STR in event_summary:
                    nonwork_cnt += 1
                    process_nonwork_event( component )

                elif LUNCH_STR in event_summary:
                    lunch_cnt += 1
                    process_lunch_event( component )

                elif CLUB_STR in event_summary:
                    club_cnt += 1
                    process_club_event( component )

                elif WORKCLEAN_STR in event_summary:
                    workclean_cnt += 1
                    process_workclean_event( component )

                elif OUTWORK_STR in event_summary:
                    outwork_cnt += 1
                    process_outwork_event( component )

                elif BREAK_STR in event_summary:
                    break_cnt += 1
                    process_break_event( component )

                elif TOGETHER_CTR in event_summary:
                    together_cnt += 1
                    process_together_event( component )

                elif SEATCLEAN_STR in event_summary:
                    seatclean_cnt += 1
                    process_seatclean_event( component )

                elif EVENT_STR in event_summary:
                    event_cnt += 1
                    process_event_event( component )

                else:
                    unknown_cnt += 1
                    print(event_summary)
                    print(component.get('dtstart').dt)
                    print(component.get('dtend').dt)
                    print(component.get('dtstamp').dt)
    g.close()

    print_results()


if __name__ == "__main__":
    main()

