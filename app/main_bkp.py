from app.crud import create_job

@app.post("/webhook")
async def webhook(payload: MessagePayload):
    result = parse_message(payload.message)
    if result["action"] == "create_job":
        job = create_job(result["vehicle"], result["service_time"])
        return {"job_id": job.id, "status": job.status}
    return result