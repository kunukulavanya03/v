from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from database import engine
from models import Base
from routes import router

load_dotenv()
Base.metadata.create_all(bind=engine)

app = FastAPI(title="the_v_project_is_a_backend_api_designed_to_handle_data_processing_and_storage_for_a_react-based_frontend_application._the_api_will_provide_a_range_of_endpoints_for_creating,_reading,_updating,_and_deleting_data._the_project_will_utilize_fastapi_as_the_backend_framework_and_sqlalchemy_for_database_operations. API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router, prefix="/api")

@app.get("/")
def read_root():
    return {"message": "Welcome to the_v_project_is_a_backend_api_designed_to_handle_data_processing_and_storage_for_a_react-based_frontend_application._the_api_will_provide_a_range_of_endpoints_for_creating,_reading,_updating,_and_deleting_data._the_project_will_utilize_fastapi_as_the_backend_framework_and_sqlalchemy_for_database_operations. API", "status": "running"}

@app.get("/health")
def health_check():
    return {"status": "healthy", "service": "the_v_project_is_a_backend_api_designed_to_handle_data_processing_and_storage_for_a_react-based_frontend_application._the_api_will_provide_a_range_of_endpoints_for_creating,_reading,_updating,_and_deleting_data._the_project_will_utilize_fastapi_as_the_backend_framework_and_sqlalchemy_for_database_operations."}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)