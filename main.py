from jinja2 import Environment, FileSystemLoader, select_autoescape
import pandas as pd
import numpy as np
import os

# Import data

def preprocessing(csv_file):
    df = pd.read_csv(csv_file, delimiter=",", header=0)  #reads the .csv file and uses 1st row as header
    df.replace(np.nan, "", regex=True, inplace=True) # replace all null values with blank
    df = df.to_dict('records')  #creates a dictionary
    return df

# Chemistry to be added when available
deptlist = ['mth', 'phy', 'bio', 'ecs', 'hss', 'chm']

for dept in deptlist:

    # Filenames
    courseTemplateFilename = "templates/course_template.html"
    deptTemplateFilename = "templates/dept_template.html"
    dataFilename = f"data/{dept}_courses.csv"
    instructorDataFilename = f"data/{dept}_instructors.csv"
    # addResourcesFilename = "addresources.csv"
    deptFilename = f"html/{dept}.html"

    courses = preprocessing(dataFilename)
    instData = preprocessing(instructorDataFilename)

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
    deptTemplate = env.get_template(deptTemplateFilename)

    # Start working
    for course in courses:
        # print("course:", course)
        # print()
        course["coursehtml"] = courseTemplate.render(course=course)
        # print("courseinfo:", course["courseinfo"])

    output = deptTemplate.render(courses=courses, dept=dept.upper())

    with open(deptFilename, "w") as outfile:
        outfile.write(output)

    print(f"Task Completed: {dept}.html")
