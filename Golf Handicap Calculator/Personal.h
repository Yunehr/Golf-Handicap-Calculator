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
	double getAvgDiff();
	void updateHdcp(double hdcp);

	int writeScores(std::ofstream& fout);
	//TODO: printPerson (name, handicap avg, (Optional* maybe add most played course Optional*)

};

