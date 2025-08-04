#pragma once
#include <string>
#include "GolfCourse.h"

class Score
{
private:
	std::string courseName;
	int roundScore;						//actual course score
	double roundDiff;
	int finalScore;						//+x or -x from course par after handicap deductions

public:
	Score(std::string courseName, int roundScore, double roundDiff, int finalScore = 0);	// always done internally after all calculations so no need for setters

	std::string getName();
	int getRoundScore();
	double getDifferential();
	int getFinalScore();
	void setFinalScore(int finalScore);

	//TODO: print (used for printing out all scores in the list
};

