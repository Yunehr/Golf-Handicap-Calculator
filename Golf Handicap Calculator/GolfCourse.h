#pragma once
#include <string>

#include "global.h"

class GolfCourse
{
private:
	std::string name; 
	int par;
	double slope;
	double rating;
	double courseHdcp;

public:
	GolfCourse(std::string name = "Unknown",int par = DEFAULT, double slope = DEFAULT, double rating = DEFAULT);

	void setName(std::string name);
	std::string getName();

	void setPar(int par);
	int getPar();

	void setSlope(double slope);
	double getSlope();

	void setRating(double rating);
	double getRating();

	void setHandicap(double courseHdcp);
	double getHandicap();

	//TODO: PrintGolfCourse
};

