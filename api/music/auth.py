import hashlib
from django.utils import timezone
from .models import Token

def get_or_create_token(user):
    token = Token.objects.filter(user=user)
    if token.count() >=1:
        token = token[0]
        if not token.is_expired():
            return token
        token.delete()
    phrase = user.email + ':' +timezone.now().strftime('%Y-%m-%d-%H-%M-%S-%f')
    hash_phrase = hashlib.sha256(bytes(phrase,'ascii')).hexdigest()
    token = Token.objects.create(user=user, hash=hash_phrase)
    return token


