#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import argparse
import sys
import glob
from distutils.dir_util import copy_tree
from auto_ovpn_profiles import parse_options_from_yaml, write_complete_config, get_all_clients_by_keyfiles


def parse_cl_args(arguments):
    parser = argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter)

    parser.add_argument(
        "-e", "--example",
        action='store_true',
        help="Print out an example of a configuration yaml file."
    )

    parser.add_argument(
        "-F", "--file",
        type=str,
        action='append',
        help="Path to a yaml file containing the configuration values."
    )

    parser.add_argument(
        "-o", "--output-dir",
        type=str,
        help="(optional) Path to an output directory where all the vpn profiles should be placed."
    )

    args = parser.parse_args(arguments)
    # print(args)
    return args, parser


if __name__ == "__main__":
    args, parser = parse_cl_args(sys.argv[1:])

    # If the `example` flag was passed, print out the example yaml and quit
    if args.example:
        with open("vpn_example.yml", 'r') as myfile:
            example_yaml = myfile.read()
            print(example_yaml)
        sys.exit(0)

    # If no files were given, display the help text and quit
    if args.file is None:
        parser.print_help()
        sys.exit(0)

    # If we make it to this point, at least a file was given.
    client_dirs = []
    for cfg in [parse_options_from_yaml(x) for x in args.file]:
        write_complete_config(cfg)
        existing_clients = get_all_clients_by_keyfiles(cfg['KEY_DIR'])
        client_dirs.append(glob.glob("{}/clients/".format(cfg['OUTPUT_DIR']))[0])

    if args.output_dir is not None:
        for a_dir in client_dirs:
            copy_tree(a_dir, args.output_dir)

    print(args)