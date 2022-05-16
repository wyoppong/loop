import uvicorn
from loop.config import config

if __name__ == "__main__":
    uvicorn.run(
        app="loop.bootstrap.startup:app",
        host=config.config.APP_HOST,
        port=config.config.APP_PORT,
        reload=True,
        workers=1,
    )
