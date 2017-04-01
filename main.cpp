/*

Copyright (c) 2008, Sebastian Schaetz
Source and Documentation: http://www.soa-world.de/echelon/walruscsv

All rights reserved.

Redistribution and use in source and binary forms, with or without modification, 
are permitted provided that the following conditions are met:

    * Redistributions of source code must retain the above copyright notice, 
      this list of conditions and the following disclaimer.
    * Redistributions in binary form must reproduce the above copyright notice, 
      this list of conditions and the following disclaimer in the documentation 
      and/or other materials provided with the distribution.
    * Neither the name of the organization nor the names of its contributors 
      may be used to endorse or promote products derived from this software 
      without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
"AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR
CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR
PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.



*/

#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <ext/hash_map>
#include "stdio.h"

#include "wtree.h"
#include "wlink.h"

namespace __gnu_cxx
{
        template<> struct hash< std::string >
        {
                size_t operator()(const std::string& x) const
                {
                        return hash< const char* >()( x.c_str() );
                }
        };
}

using namespace std;
using namespace __gnu_cxx;


// reads a csv file into a vector of links
// each line of the csv file represents a link like this:
// nodename1 <seperator> nodename2
int load_csv_file(char * filename, const char * seperator, vector<wlink> * links)
{
    ifstream csvfile(filename);                                     // open file
    if(csvfile.is_open())
    {
        int i=0;
        hash_map<string, int> h;                  // hash map to store the nodes
        while(!csvfile.eof())                               // read line by line
        {
          string line;
          getline(csvfile,line);
          int pos = line.find(seperator, 0);     // first occurence of seperator
          if(pos > 0)
          {
            string sn1 = line.substr(0, pos);
            string sn2 = line.substr(pos+1, line.length()-1);
            int in1 = 0, in2 = 0;
                               // check if node is a new node or already visited
            if(h.count(sn1) == 1)
              in1 = h[sn1];
            else
            {
              in1 = i;
              h[sn1] = i;
              i++;
            }
            if(h.count(sn2) == 1)
              in2 = h[sn2];
            else
            {
              in2 = i;
              h[sn2] = i; 
              i++;
            }
            
            wlink l;
            l.l1 = in1;
            l.l2 = in2;
            links->push_back(l);
          }
        }
        csvfile.close();
        return 0;
    }
    else return -1;
}


int main(int argc, char * argv[])
{
    vector<wlink> filevec;
    load_csv_file(argv[1], ",", &filevec);
	vector<wtree *> treevec;
	while(filevec.size() > 0)
	{
		treevec.push_back(new wtree(&filevec));
	}
	wtree maintree(&treevec);
	maintree.outputWalrusFormat();
	return 0;
}
