#include "Score.h"

Score::Score(std::string courseName, int roundScore, double roundDiff, int finalScore)
{
	this->courseName = courseName;
	this->roundScore = roundScore;
	this->roundDiff = roundDiff;
	this->finalScore = finalScore;

}

std::string Score::getName()
{
	return this->courseName;
}

int Score::getRoundScore()
{
	return this->roundScore;
}

double Score::getDifferential()
{
	return this->roundDiff;
}

int Score::getFinalScore()
{
	return this->finalScore;
}
