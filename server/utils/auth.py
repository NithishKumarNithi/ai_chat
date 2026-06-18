from fastapi.security import OAuth2PasswordBearer

import jwt
from pwdlib import PasswordHash

oauth_schema = OAuth2PasswordBearer(tokenUrl="login")

password_hash = PasswordHash.recommended()