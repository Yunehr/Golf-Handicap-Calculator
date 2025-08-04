#include "Personal.h"

Personal::Personal(std::string name)
{
	this->name = name;
	this->avgHandicap = DEFAULT;
}

void Personal::setName(std::string name)
{
	this->name = name;
}

std::string Personal::getName()
{
	return this->name;
}

void Personal::addScore(Score S)
{
	scores.push_back(S);
}

void Personal::updateHdcp(double hdcp)
{
	this->avgHandicap = hdcp;
}
