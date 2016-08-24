from channels.routing import route

channel_routing = [
    route("http.request", "rogue.consumers.http_consumer"),
]
