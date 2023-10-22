"""Main fastapi app."""
from fastapi import FastAPI, Response, Request
from pydantic import BaseModel

app = FastAPI()


@app.get("/hello")
async def hello_get():
    """Returns text response."""
    return Response("HSE One Love!", status_code=200, media_type="text/plain")


class SetInDict(BaseModel):
    """Class for json parsing."""

    key: str
    value: str


values = {}


@app.post("/set")
async def set_value(request: Request):
    """Set value in values."""
    if request.headers.get("Content-Type", "") != "application/json":
        return Response(status_code=415)
    try:
        value = await request.json()
        value_to_add = SetInDict.model_validate(value)
    except ValueError:
        return Response(status_code=415)
    values[value_to_add.key] = value_to_add.value
    return Response(status_code=200)


class Divide(BaseModel):
    """Class for validate request."""

    dividend: float
    divider: float

    def __call__(self, *args, **kwargs):
        return str(self.dividend / self.divider)


@app.post("/divide")
async def divide_post(request: Request):
    """Devide integers"""
    if request.headers.get("Content-Type", "") != "application/json":
        return Response(status_code=415)
    try:
        value = await request.json()
        divide_obj = Divide.model_validate(value)
    except ValueError:
        return Response(status_code=415)
    try:
        result = divide_obj()
    except ZeroDivisionError:
        return Response(status_code=400)

    return Response(content=result, media_type="text/plain", status_code=200)


@app.get("/get/{key}")
async def get_value(key):
    """returns value from values"""
    if key in values:
        value = SetInDict(key=key, value=values[key])
        return Response(
            content=value.model_dump_json(),
            media_type="application/json",
            status_code=200,
        )
    return Response(status_code=404)


@app.exception_handler(404)
async def not_found_exception_handler():
    """Replaces 404 status code to 405"""
    return Response(status_code=405)
