// this is a simple project to be able to calculate one's golf handicap at a given course

// what is done in this project
//		- store round scores at "X" golf courses
//		- store golf courses (including slope/rating for each tee block)
//		- calculate course handicap, and average handicap
//		- display round final score based on course handicap
//

#include <iostream>
#include "Terminal.h"

int main(void) {

	int score = Terminal::getScore();

	std::cout << "Given score: " << score << std::endl;

	return 0;
}