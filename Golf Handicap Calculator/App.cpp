#include "App.h"





int App::init() // does nothing for now
{
    return 0;
}

int App::run()  // does nothing for now
{
    return 0;
}

int App::addNewRound(GolfCourse& GC)  //terminal function that adds a new round to a user's personal list of scores
{
    // enter round score
    int score = DEFAULT;

    //final score calc
    int finalScore = GC.getPar() - (score - GC.getHandicap());      // par - (score - course handicap)      // ex. -1 (1 under par), +8 (8 over par)

    // updade final score
    user.addScore(Score(GC.getName(), score, hdcpDiff(score, GC.getSlope(), GC.getRating()), finalScore));

    return 0;
}

GolfCourse App::selectCourse()
{
    return GolfCourse();
}

double App::hdcpDiff(int score, double slope, double rating)
{   //Handicap Differential = (Adjusted Gross Score - Course Rating) / (Standard Difficulty Rating * Slope Rating)
    return (score - rating) / (SDR * slope);
}

double App::hdcpIndex(Personal& user)
{   //Handicap Index = avg( top 8 Handicap Differentials ) * Index Factor
    return user.getAvgDiff() * INDEX_FACTOR;
}

double App::courseHdcp(double hdcpIndex, GolfCourse& GC)
{   //Course Handicap =  Handicap Index * (Slope / Standard Dificulty Rating) + (Course Rating – Par)
    return  (hdcpIndex * (GC.getSlope() / SDR)) + (GC.getRating() - GC.getPar());
}
