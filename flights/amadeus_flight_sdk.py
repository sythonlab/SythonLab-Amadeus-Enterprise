import settings
from core.amadeus_sdk import AmadeusSDK
from core.header_generator import AmadeusHeaderGenerator
from flights.queries import AVAILABILITY_QUERY


class AmadeusFlightSDK:
    def get_availability(self):
        headers = AmadeusHeaderGenerator()
        headers.generate_header('availability')

        return AmadeusSDK.execute(
            settings.AMADEUS_CONFIG['ENDPOINTS']['FLIGHT_AVAILABILITY'],
            AVAILABILITY_QUERY.format(
                MESSAGE_ID=headers.message_id,
                USERNAME=settings.AMADEUS_CONFIG['USERNAME'],
                NONCE=headers.nonce,
                PASSWORD_DIGEST=headers.password_digest,
                CREATED_AT=headers.created_at,
                TO=headers.to,
            ),
            http_headers={
                'SOAPAction': 'http://webservices.amadeus.com/FMPTBQ_23_1_1A'
            }
        )
