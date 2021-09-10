#!/usr/bin/env python3


# Sara Clarin
# Challenge04: Concurrent events
# 9/9/2021

import sys, collections
from enum import IntEnum
import functools


class EType(IntEnum):
    START = 1
    END   = 2

Event = collections.namedtuple("Event", "time type")
  
events = []

def count_concurrents( events ):
    ''' Function that sorts events based on time and then on START or END value, and keeps record of rooms needed'''
    in_session = 0
    rooms = 0

    events = sorted( events, key=lambda e: (e.time, e.type))  # sort by time, then start or end

    for event in events:
        if event.type == EType.START:   # new event started: add to stack
            in_session += 1

        else:                           # an event has ended
            in_session -= 1

        if in_session > rooms:          # ramzi needs to book another room
            rooms += 1 

    return rooms


def main():

    count = 0
    while line := sys.stdin.readline():
        n = int( line.strip() )
        count += 1
        events.clear()

        for i in range(n):
            start, end = map(int, sys.stdin.readline().split())
            events.append( Event(start, EType.START))
            events.append( Event(end, EType.END))

   
        num_concurrent = count_concurrents(events)
        print(f'{count}. Maximum number of concurrent events is {num_concurrent}')



if __name__ == "__main__":
    main()
