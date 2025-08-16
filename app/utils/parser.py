import re
from datetime import datetime, timedelta

def parse_message(msg: str):
    if "need service" in msg.lower():
        vehicle_match = re.search(r"service for (\w+)", msg.lower())
        time_match = re.search(r"tomorrow (\d{1,2}am|\d{1,2}pm)", msg.lower())
        vehicle = vehicle_match.group(1) if vehicle_match else "unknown"
        time_str = time_match.group(1) if time_match else "10am"
        hour = int(re.sub(r"[^\d]", "", time_str))
        if "pm" in time_str and hour < 12:
            hour += 12
        service_time = datetime.now() + timedelta(days=1)
        service_time = service_time.replace(hour=hour, minute=0)
        return {
            "action": "create_job",
            "vehicle": vehicle,
            "service_time": service_time.strftime("%Y-%m-%d %H:%M")
        }
    return {"action": "unknown"}