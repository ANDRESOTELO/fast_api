from fastapi import FastAPI


app = FastAPI()


@app.get('/api')
def home():
    """First endpoint"""
    return {'Status': 'OK',
            'message': 'API home',
            'status': 200}