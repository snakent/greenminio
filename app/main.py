from fastapi import FastAPI
from minio import Minio

app = FastAPI(title="GreenAPI")


@app.get("/get_image")
def read_root():

    # test
    client = Minio(
        "minio:9000",
        access_key="Q3AM3UQ867SPQQA43P2F",
        secret_key="zuf+tfteSlswRu7BJ86wekitnifILbZam1KYY3TG",
        secure=False

    )

    found = client.bucket_exists("greenstorage")

    return {"result": found}
