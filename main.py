from fastapi import FastAPI


app = FastAPI()



@app.get("/")
async def greet():
    return {"message": "Hellow guys"
                
            }

@app.get("/about")
async def about_me():
    return {
        "name": "Feliche",
        "age": 20,
        "Hobby": "Sports",
        "Team": "Real Madrid",
        "contacts": ["feliche@gmail.com", "0712748364"]
    }








