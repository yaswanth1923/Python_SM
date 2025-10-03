import boto3
import os

def upload_file_to_s3(
    access_key,
    secret_key,
    region,
    bucket,
    folder,
    local_file_path,
    s3_file_name=None
):
    """
    Upload ANY local file to S3.
    """
    if not s3_file_name:
        s3_file_name = os.path.basename(local_file_path)

    # Final key path in S3
    file_key = f"{folder}/{s3_file_name}" if folder else s3_file_name

    # Initialize S3 client
    session = boto3.Session(
        aws_access_key_id=access_key,
        aws_secret_access_key=secret_key,
        region_name=region
    )
    s3 = session.client("s3")

    # Upload
    s3.upload_file(local_file_path, bucket, file_key)

    print(f"✅ Uploaded {local_file_path} → s3://{bucket}/{file_key}")
    return f"s3://{bucket}/{file_key}"
