# coding: utf-8
from __future__ import absolute_import
from __future__ import unicode_literals
from __future__ import print_function
import sys
import os
import subprocess


def print_help():
    print("USAGE : [command] [opts]")


def main(args):
    if len(args) == 0 or args[0] == help:
        print_help()

    output = ''
    if args[0] == 'runtime':
        if args[1] == 'header':
            with open('/usr/include/halide/HalideRuntime.h', 'rb') as fp:
                sys.stdout.write(fp.read())
        else:
            output = subprocess.check_output(
                ['/opt/build/halide/bin/halide_library_runtime.generator_binary',
                 '-r', 'halide_runtime', '-o', '/tmp/', 'target={}'.format(args[1]),
                 '-e', 'static_library'])
            with open('/tmp/halide_runtime.a', 'rb') as fp:
                sys.stdout.write(fp.read())
    else:
        if os.path.isabs(args[1]):
            raise Exception("source file path must be relative to /work")

        basename = os.path.splitext(args[1])[0]
        dirname = os.path.dirname(basename)
        if dirname:
            os.makedirs(dirname)
            diropts = ['-o', dirname]
        else:
            diropts = ['-o', '.']

        cxx_flags = [x for x in os.environ.get('CXX_FLAGS', '').split(' ') if x]
        output = subprocess.check_output(['clang++', ] + cxx_flags + [
            '-fno-rtti', '-lHalide', '-ldl',
            '-o', '/build/a.out', os.path.join('/work', args[1])])
        output += subprocess.check_output([
            '/build/a.out', '-e', args[0], '-n', os.path.basename(basename), ] + diropts + args[2:])

        with open('{}.{}'.format(os.path.join('/build', basename), args[0]), 'rb') as fp:
            sys.stdout.write(fp.read())
    output = output.strip()
    if output:
        sys.stderr.write(output)
        sys.stderr.write('\n')
        sys.stderr.flush()


def __entry_point():
    try:
        main(sys.argv[1:])
    except subprocess.CalledProcessError as exc:
        print("Status : FAIL", exc.returncode, exc.output, file=sys.stderr)

if __name__ == '__main__':
    __entry_point()
