from datetime import datetime, timezone

target = datetime(2029, 5, 25, 0, 0, 0)
now = datetime.now(timezone.utc)

diff = target - now

days = diff.days
hours, rem = divmod(diff.seconds, 3600)
minutes, seconds = divmod(rem, 60)

output = f"""
⏳ Time Remaining to Graduation:
📅 {days} days
⏰ {hours} hours
🕒 {minutes} minutes
⏱ {seconds} seconds
"""

with open("countdown.txt", "w", encoding="utf-8") as f:
    f.write(output.strip())
