from aiohttp import web

PORT = 3456


async def ping(request):
    return web.Response(text="pong")


app = web.Application()
app.add_routes([web.get("/ping", ping)])

web.run_app(app, port=PORT)
