# -*- coding:utf-8 -*-
import shutil
import os
import sys
import subprocess
from platform import system

input_arg = output_arg = None


def main():
    args = sys.argv

    if len(args) < 3:
        print('missing 2 required positional argument:"input","output"')
        return

    #TODO:兼容相对路径问题

    global input_arg, output_arg
    input_arg, output_arg = args[1], args[2]
    if not os.path.isdir(output_arg) or not os.path.exists(output_arg):
        print('output must be a directory,and be sure it exists')
        return

    inputs = []
    if not os.path.exists(input_arg):
        print('input must exist')
        return
    elif os.path.isfile(input_arg):
        inputs.append(input_arg)
    elif os.path.isdir(input_arg):
        for root, _, files in os.walk(input_arg):
            for file in files:
                if file.endswith(".md"):
                    inputs.append(os.path.join(root, file))
    else:
        print('input must be a file or directory')
        return

    __run_command(
        'sudo chmod -R 777 static {} {}'.format(input_arg, output_arg))
    __build(inputs, output_arg)


def __build(inputs, output):
    if not os.path.exists('node_modules'):
        __run_command('npm install')

    for md in inputs:
        if os.path.getsize(md) <= 0:
            continue

        shutil.copy(md, "static")
        __run_command('npm run build')
        os.rename(os.path.join('dist', 'index.html'), os.path.join(
            'dist', '{}.html'.format(os.path.splitext(os.path.basename(md))[0])))

        des_path = os.path.dirname(md).replace(input_arg, output_arg)
        __run_command('mkdir -p {}'.format(des_path))
        shutil.move('dist', des_path)
        # TODO:1.移除dist目录 2.同名目录内容追加 3.修改Readme.md文档 4. Docker封装
        # docker run -it --rm -e input -e output mdbuilder:1.0


def __run_command(cmd):
    if not cmd:
        return

    subprocess.run(cmd.split(' '))


if __name__ == "__main__":
    if system()!='Linux':
        print('only linux is supported curretly')
    else:
        main()
