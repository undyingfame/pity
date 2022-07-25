import uvicorn

from config import Config

# import aiomysql


if __name__ == "__main__":
    # uvicorn.run(pity, host="0.0.0.0", port=Config.SERVER_PORT, reload=False)
    uvicorn.run("main:pity", host="0.0.0.0", port=Config.SERVER_PORT, reload=True, forwarded_allow_ips="*")
