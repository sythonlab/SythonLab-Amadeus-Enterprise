import settings
from core.amadeus_sdk import AmadeusSDK
from core.header_generator import AmadeusHeaderGenerator
from flights.queries import FLIGHT_AVAILABILITY_QUERY, FLIGHT_INFORMATIVE_PRICING_WITHOUT_PNR_QUERY, \
    FLIGHT_CHECK_RULES_QUERY, FLIGHT_SIGNOUT_QUERY


class AmadeusFlightSDK:
    def get_availability(self):
        action = 'http://webservices.amadeus.com/FMPTBQ_23_1_1A'
        headers = AmadeusHeaderGenerator()
        headers.generate_header()

        return AmadeusSDK.execute(
            settings.AMADEUS_CONFIG['ENDPOINT'],
            FLIGHT_AVAILABILITY_QUERY.format(
                MESSAGE_ID=headers.message_id,
                USERNAME=settings.AMADEUS_CONFIG['USERNAME'],
                OFFICE_ID=settings.AMADEUS_CONFIG['OFFICE_ID'],
                NONCE=headers.nonce,
                PASSWORD_DIGEST=headers.password_digest,
                CREATED_AT=headers.created_at,
                TO=settings.AMADEUS_CONFIG['ENDPOINT'],
                ACTION=action
            ),
            http_headers={
                'SOAPAction': action
            }
        )

    def informative_pricing_without_pnr(self):
        action = 'http://webservices.amadeus.com/TIPNRQ_23_1_1A'
        headers = AmadeusHeaderGenerator()
        headers.generate_header()

        return AmadeusSDK.execute(
            settings.AMADEUS_CONFIG['ENDPOINT'],
            FLIGHT_INFORMATIVE_PRICING_WITHOUT_PNR_QUERY.format(
                MESSAGE_ID=headers.message_id,
                USERNAME=settings.AMADEUS_CONFIG['USERNAME'],
                OFFICE_ID=settings.AMADEUS_CONFIG['OFFICE_ID'],
                NONCE=headers.nonce,
                PASSWORD_DIGEST=headers.password_digest,
                CREATED_AT=headers.created_at,
                TO=settings.AMADEUS_CONFIG['ENDPOINT'],
                ACTION=action
            ),
            http_headers={
                'SOAPAction': action
            },
        )

    def check_rules(self, session_id, security_token, sequence_number=2):
        action = 'http://webservices.amadeus.com/FARQNQ_07_1_1A'
        headers = AmadeusHeaderGenerator()
        headers.generate_header()

        return AmadeusSDK.execute(
            settings.AMADEUS_CONFIG['ENDPOINT'],
            FLIGHT_CHECK_RULES_QUERY.format(
                MESSAGE_ID=headers.message_id,
                USERNAME=settings.AMADEUS_CONFIG['USERNAME'],
                OFFICE_ID=settings.AMADEUS_CONFIG['OFFICE_ID'],
                NONCE=headers.nonce,
                PASSWORD_DIGEST=headers.password_digest,
                CREATED_AT=headers.created_at,
                TO=settings.AMADEUS_CONFIG['ENDPOINT'],
                ACTION=action,
                SEQUENCE_NUMBER=sequence_number,
                SECURITY_TOKEN=security_token,
                SESSION_ID=session_id,
            ),
            http_headers={
                'SOAPAction': action
            },
        )

    def logout(self, session_id, security_token, sequence_number=3):
        action = 'http://webservices.amadeus.com/VLSSOQ_04_1_1A'
        headers = AmadeusHeaderGenerator()
        headers.generate_header()

        return AmadeusSDK.execute(
            settings.AMADEUS_CONFIG['ENDPOINT'],
            FLIGHT_SIGNOUT_QUERY.format(
                MESSAGE_ID=headers.message_id,
                TO=settings.AMADEUS_CONFIG['ENDPOINT'],
                ACTION=action,
                SEQUENCE_NUMBER=sequence_number,
                SECURITY_TOKEN=security_token,
                SESSION_ID=session_id,
            ),
            http_headers={
                'SOAPAction': action
            },
            show_traces=True
        )
