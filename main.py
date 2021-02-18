import argparse
import logging
import logging.config
import lib.informacast_api_calls

log = logging.getLogger(__name__)


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("--template", type=str, description="Specifies the message template to use.",
                        help="Provide the message template to be used.")

    args = parser.parse_args()
    template = args.template


if __name__ == '__main__':
    logging.config.fileConfig('logging_config.ini')
    logger = logging.getLogger(__name__)
    main()



