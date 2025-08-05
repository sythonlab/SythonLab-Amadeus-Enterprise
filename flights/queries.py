FLIGHT_AVAILABILITY_QUERY = """
    <soap:Envelope 
        xmlns:soap="http://www.w3.org/2003/05/soap-envelope"
        xmlns:wss="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-secext-1.0.xsd"
        xmlns:wsu="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-utility-1.0.xsd"
        xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" 
        xmlns:sec="http://xml.amadeus.com/2010/06/Security_v1" 
        xmlns:typ="http://xml.amadeus.com/2010/06/Types_v1" 
        xmlns:iat="http://www.iata.org/IATA/2007/00/IATA2010.1" 
        xmlns:app="http://xml.amadeus.com/2010/06/AppMdw_CommonTypes_v3" 
        xmlns:link="http://wsdl.amadeus.com/2010/06/ws/Link_v1" 
        xmlns:ses="http://xml.amadeus.com/2010/06/Session_v3">
    
       <soapenv:Header xmlns:add="http://www.w3.org/2005/08/addressing">
          <add:MessageID>WbsConsu-{MESSAGE_ID}</add:MessageID>
          <add:Action>{ACTION}</add:Action>
          <add:To>{TO}</add:To>
          <oas:Security xmlns:oas="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-secext-1.0.xsd"
                        xmlns:oas1="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-utility-1.0.xsd">
             <oas:UsernameToken oas1:Id="UsernameToken-1">
                <oas:Username>{USERNAME}</oas:Username>
                <oas:Nonce EncodingType="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-soap-message-security-1.0#Base64Binary">
                    {NONCE}
                </oas:Nonce>
                <oas:Password Type="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-username-token-profile-1.0#PasswordDigest">
                    {PASSWORD_DIGEST}
                </oas:Password>
                <oas1:Created>{CREATED_AT}</oas1:Created>
            </oas:UsernameToken>
          </oas:Security>
          <AMA_SecurityHostedUser xmlns="http://xml.amadeus.com/2010/06/Security_v1">
             <UserID AgentDutyCode="SU" RequestorType="U" PseudoCityCode="KIN1S2312" POS_Type="1"/>
          </AMA_SecurityHostedUser>
          <awsse:Session TransactionStatusCode="Start"
             xmlns:awsse="http://xml.amadeus.com/2010/06/Session_v3"/>
        </soapenv:Header>
    
       <soapenv:Body>
          <Fare_MasterPricerTravelBoardSearch>
             <numberOfUnit>
                <unitNumberDetail>
                   <numberOfUnits>2</numberOfUnits>
                   <typeOfUnit>PX</typeOfUnit>
                </unitNumberDetail>
                <unitNumberDetail>
                   <numberOfUnits>100</numberOfUnits>
                   <typeOfUnit>RC</typeOfUnit>
                </unitNumberDetail>
             </numberOfUnit>
             <paxReference>
                <ptc>ADT</ptc>
                <traveller>
                   <ref>1</ref>
                </traveller>
                <traveller>
                   <ref>2</ref>
                </traveller>
             </paxReference>
             <fareOptions>
                <pricingTickInfo>
                   <pricingTicketing>
                      <priceType>ET</priceType>
                      <priceType>RP</priceType>
                      <priceType>RU</priceType>
                      <priceType>TAC</priceType>
                      <priceType>XND</priceType>
                      <priceType>XLA</priceType>
                      <priceType>XLO</priceType>
                      <priceType>XLC</priceType>
                      <priceType>XND</priceType>
                   </pricingTicketing>
                </pricingTickInfo>
             </fareOptions>
             <travelFlightInfo>
                <companyIdentity>
                   <carrierQualifier>X</carrierQualifier>
                   <carrierId>NK</carrierId>
                   <carrierId>F9</carrierId>
                </companyIdentity>
                <flightDetail>
                   <flightType>N</flightType>
                </flightDetail>
             </travelFlightInfo>
             <itinerary>
                <requestedSegmentRef>
                   <segRef>1</segRef>
                </requestedSegmentRef>
                <departureLocalization>
                   <departurePoint>
                      <locationId>HAV</locationId>
                   </departurePoint>
                </departureLocalization>
                <arrivalLocalization>
                   <arrivalPointDetails>
                      <locationId>SCU</locationId>
                   </arrivalPointDetails>
                </arrivalLocalization>
                <timeDetails>
                   <firstDateTimeDetail>
                      <date>300825</date>
                   </firstDateTimeDetail>
                </timeDetails>
             </itinerary>
             <itinerary>
                <requestedSegmentRef>
                   <segRef>2</segRef>
                </requestedSegmentRef>
                <departureLocalization>
                   <departurePoint>
                      <locationId>SCU</locationId>
                   </departurePoint>
                </departureLocalization>
                <arrivalLocalization>
                   <arrivalPointDetails>
                      <locationId>HAV</locationId>
                   </arrivalPointDetails>
                </arrivalLocalization>
                <timeDetails>
                   <firstDateTimeDetail>
                      <date>040925</date>
                   </firstDateTimeDetail>
                </timeDetails>
             </itinerary>
          </Fare_MasterPricerTravelBoardSearch>
       </soapenv:Body>
    </soap:Envelope>
"""

FLIGHT_INFORMATIVE_PRICING_WITHOUT_PNR_QUERY = """
    <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:sec="http://xml.amadeus.com/2010/06/Security_v1" xmlns:typ="http://xml.amadeus.com/2010/06/Types_v1" xmlns:iat="http://www.iata.org/IATA/2007/00/IATA2010.1" xmlns:app="http://xml.amadeus.com/2010/06/AppMdw_CommonTypes_v3" xmlns:link="http://wsdl.amadeus.com/2010/06/ws/Link_v1" xmlns:ses="http://xml.amadeus.com/2010/06/Session_v3">
       <soapenv:Header xmlns:add="http://www.w3.org/2005/08/addressing">
            <add:MessageID>WbsConsu-{MESSAGE_ID}</add:MessageID>
            <add:Action>{ACTION}</add:Action>
            <add:To>{TO}</add:To>
            <oas:Security xmlns:oas="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-secext-1.0.xsd" xmlns:oas1="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-utility-1.0.xsd">
                <oas:UsernameToken oas1:Id="UsernameToken-1">
                    <oas:Username>{USERNAME}</oas:Username>
                    <oas:Nonce EncodingType="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-soap-message-security-1.0#Base64Binary">{NONCE}</oas:Nonce>
                    <oas:Password Type="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-username-token-profile-1.0#PasswordDigest">{PASSWORD_DIGEST}</oas:Password>
                    <oas1:Created>{CREATED_AT}</oas1:Created>
                </oas:UsernameToken>
            </oas:Security>
            <AMA_SecurityHostedUser xmlns="http://xml.amadeus.com/2010/06/Security_v1">
                <UserID AgentDutyCode="SU" RequestorType="U" PseudoCityCode="{OFFICE_ID}" POS_Type="1"/>
            </AMA_SecurityHostedUser>
            <awsse:Session TransactionStatusCode="Start" xmlns:awsse="http://xml.amadeus.com/2010/06/Session_v3"/>
        </soapenv:Header>
       <soapenv:Body>
          <Fare_InformativePricingWithoutPNR>
             <passengersGroup>
                <segmentRepetitionControl>
                   <segmentControlDetails>
                      <quantity>1</quantity>
                      <numberOfUnits>2</numberOfUnits>
                   </segmentControlDetails>
                </segmentRepetitionControl>
                <travellersID>
                   <travellerDetails>
                      <measurementValue>1</measurementValue>
                   </travellerDetails>
                   <travellerDetails>
                      <measurementValue>2</measurementValue>
                   </travellerDetails>
                </travellersID>
                <discountPtc>
                   <valueQualifier>ADT</valueQualifier>
                </discountPtc>
             </passengersGroup>
             <segmentGroup>
                <segmentInformation>
                   <flightDate>
                      <departureDate>300825</departureDate>
                      <departureTime>2350</departureTime>
                   </flightDate>
                   <boardPointDetails>
                      <trueLocationId>HAV</trueLocationId>
                   </boardPointDetails>
                   <offpointDetails>
                      <trueLocationId>SCU</trueLocationId>
                   </offpointDetails>
                   <companyDetails>
                      <marketingCompany>CU</marketingCompany>
                   </companyDetails>
                   <flightIdentification>
                      <flightNumber>470</flightNumber>
                      <bookingClass>X</bookingClass>
                   </flightIdentification>
                   <flightTypeDetails>
                      <flightIndicator>1</flightIndicator>
                   </flightTypeDetails>
                   <itemNumber>1</itemNumber>
                </segmentInformation>
             </segmentGroup>
             <segmentGroup>
                <segmentInformation>
                   <flightDate>
                      <departureDate>040925</departureDate>
                      <departureTime>1945</departureTime>
                   </flightDate>
                   <boardPointDetails>
                      <trueLocationId>SCU</trueLocationId>
                   </boardPointDetails>
                   <offpointDetails>
                      <trueLocationId>HAV</trueLocationId>
                   </offpointDetails>
                   <companyDetails>
                      <marketingCompany>CU</marketingCompany>
                   </companyDetails>
                   <flightIdentification>
                      <flightNumber>471</flightNumber>
                      <bookingClass>X</bookingClass>
                   </flightIdentification>
                   <flightTypeDetails>
                      <flightIndicator>2</flightIndicator>
                   </flightTypeDetails>
                   <itemNumber>2</itemNumber>
                </segmentInformation>
             </segmentGroup>
              <pricingOptionGroup>
                <pricingOptionKey>
                  <pricingOptionKey>RP</pricingOptionKey>
                </pricingOptionKey>
            </pricingOptionGroup>
            <pricingOptionGroup>
                <pricingOptionKey>
                  <pricingOptionKey>RU</pricingOptionKey>
                </pricingOptionKey>
            </pricingOptionGroup>
             <pricingOptionGroup>
                <pricingOptionKey>
                  <pricingOptionKey>RLO</pricingOptionKey>
                </pricingOptionKey>
            </pricingOptionGroup>
            <pricingOptionGroup>
            <pricingOptionKey>
                <pricingOptionKey>VC</pricingOptionKey>
            </pricingOptionKey>
            <carrierInformation>
                <companyIdentification>
                    <otherCompany>CU</otherCompany>
                </companyIdentification>
            </carrierInformation>
        </pricingOptionGroup>
          </Fare_InformativePricingWithoutPNR>
       </soapenv:Body>
    </soapenv:Envelope>
"""

FLIGHT_CHECK_RULES_QUERY = """
    <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:sec="http://xml.amadeus.com/2010/06/Security_v1" xmlns:typ="http://xml.amadeus.com/2010/06/Types_v1" xmlns:iat="http://www.iata.org/IATA/2007/00/IATA2010.1" xmlns:app="http://xml.amadeus.com/2010/06/AppMdw_CommonTypes_v3" xmlns:link="http://wsdl.amadeus.com/2010/06/ws/Link_v1" xmlns:ses="http://xml.amadeus.com/2010/06/Session_v3">
       <soapenv:Header xmlns:add="http://www.w3.org/2005/08/addressing">
            <add:MessageID>{MESSAGE_ID}</add:MessageID>
            <add:Action>{ACTION}</add:Action>
            <add:To>{TO}</add:To>
            <awsse:Session TransactionStatusCode="InSeries" xmlns:awsse="http://xml.amadeus.com/2010/06/Session_v3">
                <awsse:SessionId>{SESSION_ID}</awsse:SessionId>
                <awsse:SequenceNumber>{SEQUENCE_NUMBER}</awsse:SequenceNumber>
                <awsse:SecurityToken>{SECURITY_TOKEN}</awsse:SecurityToken>
            </awsse:Session>
        </soapenv:Header>
       <soapenv:Body>
            <Fare_CheckRules>
                <msgType>
                    <messageFunctionDetails>
                        <messageFunction>712</messageFunction>
                    </messageFunctionDetails>
                </msgType>
                <itemNumber>
                    <itemNumberDetails>
                        <number>1</number>
                    </itemNumberDetails>
                    <itemNumberDetails>
                        <number>1</number>
                        <type>FC</type>
                    </itemNumberDetails>
                </itemNumber>
                <fareRule>
                    <tarifFareRule>
                        <ruleSectionId>PE</ruleSectionId>
                        <ruleSectionId>MX</ruleSectionId>
                        <ruleSectionId>SR</ruleSectionId>
                        <ruleSectionId>TR</ruleSectionId>
                        <ruleSectionId>AP</ruleSectionId>
                        <ruleSectionId>FL</ruleSectionId>
                    </tarifFareRule>
                </fareRule>
            </Fare_CheckRules>
       </soapenv:Body>
    </soapenv:Envelope>
"""

FLIGHT_SIGNOUT_QUERY = """
    <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:sec="http://xml.amadeus.com/2010/06/Security_v1" xmlns:typ="http://xml.amadeus.com/2010/06/Types_v1" xmlns:iat="http://www.iata.org/IATA/2007/00/IATA2010.1" xmlns:app="http://xml.amadeus.com/2010/06/AppMdw_CommonTypes_v3" xmlns:link="http://wsdl.amadeus.com/2010/06/ws/Link_v1" xmlns:ses="http://xml.amadeus.com/2010/06/Session_v3" xmlns:vls="http://xml.amadeus.com/VLSSOQ_04_1_1A">
       <soapenv:Header xmlns:add="http://www.w3.org/2005/08/addressing">
            <add:MessageID>{MESSAGE_ID}</add:MessageID>
            <add:Action>{ACTION}</add:Action>
            <add:To>{TO}</add:To>
            <awsse:Session TransactionStatusCode="End" xmlns:awsse="http://xml.amadeus.com/2010/06/Session_v3">
                <awsse:SessionId>{SESSION_ID}</awsse:SessionId>
                <awsse:SequenceNumber>{SEQUENCE_NUMBER}</awsse:SequenceNumber>
                <awsse:SecurityToken>{SECURITY_TOKEN}</awsse:SecurityToken>
            </awsse:Session>
        </soapenv:Header>
       <soapenv:Body>
          <Security_SignOut></Security_SignOut>
       </soapenv:Body>
    </soapenv:Envelope>
"""
