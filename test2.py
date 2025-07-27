import requests
from core.header_generator import AmadeusHeaderGenerator

headers = AmadeusHeaderGenerator()
headers.generate_header('availability')

soap_body = f"""<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:sec="http://xml.amadeus.com/2010/06/Security_v1" xmlns:typ="http://xml.amadeus.com/2010/06/Types_v1" xmlns:iat="http://www.iata.org/IATA/2007/00/IATA2010.1" xmlns:app="http://xml.amadeus.com/2010/06/AppMdw_CommonTypes_v3" xmlns:link="http://wsdl.amadeus.com/2010/06/ws/Link_v1" xmlns:ses="http://xml.amadeus.com/2010/06/Session_v3">
   <soapenv:Header xmlns:add="http://www.w3.org/2005/08/addressing">
      <add:MessageID>{headers.message_id}</add:MessageID>
      <add:Action>{headers.action}</add:Action>
      <add:To>{headers.to}</add:To>
      <oas:Security xmlns:oas="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-secext-1.0.xsd" xmlns:oas1="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-utility-1.0.xsd">
         <oas:UsernameToken oas1:Id="UsernameToken-1">
            <oas:Username>WSCPJCAR</oas:Username>
            <oas:Nonce EncodingType="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-soap-message-security-1.0#Base64Binary">{headers.nonce}</oas:Nonce>
            <oas:Password Type="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-username-token-profile-1.0#PasswordDigest">{headers.password_digest}</oas:Password>
            <oas1:Created>{headers.created_at}</oas1:Created>
         </oas:UsernameToken>
      </oas:Security>
      <AMA_SecurityHostedUser xmlns="http://xml.amadeus.com/2010/06/Security_v1">
         <UserID AgentDutyCode="SU" RequestorType="U" PseudoCityCode="{headers.office_id}" POS_Type="1"/>
      </AMA_SecurityHostedUser>
   </soapenv:Header>
   <soap-env:Body>
    <ns0:Fare_MasterPricerTravelBoardSearch xmlns:ns0="{headers.action}">
      <ns0:numberOfUnit>
        <ns0:unitNumberDetail>
          <ns0:numberOfUnits>2</ns0:numberOfUnits>
          <ns0:typeOfUnit>PX</ns0:typeOfUnit>
        </ns0:unitNumberDetail>
        <ns0:unitNumberDetail>
          <ns0:numberOfUnits>100</ns0:numberOfUnits>
          <ns0:typeOfUnit>RC</ns0:typeOfUnit>
        </ns0:unitNumberDetail>
      </ns0:numberOfUnit>
      <ns0:paxReference>
        <ns0:ptc>ADT</ns0:ptc>
        <ns0:traveller>
          <ns0:ref>1</ns0:ref>
        </ns0:traveller>
        <ns0:traveller>
          <ns0:ref>2</ns0:ref>
        </ns0:traveller>
      </ns0:paxReference>
      <ns0:fareOptions>
        <ns0:pricingTickInfo>
          <ns0:pricingTicketing>
            <ns0:priceType>ET</ns0:priceType>
            <ns0:priceType>RP</ns0:priceType>
            <ns0:priceType>RU</ns0:priceType>
            <ns0:priceType>TAC</ns0:priceType>
            <ns0:priceType>XND</ns0:priceType>
            <ns0:priceType>XLA</ns0:priceType>
            <ns0:priceType>XLO</ns0:priceType>
            <ns0:priceType>XLC</ns0:priceType>
            <ns0:priceType>XND</ns0:priceType>
          </ns0:pricingTicketing>
        </ns0:pricingTickInfo>
      </ns0:fareOptions>
      <ns0:travelFlightInfo>
        <ns0:companyIdentity>
          <ns0:carrierQualifier>X</ns0:carrierQualifier>
          <ns0:carrierId>NK</ns0:carrierId>
          <ns0:carrierId>F9</ns0:carrierId>
        </ns0:companyIdentity>
        <ns0:flightDetail>
          <ns0:flightType>N</ns0:flightType>
        </ns0:flightDetail>
      </ns0:travelFlightInfo>
      <ns0:itinerary>
        <ns0:requestedSegmentRef>
          <ns0:segRef>1</ns0:segRef>
        </ns0:requestedSegmentRef>
        <ns0:departureLocalization>
          <ns0:departurePoint>
            <ns0:locationId>HAV</ns0:locationId>
          </ns0:departurePoint>
        </ns0:departureLocalization>
        <ns0:arrivalLocalization>
          <ns0:arrivalPointDetails>
            <ns0:locationId>MAD</ns0:locationId>
          </ns0:arrivalPointDetails>
        </ns0:arrivalLocalization>
        <ns0:timeDetails>
          <ns0:firstDateTimeDetail>
            <ns0:date>2025-08-06</ns0:date>
          </ns0:firstDateTimeDetail>
        </ns0:timeDetails>
      </ns0:itinerary>
      <ns0:itinerary>
        <ns0:requestedSegmentRef>
          <ns0:segRef>2</ns0:segRef>
        </ns0:requestedSegmentRef>
        <ns0:departureLocalization>
          <ns0:departurePoint>
            <ns0:locationId>MAD</ns0:locationId>
          </ns0:departurePoint>
        </ns0:departureLocalization>
        <ns0:arrivalLocalization>
          <ns0:arrivalPointDetails>
            <ns0:locationId>HAV</ns0:locationId>
          </ns0:arrivalPointDetails>
        </ns0:arrivalLocalization>
        <ns0:timeDetails>
          <ns0:firstDateTimeDetail>
            <ns0:date>2025-08-13</ns0:date>
          </ns0:firstDateTimeDetail>
        </ns0:timeDetails>
      </ns0:itinerary>
    </ns0:Fare_MasterPricerTravelBoardSearch>
  </soap-env:Body>
</soapenv:Envelope>
"""

http_headers = {
    "Content-Type": "text/xml;charset=UTF-8",
    "SOAPAction": "http://webservices.amadeus.com/FMPTBQ_24_1_1A",
}

print(soap_body)
response = requests.post(
    "https://nodeD1.test.webservices.amadeus.com/",
    data=soap_body.encode("utf-8"),
    headers=http_headers
)

print(response.status_code)
print(response.text)
