#include "wlink.h"

wlink::wlink(){}

wlink::wlink(int l1, int l2)
{
	this->l1 = l1;
	this->l2 = l2;
	return;
}

int wlink::setlink(int l1, int l2)
{
	this->l1 = l1;
	this->l2 = l2;
	return 0;
}

