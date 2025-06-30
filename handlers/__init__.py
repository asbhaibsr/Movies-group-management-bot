from .start import start_cmd
from .info import info_handler
from .trivia import trivia_handler
from .settings import settings_handler
from .admin import admin_handler

def register_handlers(app):
    app.add_handler(start_cmd)
    app.add_handler(info_handler)
    app.add_handler(trivia_handler)
    app.add_handler(settings_handler)
    app.add_handler(admin_handler)
