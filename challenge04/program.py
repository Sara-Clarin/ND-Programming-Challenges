#!/usr/bin/env python3

import sys, collections
from enum import IntEnum
import functools


class EType(IntEnum):
    START = 1
    END   = 2

Event = collections.namedtuple("Event", "time type")
  
events = []

def count_concurrents( events ):
    in_session = 0
    rooms = 0

    events = sorted( events, key=lambda e: (e.time, e.type))  # sort by time, then if it's start or end
    #events = sorted( events, key=lambda e: e.type)

    for event in events:
        if event.type == EType.START:   # new event started: add to stack
            in_session += 1

        else:                           # an event has ended
            in_session -= 1

        if in_session > rooms:          # ramzi needs to book another room
            rooms += 1 
        #print(f'{event.time} {event.type}')
        

    return rooms

def main():

    count = 0
    while line := sys.stdin.readline():
        n = int( line.strip() )
        count += 1
        events.clear()
        for i in range(n):
            start, end =  sys.stdin.readline().split()
            #event1 = Event(start , EType.START)
            #event2 = Event( end , EType.END)
            #events.append(event1)
            #events.append(event2)
            events.append( Event(start, EType.START))
            events.append( Event(end, EType.END))

    #for event in events:
        #print(f'{event.time} {event.type}')
   
        num_concurrent = count_concurrents(events)
        print(f'{count}. Maximum number of concurrent events is {num_concurrent}')



if __name__ == "__main__":
    main()
