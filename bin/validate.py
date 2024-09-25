from os import listdir, getcwd, path, environ
import yaml
import re


def try_get_value(chart: dict, key: str) -> str | dict:
    try:
        value = chart[key]
    except KeyError:
        return ""
    return value


def fail(value) -> bool:
    print(f">    Error: Chart value '{value}' is incorrect or not set!")
    return True


def validate_chart_file(chart_file) -> None:
    failed = False
    chart = yaml.safe_load(chart_file)
    print(f"> Validating chart {chart['name']}...")

    home = try_get_value(chart, "home")
    description = try_get_value(chart, "description")
    version = try_get_value(chart, "version")

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

    if not re.match("^\d{1,3}.\d{1,3}.\d{1,3}$", version):
        failed = fail("version")

    if failed:
        print(
            f">\n>  One or more checks for chart '{chart['name']}' have failed. Exiting 1."
        )
        exit(1)


def main() -> None:
    try:
        charts_dir = environ["CHARTS_DIR"]
    except KeyError:
        print("CHARTS_DIR not defined! Exiting 1.")
        exit(1)

    cwd = getcwd()
    charts = listdir(path.join(cwd, charts_dir))

    if len(charts) < 1:
        print(f"No directories found in {charts_dir}. Exiting.")
        exit(0)

    for chart in charts:
        try:
            with open(path.join(cwd, charts_dir, chart, "Chart.yaml")) as f:
                chart_file = f.read()
                validate_chart_file(chart_file)
        except NotADirectoryError:
            continue

    print(">\n> All charts successfully validated")


if __name__ == "__main__":
    main()
