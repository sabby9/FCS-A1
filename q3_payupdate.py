import json
import base64
import hmac
import hashlib

jwt_token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJmY3MtYXNzaWdubWVudC0xIiwiaWF0IjoxNTE2MjM5MDIyLCJleHAiOjE3MDQwNjcyMDAsInJvbGxfbm8iOiIyMHh4eHh4IiwiZW1haWwiOiJhcnVuQGlpaXRkLmFjLmluIiwiaGludCI6Imxvd2VyY2FzZS1hbHBoYW51bWVyaWMtbGVuZ3RoLTUifQ.5RcJW1ZV5gsCmV-3mufIieogVoAqr_xdyUbvLJh49dQ'
secret = 'gg476'

header, payload, sign = jwt_token.split('.')
header_decoded = base64.b64decode(header).decode()
header_idx = (header_decoded.find('alg'))
header_alg = header_decoded[header_idx+6: header_idx+6+5]

bytes_to_be_padded = 4 - (len(payload) % 4) 
payload_decoded =  base64.urlsafe_b64decode(payload + '=' * bytes_to_be_padded).decode()
# print(payload_decoded)

# update
dict_payload = json.loads(payload_decoded)
dict_payload['roll_no'] = "2020325"
dict_payload['email'] = "sadhvi20325@iiitd.ac.in"
payload = json.dumps(dict_payload)
# print(payload)
bytes_payload = payload.encode("utf-8")
encoded_payload = base64.urlsafe_b64encode(bytes_payload).rstrip(b'=').decode('utf-8')
# print(encoded_payload)

q = header + "." + encoded_payload
hmac_obj = hmac.new(bytes(secret, 'utf-8'), bytes(q, 'utf-8'), hashlib.sha256).digest()
sign = base64.urlsafe_b64encode(hmac_obj).rstrip(b'=').decode('utf-8')
# sign= base64url_encode(hmac_obj)
sign = base64.urlsafe_b64encode(hmac_obj).replace(b"=", b"").decode()


token_gen = q + "." + sign
print(token_gen)