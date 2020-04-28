# ref: https://www.youtube.com/watch?v=U6BzW48-D9

# python3 -m pip install fastapi[all]
# python -m uvicorn

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class LinuxTips(BaseModel):
    canal: str
    msg: str
    dia: int


@app.get("/", response_model=LinuxTips)
async def linuxtips():
    return LinuxTips(
        canal="LinuxTips",
        msg="VAIIIIII",
        dia=25
    )