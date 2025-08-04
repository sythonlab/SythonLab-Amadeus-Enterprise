import requests
from core.header_generator import AmadeusHeaderGenerator
from flights.queries import AVAILABILITY_QUERY

headers = AmadeusHeaderGenerator()
headers.generate_header('availability')

http_headers = {
    "Content-Type": "application/soap+xml; charset=utf-8",
    "SOAPAction": "http://webservices.amadeus.com/FMPTBQ_23_1_1A"
}

response = requests.post(
    "https://nodeD1.test.webservices.amadeus.com/1ASIWCARCPJ",
    data=AVAILABILITY_QUERY.format(
        MESSAGE_ID=headers.message_id,
        USERNAME=headers.username,
        NONCE=headers.nonce,
        PASSWORD_DIGEST=headers.password_digest,
        CREATED_AT=headers.created_at
    ).encode("utf-8"),
    headers=http_headers,
    timeout=10
)

print(response.status_code)
print(response.text)
