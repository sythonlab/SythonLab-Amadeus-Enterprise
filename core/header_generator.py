import base64
import hashlib
import uuid
from datetime import datetime, timezone


class AmadeusHeaderGenerator:
    username = 'WSCPJCAR'
    office_id = 'KIN1S2312'
    message_id = None
    action = None
    to = None
    nonce_bytes = None
    nonce = None
    created_at = None
    password_digest = None

    def __init__(self, **kwargs):
        pass

    def generate_message_id(self):
        code = f'{str(uuid.uuid4())}{str(uuid.uuid4())}'.replace('-', '')
        self.message_id = f'WbsConsu-{code[:31]}-{code[31:40]}'

        print('MESSAGE ID', self.message_id)

    def generate_action(self, target):
        self.action = {
            'availability': 'http://webservices.amadeus.com/FMPTBQ_24_1_1A'
        }[target]

        print('ACTION', self.action)

    def generate_to(self, target):
        self.to = {
            'availability': 'https://nodeD1.test.webservices.amadeus.com/1ASIWCARCPJ'
        }[target]

        print('TO', self.to)

    def generate_nonce(self):
        # self.nonce_bytes = os.urandom(16)
        self.nonce_bytes = str(uuid.uuid4()).replace('-', '')[:16].encode('utf-8')
        self.nonce = base64.b64encode(self.nonce_bytes).decode('utf-8')

        print('NONCE BYTES', self.nonce_bytes)
        print('NONCE', self.nonce)

    def generate_created_at(self):
        self.created_at = datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3] + 'Z'

        print('CREATED', self.created_at)

    def generate_password_digest(self):
        password_bytes = '6WbmmXZJGS?D'.encode('utf-8')
        concatenated = self.nonce_bytes + self.created_at.encode('utf-8') + password_bytes
        digest = hashlib.sha1(concatenated).digest()
        self.password_digest = base64.b64encode(digest).decode('utf-8')

        print('PASSWORD DIGEST', self.password_digest, 'GENERATED WITH PASSWORD BYTES', password_bytes, 'CREATED',
              self.created_at, 'AND NONCE BYTES', self.nonce_bytes)

    def generate_header(self, target):
        self.generate_message_id()
        self.generate_action(target)
        self.generate_to(target)
        self.generate_created_at()
        self.generate_nonce()
        self.generate_password_digest()
