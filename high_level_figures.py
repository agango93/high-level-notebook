import argparse as ap
import assessmenttemplates.intranode as intranode
import assessmenttemplates.summary as summary


def _main():
    parser = ap.ArgumentParser(
        prog="high_level-graphs.py",
        description="Tools to generate plots for the high-level assessment.",
        epilog="Unless an output flag is specified, a requested output will be echoed to the standard console output."
    )

    parser.add_argument("--version",
                        action="version",
                        version="%(prog)s 1.1",
                        help="Show program version number and exit.")

    sub_parsers = parser.add_subparsers(dest="metric", required=True, help="Metric for which plots are to be "
                                                                           "generated.")
    # Add plots per mode
    intranode.intranode_add_args(sub_parsers)
    summary.summary_add_args(sub_parsers)

    args = parser.parse_args()

    if args.metric == "intranode":
        intranode.intranode_main(args)
    elif args.metric == "summary":
        summary.summary_main(args)


if __name__ == "__main__":
    _main()
