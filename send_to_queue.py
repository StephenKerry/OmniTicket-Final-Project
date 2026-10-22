import logging
import sys
from celery import Celery

logging.basicConfig(
    filename="queue_log.txt",
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
)

app = Celery(broker="redis://localhost:6379/0")

message = sys.argv[1] if len(sys.argv) > 1 else "test message"

result = app.send_task("queuedemo.tasks.send_queue_email", args=[message])

logging.info("Sent message %r to Redis, task id %s", message, result.id)
print(f"Sent {message!r} to the queue, task id {result.id}")