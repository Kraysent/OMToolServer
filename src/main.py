import argparse
import logging
from aiohttp import web
from handlers import ping, get_model


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--port")

    return parser.parse_args()


def main():
    logging.basicConfig(level=logging.DEBUG)
    args = parse_args()

    app = web.Application()
    app.add_routes([web.get("/ping", ping), web.post("/v1/model", get_model)])

    web.run_app(app, port=args.port)


if __name__ == "__main__":
    main()
