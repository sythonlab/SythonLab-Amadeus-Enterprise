from flights.amadeus_flight_sdk import AmadeusFlightSDK

sdk = AmadeusFlightSDK()

availability = sdk.get_availability()

print(availability)
