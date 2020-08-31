from jinja2 import Environment, FileSystemLoader, select_autoescape
from pandas import read_csv
import os

# Filenames
courseTemplateFilename = "templates/course_template.html"
indexTemplateFilename = "templates/index_template.html"
dataFilename = "data/data.csv"
instructorDataFilename = "data/instructors.csv"
# addResourcesFilename = "addresources.csv"
indexFilename = "index.html"

# Import data
courses = read_csv(dataFilename, delimiter=",", header=0)
courses = courses.to_dict("records")
instData = read_csv(instructorDataFilename, delimiter=",", header=0)
instData = instData.to_dict("records")

# print("courses:", courses)
# print()
# print("instData:", instData)
# print()
# Merge the datasets
for course in courses:
    instructors = []
    for prof in instData:
        if prof["courseid"] == course["id"]:
            instructors.append(prof)
    course["instructors"] = instructors

# Jinja Setup
env = Environment(loader=FileSystemLoader(os.path.abspath(".")), autoescape=select_autoescape(["html"]))
courseTemplate = env.get_template(courseTemplateFilename)
indexTemplate = env.get_template(indexTemplateFilename)

# Start working
for course in courses:
    # print("course:", course)
    # print()
    course["coursehtml"] = courseTemplate.render(course=course)
    # print("courseinfo:", course["courseinfo"])

output = indexTemplate.render(courses=courses)

with open(indexFilename, "w") as outfile:
    outfile.write(output)

print("Tasked Completed Successfully!")
