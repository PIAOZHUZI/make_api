# This is a sample Python script.
import argparse
import os
from jinja2 import Template, environment, FileSystemLoader, Environment
import yaml
import sys

parser = argparse.ArgumentParser()
parser.add_argument('-path', help=' : Please set the folder path')
# parser.add_argument('-option', help=' : train or prediction', default='train')
# parser.add_argument('-stt_date', help=' : Please set the start date of prediction(default)', default='2021-11-02')
# parser.add_argument('-end_date', help=' : Please set the last date of prediction(default)', default='2021-12-02')

args = parser.parse_args()


def test(args):
    try:
        os.makedirs(args.path + "/routes")
    except FileExistsError:
        # directory already exists
        pass
    with open(args.path + '/__init__.py', 'w') as f:
        pass
    with open(args.path + '/routes/__init__.py', 'w') as f:
        pass
    env = Environment(loader=FileSystemLoader("templates"))
    jinja_template = env.get_template('make.j2')
    with open('settings/api.yaml') as f:
        y = yaml.safe_load(f)
    output = jinja_template.render(yaml=y)
    with open(args.path + '/main.py', 'w') as f:
        f.write(output)
    with open('settings/router.yaml') as f:
        y2 = yaml.safe_load(f)
    env = Environment(loader=FileSystemLoader("templates"))
    jinja_template2 = env.get_template('make_route.j2')
    output2 = jinja_template2.render(yaml=y2)
    with open(args.path + '/routes/route1.py', 'w') as f:
        f.write(output2)
    if os.path.isfile(args.path + '/db.py'):
        pass
    else:
        jinja_template3 = env.get_template('make_db.j2')
        with open('settings/db.yaml', encoding='UTF-8') as f:
            y = yaml.safe_load(f)
        output3 = jinja_template3.render(yaml=y)
        with open(args.path + '/db.py', 'w', encoding='UTF-8') as f:
            f.write(output3)

    if os.path.isfile(args.path + '/model.py'):
        pass
    else:
        jinja_template4 = env.get_template('make_model.j2')
        with open('settings/model.yaml', encoding='UTF-8') as f:
            y = yaml.safe_load(f)
        output4 = jinja_template4.render(yaml=y)
        with open(args.path + '/model.py', 'w', encoding='UTF-8') as f:
            f.write(output4)


def make_folder(args):
    try:
        os.makedirs(args.path)
    except OSError:
        if not os.path.isdir(args.path):
            raise


def main(argv, args):
    print('\n')
    # print(f'argv : ', argv)
    # print(f'args : ', args)

    print(f'args.path : ', args.path)
    make_folder(args)
    test(args)
    print('\n')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    argv = sys.argv
    main(argv, args)
