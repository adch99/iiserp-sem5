from jinja2 import Environment, FileSystemLoader, select_autoescape
from pandas import read_csv
import os

# Filenames
courseTemplateFilename = "course_template.html"
indexTemplateFilename = "index_template.html"
dataFilename = "data.csv"
instructorDataFilename = "instructors.csv"
# addResourcesFilename = "addresources.csv"
indexFilename = "index.html"

# Import data
courses = read_csv(dataFilename, delimiter=",", header=0, index_col="id")
courses = courses.to_dict("records")
instData = read_csv(instructorDataFilename, delimiter=",", header=0, index_col="iiserid")
instData = instData.to_dict("records")

# Merge the datasets
for course in courses:
    instructors = []
    for prof in instData:
        if prof["courseid"] == course["id"]:
            instructor.append(prof)
    course["instructors"] = instructors

# Jinja Setup
env = Environment(loader=FileSystemLoader(os.path.abspath(".")), autoescape=select_autoescape(["html"]))
courseTemplate = env.get_template(courseTemplateFilename)
indexTemplate = env.get_template(indexTemplateFilename)

# Start working
for course in courses:
    course["courseinfo"] = courseTemplate.render(course)

output = indexTemplate.render(courses)

with open(indexFilename, "w") as outfile:
    outfile.write(output)

print("Tasked Completed Successfully!")
