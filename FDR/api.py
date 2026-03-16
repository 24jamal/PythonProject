from fastapi import FastAPI
from producer_service import publish_fdr_transactions

app = FastAPI()

@app.post("/publish-merchant-fdr")
def publish_fdr():

    publish_fdr_transactions()

    return {
        "message": "Merchant FDR data pushed to queue"
    }