from jinja2 import Environment, FileSystemLoader, select_autoescape
from pandas import read_csv

# Filenames
courseTemplateFilename = ""
indexTemplateFilename = ""
dataFilename = "data.csv"
indexFilename = "index.html"

# Import data
data = read_csv(dataFilename, delimiter=",", header=0, index_col="id")

# Jinja Setup
env = Environment(loader=FileSystemLoader, autoescape=select_autoescape(["html"]))
courseTemplate = env.get_template(courseTemplateFilename)
indexTemplateFilename = env.get_template(indexTemplateFilename)

# Classes for instructor and course

class Course():
    pass

# Start working



