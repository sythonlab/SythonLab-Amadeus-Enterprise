import settings
from core.amadeus_sdk import AmadeusSDK
from core.header_generator import AmadeusHeaderGenerator
from flights.queries import FLIGHT_AVAILABILITY_QUERY, FLIGHT_INFORMATIVE_PRICING_WITHOUT_PNR_QUERY, \
    FLIGHT_CHECK_RULES_QUERY, FLIGHT_SIGNOUT_QUERY, FLIGHT_RESERVE_QUERY, FLIGHT_ADD_PASSENGERS_QUERY, \
    ADD_CASH_PAYMENT_QUERY, FARE_PRICE_PNR_WITH_BOOKING_CLASS_QUERY, TICKET_CREATE_TST_FROM_PRICING_QUERY, \
    PNR_ADD_MULTIELEMENTS_QUERY


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
        )

    def reserve(self):
        action = 'http://webservices.amadeus.com/ITAREQ_05_2_IA'
        headers = AmadeusHeaderGenerator()
        headers.generate_header()

        return AmadeusSDK.execute(
            settings.AMADEUS_CONFIG['ENDPOINT'],
            FLIGHT_RESERVE_QUERY.format(
                MESSAGE_ID=headers.message_id,
                TO=settings.AMADEUS_CONFIG['ENDPOINT'],
                ACTION=action,
                USERNAME=settings.AMADEUS_CONFIG['USERNAME'],
                OFFICE_ID=settings.AMADEUS_CONFIG['OFFICE_ID'],
                NONCE=headers.nonce,
                PASSWORD_DIGEST=headers.password_digest,
                CREATED_AT=headers.created_at,
            ),
            http_headers={
                'SOAPAction': action
            },
        )

    def add_passengers(self, session_id, security_token, sequence_number=2):
        action = 'http://webservices.amadeus.com/PNRADD_22_1_1A'
        headers = AmadeusHeaderGenerator()
        headers.generate_header()

        return AmadeusSDK.execute(
            settings.AMADEUS_CONFIG['ENDPOINT'],
            FLIGHT_ADD_PASSENGERS_QUERY.format(
                MESSAGE_ID=headers.message_id,
                TO=settings.AMADEUS_CONFIG['ENDPOINT'],
                ACTION=action,
                SEQUENCE_NUMBER=sequence_number,
                SECURITY_TOKEN=security_token,
                SESSION_ID=session_id,
                OFFICE_ID=settings.AMADEUS_CONFIG['OFFICE_ID'],
            ),
            http_headers={
                'SOAPAction': action
            },
        )

    def add_cash_payment(self, session_id, security_token, sequence_number=2):
        action = 'http://webservices.amadeus.com/TFOPCQ_19_2_1A'
        headers = AmadeusHeaderGenerator()
        headers.generate_header()

        return AmadeusSDK.execute(
            settings.AMADEUS_CONFIG['ENDPOINT'],
            ADD_CASH_PAYMENT_QUERY.format(
                MESSAGE_ID=headers.message_id,
                TO=settings.AMADEUS_CONFIG['ENDPOINT'],
                ACTION=action,
                SEQUENCE_NUMBER=sequence_number,
                SECURITY_TOKEN=security_token,
                SESSION_ID=session_id,
                OFFICE_ID=settings.AMADEUS_CONFIG['OFFICE_ID'],
            ),
            http_headers={
                'SOAPAction': action
            },
        )

    def fare_price_pnr_with_booking_class(self, session_id, security_token, sequence_number=3):
        action = 'http://webservices.amadeus.com/TPCBRQ_23_2_1A'
        headers = AmadeusHeaderGenerator()
        headers.generate_header()

        return AmadeusSDK.execute(
            settings.AMADEUS_CONFIG['ENDPOINT'],
            FARE_PRICE_PNR_WITH_BOOKING_CLASS_QUERY.format(
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
        )

    def ticket_create_tst_from_pricing(self, session_id, security_token, sequence_number=4):
        action = 'http://webservices.amadeus.com/TAUTCQ_04_1_1A'
        headers = AmadeusHeaderGenerator()
        headers.generate_header()

        return AmadeusSDK.execute(
            settings.AMADEUS_CONFIG['ENDPOINT'],
            TICKET_CREATE_TST_FROM_PRICING_QUERY.format(
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
        )

    def pnr_add_multielements(self, session_id, security_token, sequence_number=5):
        action = 'http://webservices.amadeus.com/PNRADD_22_1_1A'
        headers = AmadeusHeaderGenerator()
        headers.generate_header()

        return AmadeusSDK.execute(
            settings.AMADEUS_CONFIG['ENDPOINT'],
            PNR_ADD_MULTIELEMENTS_QUERY.format(
                MESSAGE_ID=headers.message_id,
                TO=settings.AMADEUS_CONFIG['ENDPOINT'],
                ACTION=action,
                SEQUENCE_NUMBER=sequence_number,
                SECURITY_TOKEN=security_token,
                SESSION_ID=session_id,
                OFFICE_ID=settings.AMADEUS_CONFIG['OFFICE_ID'],
            ),
            http_headers={
                'SOAPAction': action
            },
            show_traces=True
        )
