import os
import requests
from databricks import sql
from dotenv import load_dotenv
from setup_logging import logger

load_dotenv()

CLIENT_API_SYNC_TOKEN_URL=os.getenv('CLIENT_API_SYNC_TOKEN_URL')
CLIENT_API_SYNC_ID=os.getenv('CLIENT_API_SYNC_ID')
CLIENT_API_SYNC_SECRET=os.getenv('CLIENT_API_SYNC_SECRET')

DATABRICKS_WAREHOUSE_ID=os.getenv('DATABRICKS_WAREHOUSE_ID')
DATABRICKS_URL=os.getenv('DATABRICKS_URL')

def get_token_databricks():
    try:
        """
        OAuthトークンを取得します
        """
        token_data = {
            'grant_type': 'client_credentials',
            'scope': 'all-apis'
        }
        token_auth = (CLIENT_API_SYNC_ID, CLIENT_API_SYNC_SECRET)
        token_response = requests.post(CLIENT_API_SYNC_TOKEN_URL, data=token_data, auth=token_auth)
        token_json = token_response.json()
        OAUTH_TOKEN = token_json['access_token']
        return OAUTH_TOKEN

    except requests.exceptions.RequestException as error:
        logger.error(f"Error fetching token: {error}")
        raise error
    

def connect_to_databricks():
    token = get_token_databricks()

    try:
        with sql.connect(
            server_hostname=DATABRICKS_URL,
            http_path=f"/sql/1.0/warehouses/{DATABRICKS_WAREHOUSE_ID}",
            access_token=token
        ) as connection:
            logger.info("Kết nối thành công!")

            query = "SELECT * FROM sales_mart.sales_forecast.order_data LIMIT 10"
            cursor = connection.cursor()
            cursor.execute(query)

            rows = cursor.fetchall()
            for row in rows:
                print(row)

    except Exception as e:
        logger.error(f"Error connecting to Databricks: {e}")
        raise e


if __name__ == "__main__":
    connect_to_databricks()