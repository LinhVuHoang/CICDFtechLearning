from src.components.Data_ingestion import DataIngestion
from src.components.Data_transformation import DataTransformation
from src.components.Model_trainer import ModelTrainer


obj = DataIngestion()
train_path, test_path = obj.initiate_data_ingestion()

data_transformation = DataTransformation()

train_arr, test_arr, processor_path = data_transformation.initiate_data_transformation(train_path,test_path)

model_trainer = ModelTrainer()

print(model_trainer.initiate_model_trainer(train_arr,test_arr))
