import os
import boto3
from botocore.exceptions import NoCredentialsError, PartialCredentialsError
from dotenv import load_dotenv
from setup_logging import logger

load_dotenv()

S3_ACCESS_KEY = os.getenv('S3_ACCESS_KEY')
S3_SECRET_KEY = os.getenv('S3_SECRET_KEY')
S3_REGION = os.getenv('S3_REGION')


def connect_to_s3():
    try:
        s3_client = boto3.client(
            service_name='s3',
            aws_access_key_id=S3_ACCESS_KEY,
            aws_secret_access_key=S3_SECRET_KEY
        )
        s3_client.list_buckets()

        logger.info("Kết nối đến S3 thành công!")
        return s3_client
    except NoCredentialsError:
        logger.error("Lỗi xác thực AWS: Không tìm thấy thông tin xác thực.")
        return None
    except PartialCredentialsError:
        logger.error("Lỗi xác thực AWS: Thông tin xác thực không đầy đủ.")
        return None
    except Exception as e:
        logger.error(f"Có lỗi xảy ra khi kết nối đến S3: {e}")
        return None

if __name__ == "__main__":
    connect_to_s3()
