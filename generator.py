import yaml
import os
from jinja2 import Environment, FileSystemLoader


with open("data/portfolio.yaml", "r") as file:
    portfolio_data = yaml.safe_load(file)

env = Environment(loader=FileSystemLoader("templates"))
template = env.get_template("index.html")

output_html = template.render(portfolio_data)

os.makedirs("output", exist_ok=True)

with open("output/index.html", "w") as file:
    file.write(output_html)
