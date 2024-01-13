import argparse


def dprint(string):
    print(f"DEBUG -> {string}")


def print_ln(length=60):
    print("─" * length)


def print_parameter_usage(args):
    if args.clusters is not None:
        dprint(f"Number of clusters (-c): {args.clusters}")
    if args.items is not None:
        dprint(f"Number of items (-i): {args.items}")
    if args.seed is not None:
        dprint(f"Seed given (-s): {args.seed}")
    if args.round is not None:
        dprint(f"Round precision (-r): {args.round}")
    if args.file is not None:
        dprint(f"Data file (-f): {args.file}")
    print_ln()
