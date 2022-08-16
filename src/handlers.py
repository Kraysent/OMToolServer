from aiohttp import web

async def ping(request: web.Request):
    return web.Response(text="pong")

async def get_model(request: web.Request):
    pass