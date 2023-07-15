# Installation Django Channels

i) pip install channels

ii) Add 'channels' in INSTALLED_APPS (সবার উপরে লিখতে হবে।)

    INSTALLED_APPS = [

        'channels',

    ]

iii) setting.py file এ WSGI_APPLICATION = 'Core.wsgi.application' এর পরিবর্তে ,

    ASGI_APPLICATION = 'Core.asgi.application'

iv) Project Folder এর asgi.py file এর ভেতর Router defile করতে হবে,

    from channels.routing import ProtocolTypeRouter, URLRouter
    import app.routing

    application = ProtocolTypeRouter({
        'http':get_asgi_application(),

        'websocket': URLRouter(
            app.routing.websocket_urlpatterns
        )
    })


v) Testing, 

    http://127.0.0.1:8000/ এখানে http:// এর পরিবর্তে ws:// এবং wss:// হবে,

    ws://127.0.0.1:8000/ws/sc/
