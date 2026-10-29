import hashlib
import hmac

import qrcode

SECRET = b"demo-secret"
used = set()


def make_token(ticket_id):
    signature = hmac.new(SECRET, str(ticket_id).encode(), hashlib.sha256).hexdigest()[:16]
    return f"{ticket_id}.{signature}"


def scan(token):
    ticket_id = token.split(".")[0]
    if make_token(ticket_id) != token:
        return "invalid"
    if ticket_id in used:
        return "already_used"
    used.add(ticket_id)
    return "accepted"


token = make_token(42)
qrcode.make(token).save("ticket_42.png")
print("Token:", token)

print("First scan: ", scan(token))
print("Second scan:", scan(token))
print("Fake ticket:", scan("43.abc")) 