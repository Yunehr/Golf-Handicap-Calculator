#include "GolfCourse.h"

GolfCourse::GolfCourse(std::string name,int par, double slope, double rating)
{
	this->name = name;
	this->par = par;
	this->slope = slope;
	this->rating = rating;
	this->courseHdcp = 0;	// I know it is a magic number, but the default for course handicap should be 0 0, thus not applicable for DEFAULT (-7) to be used
}

void GolfCourse::setName(std::string name)
{
	this->name = name;
}

std::string GolfCourse::getName()
{
	return this->name;
}

void GolfCourse::setPar(int par)
{
}

int GolfCourse::getPar()
{
	return 0;
}

void GolfCourse::setSlope(double slope)
{
	this->slope = slope;
}

double GolfCourse::getSlope()
{
	return slope;
}

void GolfCourse::setRating(double rating)
{
	this->rating = rating;
}

double GolfCourse::getRating()
{
	return rating;
}

void GolfCourse::setHandicap(double courseHdcp)
{
	this->courseHdcp = courseHdcp;
}

double GolfCourse::getHandicap()
{
	return courseHdcp;
}
