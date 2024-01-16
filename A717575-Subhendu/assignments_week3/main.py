# main app for sample fastapi application

from fastapi import FastAPI, Depends
from models import Items
from database import init_db, get_rows
from loadenv import init_env
from logger import init_logger
from routers import router


# create fastapi app
app = FastAPI(description="This is a sample FastAPI application",
              dependencies=[Depends(init_env), Depends(init_logger), Depends(init_db)])

# register routers
app.include_router(router)


@app.get("/", response_model=list[Items])
async def home():
    """home end point 

    Returns:
        list[Items]: list of items
    """
    data = get_rows("items")
    if not data:
        return []
    return data


if __name__  == "__main__":
    import uvicorn
    uvicorn.run("__main__:app", port=3000, reload=True)
