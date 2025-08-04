#pragma once
#include "GolfCourse.h"
#include "Personal.h"

class FileIO
{

public:
	Personal readUser();
	std::list<GolfCourse> readGC();

	void write(std::list<GolfCourse> Courses);
	void write(Personal user);


};

