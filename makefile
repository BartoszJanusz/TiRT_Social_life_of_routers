CC=g++
CFLAGS=-c -O3
LDFLAGS=
SOURCES=main.cpp wlink.cpp wtree.cpp
OBJECTS=$(SOURCES:.c=.o)
EXECUTABLE=slor


all: $(SOURCES) $(EXECUTABLE)

$(EXECUTABLE): $(OBJECTS) 
	$(CC) $(LDFLAGS) $(OBJECTS) -o $@

.cpp.o:
	$(CC) $(CFLAGS) $< -o $@
