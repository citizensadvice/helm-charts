from operator import truediv
from os import listdir, getcwd, path
import yaml

def try_get_value(chart: dict, key: str) -> str:
    try:
        value = chart[key]
    except KeyError:
        return ""
    return value

def fail(value) -> bool:
    print(f">    Error: Chart value '{value}' is incorrect or not set!")
    return True

def validate_chart_file(chart_file) -> bool:
    failed = False
    chart = yaml.safe_load(chart_file)
    print(f"> Validating chart {chart['name']}...")

    home = try_get_value(chart, "home")
    description = try_get_value(chart, "description")
    version = try_get_value(chart, "version")
    icon = try_get_value(chart, "icon")

    maintainers = try_get_value(chart, "maintainers")
    try:
        maintainers = maintainers[0]
    except IndexError:
        maintainers = {}
    maintainer_name = try_get_value(maintainers, "name")
    maintainer_email = try_get_value(maintainers, "email")

    if home != "https://github.com/citizensadvice/helm-charts":
        failed = fail("home")
    
    if description == "":
        failed = fail("decription")

    if maintainer_name != "CA Devops":
        failed = fail("maintainer name")
    
    if maintainer_email != "ca-devops@citizensadvice.org.uk":
        failed = fail("maintainer email")

    if version == "":
        failed = fail("version")

    if icon == "":
        failed = fail("icon")

    if failed:
        print(f">\n>  One or more checks for chart '{chart['name']}' have failed. Exiting 1.")
        exit(1)

def main() -> None:
    charts =  listdir("src")
    cwd = getcwd()
    for chart in charts:
        with open(path.join(cwd,"src",chart,"Chart.yaml")) as f:
            chart_file = f.read()
        validate_chart_file(chart_file)
            
if __name__ == "__main__":
    main()