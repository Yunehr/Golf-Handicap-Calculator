#include "Terminal.h"
#include <iostream>
#define NOMINMAX
#include <Windows.h>


int Terminal::getScore()
{
	system("cls");
	int score = 0;
	while (true) {
		
		std::cout << "Enter your Score Here --> ";
		std::cin >> score;

		if (std::cin.fail()) {
			std::cin.clear();
			std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n'); // Clear Input Buffer
			std::cout << "Invalid input. Please Enter your Golf Score." << std::endl;
			Sleep(1000);
		}
		else {
			std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n'); // Remove any extra input
			
			std::string option;
			std::cout << "Do you wish to register " << score << " as your Score [Y/N] -> ";
			std::cin >> option;
			if (option == "Y" || option == "y") {
				std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
				std::cout << "Registering " << score << " to new round" << std::endl;
				Sleep(1000);
				system("cls");
				break;
			}
			else {
				std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n'); 
				std::cout << "Resetting..." << std::endl;
				Sleep(1000);
				system("cls");
			}
			
		}
	}
    return score;
}
