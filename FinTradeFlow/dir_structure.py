import os

def create_directory_structure(base_dir):
    directories = [
        "backend/api/routes",
        "backend/services",
        "data_pipeline/airflow/dags",
        "db",
        "frontend/src/components",
        "config/env",
    ]
    
    files = [
        "backend/api/routes/market_data.py",
        "backend/api/routes/risk_analysis.py",
        "backend/api/main.py",
        "backend/services/data_processor.py",
        "backend/services/kafka_consumer.py",
        "backend/requirements.txt",
        "backend/Dockerfile",
        "data_pipeline/kafka_producer.py",
        "data_pipeline/spark_processor.py",
        "data_pipeline/airflow/dags/stock_pipeline.py",
        "data_pipeline/Dockerfile",
        "db/clickhouse_init.sql",
        "db/Dockerfile",
        "frontend/src/components/Dashboard.js",
        "frontend/src/components/Chart.js",
        "frontend/src/App.js",
        "frontend/package.json",
        "frontend/Dockerfile",
        "config/env/.env",
        "config/settings.yaml",
        "docker-compose.yml",
        "README.md",
        "setup.sh",
    ]
    
    for directory in directories:
        os.makedirs(os.path.join(base_dir, directory), exist_ok=True)
    
    for file in files:
        file_path = os.path.join(base_dir, file)
        with open(file_path, "w") as f:
            pass  # Create empty file
    
    print(f"Directory structure created under {base_dir}")

if __name__ == "__main__":
    base_directory = "FinTradeFlow"
    create_directory_structure(base_directory)
