#pragma once

#include <list>
#include "Personal.h"
#include "GolfCourse.h"

class App
{
private:
	Personal user;
	std::list<GolfCourse> Courses;

public:
	// backend

	int init();
	int run();

	//terminal

	int addNewRound(GolfCourse& GC);
	GolfCourse selectCourse();

	//calculations

	double hdcpDiff(int score, double slope, double rating);
	double hdcpIndex(Personal& user);	// calculates handicap Index based on stored hdcp differentials 
	double courseHdcp(double hdcpIndex, GolfCourse& GC);
};

