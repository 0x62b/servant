from datetime import datetime, timedelta, timezone
from flask import jsonify

def sleep(data, app):
    user_id = data.get('user_id')

    if user_id != "U092839T3A7":
        res = {
            "response_type": "ephemeral",
            "text": "no perms"
        }

        return jsonify(res)

    channel_id = data.get('channel_id')
    
    tomorrow = (datetime.now(timezone.utc) + timedelta(days=1)).date()
    target = datetime(tomorrow.year, tomorrow.month, tomorrow.day, 6, 45, tzinfo=timezone.utc)
    
    app.client.chat_scheduleMessage(
        channel=channel_id,
        post_at=int(target.timestamp()),
        text=f"<@U092839T3A7> wakey wakey"
    )
        
    res = {
        "response_type": "ephemeral",
        "text": f"you shall wake at 6:45am"
    }
    return jsonify(res)
