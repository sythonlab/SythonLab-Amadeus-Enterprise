from core.amadeus_sdk import AmadeusSDK
from flights.amadeus_flight_sdk import AmadeusFlightSDK

sdk = AmadeusFlightSDK()

availability_status, availability = sdk.get_availability()
print('AVAILABILITY', availability_status, availability)

if availability_status == 200:
    informative_prices_without_pnr_status, informative_prices_without_pnr = sdk.informative_pricing_without_pnr()
    print('INFORMATIVE', informative_prices_without_pnr_status, informative_prices_without_pnr)

    if informative_prices_without_pnr_status == 200:
        session_id = AmadeusSDK.extract_session_id(informative_prices_without_pnr)
        security_token = AmadeusSDK.extract_security_token(informative_prices_without_pnr)

        check_rules_status, check_rules = sdk.check_rules(session_id, security_token)
        print('CHECK RULES', check_rules_status, check_rules)
