from datetime import datetime, timedelta, timezone
from zoneinfo import ZoneInfo
from flask import jsonify

def sleep(data, app):
    user_id = data.get('user_id')

    if user_id != "U092839T3A7":
        return jsonify({"response_type": "ephemeral", "text": "no perms"})

    channel_id = data.get('channel_id')

    tz = ZoneInfo("Australia/Sydney")

    local_now = datetime.now(tz)
    tomorrow = (local_now + timedelta(days=1)).date()
    target_local = datetime(tomorrow.year, tomorrow.month, tomorrow.day, 6, 45, tzinfo=tz)

    post_at = int(target_local.astimezone(timezone.utc).timestamp())

    app.client.chat_scheduleMessage(
        channel=channel_id,
        post_at=post_at,
        text=f"<@U092839T3A7> wakey wakey"
    )

    app.client.chat_postMessage(
        channel=channel_id,
        text=f"<@U092839T3A7> finally slept. took him long enough"
    )

    return jsonify({"response_type": "ephemeral", "text": "you shall wake at 6:45am"})
