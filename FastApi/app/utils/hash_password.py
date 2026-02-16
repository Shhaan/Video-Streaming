from passlib.context import CryptContext
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend
import base64 

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash_password(password: str) -> str:
    return pwd_context.hash(password)


def verify_password(password: str, hashed: str) -> bool:
    return pwd_context.verify(password, hashed)


 

def base64url_encode(data: bytes):
    return base64.urlsafe_b64encode(data).rstrip(b"=").decode("utf-8")

def load_public_key():
    with open("public.pem", "rb") as f:
        key = serialization.load_pem_public_key(
            f.read(),
            backend=default_backend()
        )
  
    numbers = key.public_numbers()

    n = base64url_encode(numbers.n.to_bytes((numbers.n.bit_length() + 7) // 8, "big"))
    e = base64url_encode(numbers.e.to_bytes((numbers.e.bit_length() + 7) // 8, "big"))

    return {
        "kty": "RSA",
        "use": "sig",
        "kid": "my-key-1",
        "alg": "RS256",
        "n": n,
        "e": e,
    }