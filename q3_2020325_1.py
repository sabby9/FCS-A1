import hmac
import base64
import hashlib


def verify(algo, q, secret, signature):
    if algo == "HS256":
        s = hmac.new(secret.encode("utf-8"), q.encode("utf-8"), hashlib.sha256).digest()
        t = base64.urlsafe_b64encode(s)
        t = t.replace(b'=', b'')
        if hmac.compare_digest(t, signature.encode('utf-8')):
            return True
        return False 


    elif algo == "HS384":
        s = hmac.new(secret.encode("utf-8"), q.encode("utf-8"), hashlib.sha384).digest()
        t = base64.urlsafe_b64encode(s)
        t = t.replace(b'=', b'')
        if hmac.compare_digest(t, signature.encode('utf-8')):
            return True
        return False 

def verifyJWT(token, secret):
    header, payload, sign = token.split('.')
    header_decoded = base64.b64decode(header).decode()
    header_idx = (header_decoded.find('alg'))
    header_alg = header_decoded[header_idx+6: header_idx+6+5]

    bytes_to_be_padded = 4 - (len(payload) % 4) 
    payload_decoded =  base64.b64decode(payload + '=' * bytes_to_be_padded).decode()
   
    q = header + "." + payload
    verified = verify(header_alg, q, secret, sign)
    
    if verified:
        return payload_decoded
    else:
        #return -1
        raise Exception("The secret provided is incorrect.")


  


jwt_token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJmY3MtYXNzaWdubWVudC0xIiwiaWF0IjoxNTE2MjM5MDIyLCJleHAiOjE3MDQwNjcyMDAsInJvbGxfbm8iOiIyMHh4eHh4IiwiZW1haWwiOiJhcnVuQGlpaXRkLmFjLmluIiwiaGludCI6Imxvd2VyY2FzZS1hbHBoYW51bWVyaWMtbGVuZ3RoLTUifQ.5RcJW1ZV5gsCmV-3mufIieogVoAqr_xdyUbvLJh49dQ'
jwt_HSA384 = 'eyJhbGciOiJIUzM4NCIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJmY3MtYXNzaWdubWVudC0xIiwiaWF0IjoxNTE2MjM5MDIyLCJleHAiOjE3MDQwNjcyMDAsInJvbGxfbm8iOiIyMDIwMzI1IiwiZW1haWwiOiJzYWRodmkyMDMyNUBpaWl0ZC5hYy5pbiIsImhpbnQiOiJsb3dlcmNhc2UtYWxwaGFudW1lcmljLWxlbmd0aC01In0.ytmeHIXLAwu-2lBWGkPGBt1gizXYCy8Thrh2qtUf80jDvk3fM-sbBCS9o2USdE0E'
a = 'abcdefghijklmnopqrstuvwxyz0123456789'

print('Token - \n' + str(jwt_token))
print("\n Payload: ")
print(verifyJWT(jwt_token, "gg476"))

print('\n Token - \n' + str(jwt_HSA384))
print("\n Payload: ")
print(verifyJWT(jwt_HSA384, "hs384"))


# for i in range(36):
#     for j in range(36):
#         for k in range(36):
#             for l in range(36):
#                 for m in range(36):
#                    key = '{}{}{}{}{}'.format(a[i],a[j],a[k],a[l],a[m])
#                    if(verifyJWT(jwt_token, key) != -1):
#                         print('The key is:' + str(key))
#                         break