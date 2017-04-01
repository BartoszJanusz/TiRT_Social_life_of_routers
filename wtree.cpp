#include <iostream>

#include "wtree.h"

// constructor
// creates the wtree object out of a vector of wlinks
// the vector can contain n trees
// the tree that stars at position 0 of the vector is created
wtree::wtree(vector<wlink> * links)
{
	this->links = links;
	this->np = 0; 								        // set node pointer to 0
	wlink t = links->front();				   // fill node list with first link
	this->n.push_back(t.l1);	
	this->n.push_back(t.l2);
	this->nh[t.l1] = 0;						
	this->nh[t.l2] = 1;	
	wlink tmp(0, 1);
	this->t.push_back(tmp);	
	this->st.push_back(this->t.size()-1);
	this->links->erase(this->links->begin());		
	this->walkTree();
}

// constructor
// create the wtree object out of a vector of wtree objects
// essentially merges all wtree objects in the vector
// into one large tree
wtree::wtree(vector<wtree *> * trees)
{
	this->mergeTrees(trees);
}

// destructor
wtree::~wtree()
{
}

// helper function that prints information about a tree and it's structure
int wtree::printTree()
{
	vector<wlink>::iterator it;
	for(it = this->t.begin(); it < this->t.end(); it++)
	{
		cout << it->l1 << " : " << it->l2 << endl;
	}
	cout << "Links in Tree: " << this->t.size() << endl;
	cout << "Nodes in Tree: " << this->n.size() << endl;
	cout << "Links remaining overall " << this->links->size() << endl;
}

// walktree
// creates a tree using a vector of links
int wtree::walkTree()
{
	while(this->np < this->n.size() && this->n.size() != 0)
	{
								   // iterate over unconsumed nodes in node list
		int nph = this->n.size();
		for(int i = np; i<nph; i++) 	
		{
											 // iterate over all remaining links
			int search = this->n[i];
			
			for(int j = 0; j < this->links->size(); j++)
			{
				wlink tlink = this->links->at(j);
															  // check for match
				if(tlink.l1 == search || tlink.l2 == search)	
				{
					if(this->nh.count(tlink.l1) == 0)
					{
						this->n.push_back(tlink.l1);			
						this->nh[tlink.l1] = this->n.size() - 1;
						this->st.push_back(this->t.size());
					}	
					else if(this->nh.count(tlink.l2) == 0)
					{
						this->n.push_back(tlink.l2);			
						this->nh[tlink.l2] = this->n.size() - 1;
						this->st.push_back(this->t.size());
					}
					this->links->erase(this->links->begin()+j);
				
					wlink tmp;	
					if(tlink.l1 == search)
						tmp.setlink(this->nh[tlink.l1], this->nh[tlink.l2]);
					else
						tmp.setlink(this->nh[tlink.l2], this->nh[tlink.l1]);
					this->t.push_back(tmp);	
					j--;		
				}
			}	
		}
		this->np = nph;
	}
}

// mergeTrees
// creates a tree out of many trees by merging them into one
int wtree::mergeTrees(vector< wtree * > * trees)
{
	int no = 1;												      // node offset
			
	for(int i=0; i<trees->size(); i++)
	{
													   // add first node of tree
		wlink tmp;
		tmp.setlink(0, trees->at(i)->t[0].l1+no);	
		this->t.push_back(tmp);
		this->st.push_back(this->t.size()-1);
		int sto = 0; 								     // spanning tree offset
		for(int j=0; j<trees->at(i)->t.size(); j++)
		{
			wlink tmp2;											     // add link
			tmp2.setlink(trees->at(i)->t[j].l1+no, trees->at(i)->t[j].l2+no); 
			this->t.push_back(tmp2);
			if(trees->at(i)->st[sto] == j) 			   // add spanning tree link
			{
				this->st.push_back(this->t.size()-1);
				sto++;	
			}
		}	
		no += trees->at(i)->n.size();	
	}
	this->np = no;
	
}

// outputWalrusFormat
// outputs the tree in walrus format
int wtree::outputWalrusFormat()
{
    cout << "Graph" << endl;
    cout << "{" << endl;
    cout << "\t### metadata ###" << endl;
    cout << "\t@name=;" << endl;
    cout << "\t@description=;" << endl;
    if(this->n.size() > 0)
		cout << "\t@numNodes=" << this->n.size() << ";" << endl;
    else
		cout << "\t@numNodes=" << this->np << ";" << endl;
	cout << "\t@numLinks=" << this->t.size() << ";" << endl;
    cout << "\t@numPaths=0;" << endl;
    cout << "\t@numPathLinks=0;" << endl;
    cout << "" << endl;
    cout << "\t### structural data ###" << endl;
    cout << "\t@links=[" << endl;
	
	for(int i = 0; i<this->t.size(); i++)
	{
    	cout << "\t\t{ @source=" << this->t[i].l1 << "; " << 
			"@destination=" << this->t[i].l2 << "; }";
		if(i < this->t.size()-1)
			cout << "," << endl;
		else
			cout << endl;
	}
    
	cout << "\t];" << endl;
    cout << "\t@paths=;" << endl;
    cout << "" << endl;
    cout << "\t### attribute data ###" << endl;
    cout << "\t@enumerations=;" << endl;
    cout << "\t@attributeDefinitions=[" << endl;
    cout << "\t\t{" << endl;
    cout << "\t\t\t@name=$root;" << endl;
    cout << "\t\t\t@type=bool;" << endl;
    cout << "\t\t\t@default=|| false ||;" << endl;
    cout << "\t\t\t@nodeValues=[ { @id=0; @value=T; } ];" << endl;
    cout << "\t\t\t@linkValues=;" << endl;
    cout << "\t\t\t@pathValues=;" << endl;
    cout << "\t\t}," << endl;
    cout << "\t\t{" << endl;
    cout << "\t\t\t@name=$tree_link;" << endl;
    cout << "\t\t\t@type=bool;" << endl;
    cout << "\t\t\t@default=|| false ||;" << endl;
    cout << "\t\t\t@nodeValues=;" << endl;
    cout << "\t\t\t@linkValues=[" << endl;

	for(int i = 0; i<this->st.size(); i++)
	{
    	cout << "\t\t\t\t{ @id=" << this->st[i] << "; @value=T; }";
		if(i < this->st.size()-1)
			cout << "," << endl;
		else
			cout << endl;
	}
    
	cout << "\t\t\t];" << endl;
    cout << "\t\t\t@pathValues=;" << endl;
    cout << "\t\t}" << endl;
    cout << "\t];" << endl;
    cout << "\t@qualifiers=[" << endl;
    cout << "\t\t{" << endl;
    cout << "\t\t\t@type=$spanning_tree;" << endl;
    cout << "\t\t\t@name=$sample_spanning_tree;" << endl;
    cout << "\t\t\t@description=;" << endl;
    cout << "\t\t\t@attributes=[" << endl;
    cout << "\t\t\t\t{ @attribute=0; @alias=$root; }," << endl;
    cout << "\t\t\t\t{ @attribute=1; @alias=$tree_link; }" << endl;
    cout << "\t\t\t];" << endl;
    cout << "\t\t}" << endl;
    cout << "\t];" << endl;
    cout << "" << endl;
    cout << "\t### visualization hints ###" << endl;
    cout << "\t@filters=;" << endl;
    cout << "\t@selectors=;" << endl;
    cout << "\t@displays=;" << endl;
    cout << "\t@presentations=;" << endl;
    cout << "" << endl;
    cout << "\t### interface hints ###" << endl;
    cout << "\t@presentationMenus=;" << endl;
    cout << "\t@displayMenus=;" << endl;
    cout << "\t@selectorMenus=;" << endl;
    cout << "\t@filterMenus=;" << endl;
    cout << "\t@attributeMenus=;" << endl;
    cout << "}" << endl;	
	return 0;    
}
