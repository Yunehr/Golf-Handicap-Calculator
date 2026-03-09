# Golf Handicap Calculator - Functions

def check_credentials(username, password):
    valid_username = "admin"
    valid_password = "password"
    return username == valid_username and password == valid_password


class golfCourse:
    def __init__(self, name, slope, rating, par):
        self.name = name
        self.slope = slope
        self.rating = rating
        self.par = par

    def save_course(self):
        with open("courses.txt", "a") as f:
            f.write(f"{self.name},{self.slope},{self.rating},{self.par}\n")

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

def delete_courses(self):
    with open("courses.txt", "w") as f:
        f.write("")
    


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

def delete_scores(self):
    with open("scores.txt", "w") as f:
        f.write("")
    


def calculate_round_differential(score, course):
    rd = (score - course.rating) * 113 / course.slope
    return round(rd, 1)


def calculate_handicap_index(scores):
    if len(scores) < 5:
        return 0.0

    diffs = [calculate_round_differential(score, get_course_info(name)) for name, score in scores]
    diffs.sort()

    if len(diffs) < 10:
        best = diffs[:len(diffs)]
        return round(sum(best) / len(best) * 0.96, 1)
    else:
        return round(sum(diffs[:10]) / 10 * 0.96, 1)


def calculate_course_handicap(handicap_index, course):
    return round(handicap_index * course.slope / 113)


def get_course_info(course_name):
    for course in load_courses():
        if course.name == course_name:
            return course
    return None


def get_handicap_index():
    return calculate_handicap_index(load_scores())


def display_courses(self):
    courses_screen = self.root.ids.screen_manager.get_screen("courses_screen")
    courses = load_courses()
    handicap_index = get_handicap_index()

    course_list = "\n".join([
        f"{c.name} - Slope: {c.slope}, Rating: {c.rating}, Par: {c.par}, Course Handicap: {calculate_course_handicap(handicap_index, c)}"
        for c in courses
    ])

    courses_screen.ids.course_list.text = course_list if course_list else "No courses available"


def display_scores(self):
    scorecard_screen = self.root.ids.screen_manager.get_screen("scorecard_screen")
    scores = load_scores()

    score_list = "\n".join([f"{name} - Score: {score}" for name, score in scores])
    scorecard_screen.ids.score_list.text = score_list if score_list else "No scores available"


def validate_score_input(course_name, score_text):
    if course_name == "--No Course Selected--":
        return "Please select a valid course"

    if not score_text or not score_text.isdigit():
        return "Please enter a valid score"

    return None


def validate_course_input(course_name, slope_text, rating_text, par_text):
    if not course_name:
        return "Please enter a course name"

    if not slope_text or not slope_text.isdigit():
        return "Please enter a valid slope rating"

    if not rating_text:
        return "Please enter a valid course rating"

    if not par_text or not par_text.isdigit():
        return "Please enter a valid par"

    return None
