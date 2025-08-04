#include "Personal.h"
#include <iostream>
#include <fstream>

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


double Personal::getAvgDiff()
{	
	int count = 0;
	double sum = 0;
	double avg = 0;
	std::list<double> temparray;
	for (Score s : scores) {
		temparray.push_back(s.getDifferential());
		count++;
	}
	if (count <= DIFFERENTIAL_INDEX) {
		for (double val : temparray) {
			sum += val;
		}
		if (count == 0) {
			// TODO: Print error statement
			return -1; //cannot div by zero 
		}
		avg = sum / count;
	}
	else {
		temparray.sort();
		count = 0;
		for (auto it = temparray.begin(); it != temparray.end() && count < DIFFERENTIAL_INDEX; ++it, count++) {
			sum += *it;
		}
		avg = sum / DIFFERENTIAL_INDEX;
	}
	return avg;
}

void Personal::updateHdcp(double hdcp)
{
	this->avgHandicap = hdcp;
}

int Personal::writeScores(std::ofstream& fout)
{
	if (fout.is_open()) {
		for (Score S : scores) {
			fout << S.getName() << std::endl;
			fout << S.getRoundScore() << std::endl;
			fout << S.getDifferential() << std::endl;
			fout << S.getFinalScore() << std::endl;
		}
	}
	else {
		std::cout << "Error reading Round Scores from file: " << USER_FILE << std::endl;
		return EXIT_FAILURE;
	}

	return EXIT_SUCCESS;
}
