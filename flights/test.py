from flights.amadeus_flight_sdk import AmadeusFlightSDK

sdk = AmadeusFlightSDK()

availability = sdk.get_availability()

print(availability)

informative_prices_without_pnr = sdk.informative_pricing_without_pnr()
print(informative_prices_without_pnr)
