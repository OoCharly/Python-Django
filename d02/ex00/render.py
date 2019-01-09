import sys, re, os


def parse_settings():
    data = {}
    with open("settings.py", "r") as settings:
        for line in settings:
            tmp = line.split('=')
            data.update({tmp[0].strip(): tmp[1].strip('" \n')})
        settings.close()
    return data


def render(filename):
    if not re.match("\w+.template", filename):
        raise  ('wrong extension')
    with open(filename, "r") as template:
        content = template.read()
        template.close()

    with open("cv.html", "w") as cv:
        cv.write(content.format_map(parse_settings()))
        cv.close()


if __name__ == "__main__":
    if len(sys.argv) == 2:
        try:
            render(sys.argv[1])
        except KeyError as e:
            print("missing data in settings.py: ")
            print(e)
        except FileNotFoundError as e:
            print(e)
        except PermissionError as e:
            print(e)
        except Exception as e:
            print(e)
    else:
        print("usage: render.py <filename.template>")
