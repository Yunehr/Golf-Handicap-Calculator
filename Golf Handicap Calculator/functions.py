# Golf Handicap Calculator - Functions
# This file contains utility functions for the Golf Handicap Calculator app.

## Authentication Function
def check_credentials(username, password):
    """
    Check if the provided credentials are valid.
    Currently hardcoded for testing. Update this function for proper authentication.
    
    Args:
        username: The username to verify
        password: The password to verify
        
    Returns:
        True if credentials are valid, False otherwise
    """
    valid_username = "admin"
    valid_password = "password"
    
    return username == valid_username and password == valid_password

## Golf Course Class and File Handling
class golfCourse:
    def __init__(self, name, slope, rating, par):
        self.name = name
        self.slope = slope
        self.rating = rating
        self.par = par

    #save course to text file
    def save_course(self):
        with open("courses.txt", "a") as f:
            f.write(f"{self.name},{self.slope},{self.rating},{self.par}\n")

    ##load course from text file (single line)
    def load_course(self, line):
        parts = line.strip().split(',')
        self.name = parts[0]
        self.slope = int(parts[1])
        self.rating = float(parts[2])
        self.par = int(parts[3])

def load_courses():
    courses = []
    try:
        with open("courses.txt", "r") as f:
            for line in f:
                course = golfCourse("", 0, 0.0, 0)
                course.load_course(line)
                courses.append(course)
    except FileNotFoundError:
        print("No courses found.")
    return courses

## Golf Score Handling
def save_score(course_name, score):
    with open("scores.txt", "a") as f:
        f.write(f"{course_name},{score}\n")

def load_scores():
    scores = []
    try:
        with open("scores.txt", "r") as f:
            for line in f:
                parts = line.strip().split(',')
                scores.append((parts[0], int(parts[1])))
    except FileNotFoundError:
        print("No scores found.")
    return scores

## Utils
## get course info by name
def get_course_info(course_name):
    courses = load_courses()
    for course in courses:
        if course.name == course_name:
            return course
    return None

## calculate round differential
def calculate_round_differential(score, course):
    round_differential = (score - course.rating) * 113 / course.slope
    return round(round_differential, 1)

## calculate handicap index
def calculate_handicap_index(scores):
    if len (scores) < 5:
        return 0.0  # Not enough scores to calculate a handicap index
    differentials = [calculate_round_differential(score, get_course_info(course_name)) for course_name, score in scores]
    differentials.sort()
    if len(differentials) < 10:
        best_differentials = differentials[:len(differentials)] # Use the lowest 5 differentials
        return round(sum(best_differentials) / len(best_differentials) * 0.96, 1)
    else:
        return round(sum(differentials[:10]) / 10 * 0.96, 1)

## calculate course handicap
def calculate_course_handicap(handicap_index, course):
    course_handicap = handicap_index * course.slope / 113
    return round(course_handicap) 


