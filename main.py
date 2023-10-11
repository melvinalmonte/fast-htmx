from fastapi import Depends

from src import config
from src.api import router
from src.app import create_app
from src.utils.utils import default_headers_injection

app_config = config.get_config()
app = create_app()

app.include_router(router,  dependencies=[Depends(default_headers_injection)])
if __name__ == '__main__':
    import uvicorn
    uvicorn.run('main:app', host=app_config.APP_HOST, port=app_config.APP_PORT,)
