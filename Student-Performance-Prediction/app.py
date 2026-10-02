from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from src.pipeline.Prediction_pipeline import CustomData, PredictPipeline

app = FastAPI()
app.mount(
    "/static",
    StaticFiles(directory='static'),
    name='static'
)

templates = Jinja2Templates(directory='templates')

@app.get("/",response_class=HTMLResponse)
async def home(request:Request):
    return templates.TemplateResponse(
        'home.html',
        {"request":request}
    )
@app.post("/",response_class=HTMLResponse)
async def predict_datapoint(
    request:Request,
    gender: str= Form(...),
    race_ethnicity: str= Form(...),
    parental_level_of_education: str = Form(...),
    lunch: str = Form(...),
    test_preparation_course: str = Form(...),
    reading_score: int = Form(...),
    writing_score: int = Form(...)
):
    data = CustomData(
        gender=gender,
        race_ethnicity=race_ethnicity,
        parental_level_of_education=parental_level_of_education,
        lunch=lunch,
        test_preparation_course=test_preparation_course,
        reading_score=reading_score,
        writing_score=writing_score
        
    )
    #convert input data to DataFrame
    final_data = data.get_data_as_data_frame()
    predict_pipeline = PredictPipeline()
    pred = predict_pipeline.predict(final_data)
    result = round(pred[0],2)
    if result >100:
        result = 100
    return templates.TemplateResponse(
        request=request,
        name="home.html",
        context={
            "request": request,
            "results": result
        }
        )
    
if __name__ == "__main__": 
    import uvicorn 
    uvicorn.run(app, host="0.0.0.0", port=8080 )