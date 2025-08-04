#pragma once

#include <string>
#include <list>
#include "global.h"
#include "Score.h"
#include "GolfCourse.h"

class Personal
{
private:
	std::string name;
	std::list<Score> scores;
	double avgHandicap;

public:
	Personal(std::string name = "Unknown");

	void setName(std::string name);
	std::string getName();

	void addScore(Score S);
	void updateHdcp(double hdcp);

	//TODO: printPerson (name, handicap avg, (Optional* maybe add most played course Optional*)

};

