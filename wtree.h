#ifndef H_WTREE
#define H_WTREE

#include <ext/hash_map>
#include <vector>
#include "stdio.h"
#include "wlink.h"

using namespace std;
using namespace __gnu_cxx;

class wtree 
{
	public:
		vector<int> n;                        // keeps all the nodes of the tree
		vector<int> st;								  // keeps the spanning tree
		hash_map<int, int> nh; 					// hash map of nodes of the tree
		int np;				    // points to the last processed node of the tree
		vector<wlink> t; 										     // the tree
		vector<wlink> * links;			    	   // pointer to input file data

		wtree(vector<wlink> *);
		wtree(vector< wtree * > *);
		~wtree();

		int printTree();
		int outputWalrusFormat();

	private:
		int walkTree();
		int mergeTrees(vector<wtree *> *);
};

#endif
