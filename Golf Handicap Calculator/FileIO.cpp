#include "FileIO.h"
#include <iostream>
#include <fstream>

Personal FileIO::readUser()
{
    // open file

    // error handling
        // if file cannot be opened
        //
        // if file empty

    //read 
        // Name
        // avgHandicap

    // while file not empty
        // Score

    return Personal();
}

std::list<GolfCourse> FileIO::readGC()
{
    // open file

    // error handling
        // if file cannot be opened
        //
        // if file empty

    //while file not empty
        // Name
        // Par
        // Slope
        // Rating
        // Handicap

    return std::list<GolfCourse>();
}

void FileIO::write(std::list<GolfCourse> Courses)
{
    std::ofstream fout;
    fout.open(GC_FILE);
    std::cout << "Opening File: " << GC_FILE << std::endl;
    if (fout.is_open()) {
        std::cout << "Loading Golf Course Data..." << std::endl;
        for (GolfCourse GC : Courses) {
            fout << GC.getName() << std::endl;
            fout << GC.getPar() << std::endl;
            fout << GC.getSlope() << std::endl;
            fout << GC.getRating() << std::endl;
            fout << GC.getHandicap() << std::endl;
        }
    }
    else {
        std::cout << "Cannot Open File: " << GC_FILE << std::endl;
        exit(EXIT_FAILURE);
    }
    fout.close();
}

void FileIO::write(Personal user)
{
    std::ofstream fout;
    fout.open(USER_FILE);
    std::cout << "Opening File: " << USER_FILE << std::endl;
    if (fout.is_open()) {
        std::cout << "Loading User Data..." << std::endl;
        fout << user.getName() << std::endl;
        fout << user.getAvgDiff() << std::endl;

        if (user.writeScores(fout) == EXIT_FAILURE) {
            exit(EXIT_FAILURE);
        }
    }
    else {
        std::cout << "Cannot Open File: " << USER_FILE << std::endl;
        exit(EXIT_FAILURE);
    }
    fout.close();
}
