import models
from fastapi import FastAPI, Request, Depends
from starlette.responses import RedirectResponse
from api import balances, stocks, orders

app = FastAPI()
app.include_router(balances.router)
app.include_router(stocks.router)
app.include_router(orders.router)


@app.get("/")
async def index():
    return RedirectResponse(url="/docs")
