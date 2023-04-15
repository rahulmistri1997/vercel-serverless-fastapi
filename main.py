from fastapi import FastAPI, Request
import os
import json
import httpx

app = FastAPI()

def handle_alerts(data: list):
    # print(data)
    from util import parse_value_string
    # Return the JSON data
    # return (
    #     [parse_value_string(x["valueString"]) for x in data["alerts"] if x["status"] == "firing"][0]
    # )

    output = []

    for x in data["alerts"]:
        if x["status"] == "firing":
            print(x["labels"]["alertname"])
            output.append(
                {
                    "alertname": x["labels"]["alertname"],
                    "value": parse_value_string(x["valueString"]),
                }
            )

    return output

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}

@app.post("/webhook")
async def webhook(request: Request):
    # Check if the request is a JSON request
    if request.headers["Content-Type"] == "application/json":
        # Get the JSON data
        data = await request.json()
        # Print the JSON data
        # print(data)
        from util import parse_value_string
        # Return the JSON data
        
        response = httpx.post(
            os.getenv("WEBHOOK_SEND_URL"),
            data=json.dumps(data),
            headers={"Content-Type": "application/json"},
        )
        
        return {
            "message" : "Success",
            "data" : handle_alerts(data)
        }
