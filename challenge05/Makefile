$(CC) = gcc
$(CFLAGS) = -std=c++11
$(PROGRAM) = program.cpp

prog: program.o
    $(CC)  $(PROGRAM) $(CFLAGS) -o prog

program.o: $(PROGRAM)
    $(CC) $(CFLAGS) -c program.cc
