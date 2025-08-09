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

        if check_rules_status == 200:
            logout_status, logout = sdk.logout(session_id, security_token)
            print('LOGOUT', logout_status, logout)

            if logout_status == 200:
                reserve_status, reserve = sdk.reserve()
                print('RESERVE', reserve_status, reserve)

                if reserve_status == 200:
                    session_id = AmadeusSDK.extract_session_id(reserve)
                    security_token = AmadeusSDK.extract_security_token(reserve)

                    add_pax_status, add_pax = sdk.add_passengers(session_id, security_token)
                    print('ADD PAX', add_pax_status, add_pax)

                    if add_pax_status == 200:
                        session_id = AmadeusSDK.extract_session_id(add_pax)
                        security_token = AmadeusSDK.extract_security_token(add_pax)

                        cash_status, cash = sdk.add_cash_payment(session_id, security_token)
                        print('CASH', cash_status, cash)

                        if cash_status == 200:
                            session_id = AmadeusSDK.extract_session_id(cash)
                            security_token = AmadeusSDK.extract_security_token(cash)

                            price_pnr_status, price_pnr = sdk.fare_price_pnr_with_booking_class(session_id,
                                                                                                security_token)
                            print('PRICE PNR WITH BOOKING CLASS', price_pnr_status, price_pnr)

                            if price_pnr_status == 200:
                                session_id = AmadeusSDK.extract_session_id(price_pnr)
                                security_token = AmadeusSDK.extract_security_token(price_pnr)

                                tst_status, tst = sdk.ticket_create_tst_from_pricing(session_id, security_token)
                                print('TICKET TST FROM PRICING', tst_status, tst)

                                if tst_status == 200:
                                    session_id = AmadeusSDK.extract_session_id(tst)
                                    security_token = AmadeusSDK.extract_security_token(tst)

                                    add_multi_status, add_multi = sdk.pnr_add_multielements(session_id, security_token)
                                    print('ADD MULTIELEMENTS (LOCATOR)', add_multi_status, add_multi)
