import jwt

d = {"sub": "fcs-assignment-1", "iat": 1516239022, "exp": 1704067200, "roll_no": "2020325", "email": "sadhvi20325@iiitd.ac.in", "hint": "lowercase-alphanumeric-length-5"}
secret = 'gg476'
encoded_jwt = jwt.encode(d, secret, algorithm="HS256")
print(encoded_jwt)