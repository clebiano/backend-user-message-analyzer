from app.application import Application
from app.router import router

app = Application(router=router)
