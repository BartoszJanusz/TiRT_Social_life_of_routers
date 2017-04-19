CXX?=g++
CXXFLAGS=-c -O3 -std=c++11
LDFLAGS=
SOURCES=wlink.cpp wtree.cpp main.cpp
OBJECTS=$(SOURCES:.cpp=.o)
EXECUTABLE=slor


all: $(SOURCES) $(EXECUTABLE)

$(EXECUTABLE): $(OBJECTS) 
	$(CXX) $(LDFLAGS) $(OBJECTS) -o $@

.cpp.o:
	$(CXX) $(CXXFLAGS) $< -o $@
