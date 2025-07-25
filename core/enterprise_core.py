import base64
import hashlib
import datetime
import uuid

from lxml import etree

import settings


class AmadeusEnterpriseSDK:
    created_at = None
    nonce = None

    def __init__(self, **kwargs):
        pass

    def get_headers(self, action, sequence):
        self.generate_created_at()
        self.generate_nonce()

        return {
            'message_id': self.generate_message_id(),
            'action': self.generate_action(action),
            'to': self.generate_to(action),
            'session': self.generate_session(sequence),
            'security': self.generate_security(),
            'user_id': self.generate_user_id()
        }

    def generate_message_id(self):
        value = f'WbsConsu-{str(uuid.uuid4())}'
        header = etree.Element(f"{{{settings.NSMAP['add']}}}MessageID", nsmap={'add': settings.NSMAP['add']})
        header.text = value
        return {'value': value, 'header': header}

    def generate_action(self, action):
        value = {
            'availability': 'http://webservices.amadeus.com/FMPTBQ_23_1_1A',
        }[action]
        header = etree.Element(f"{{{settings.NSMAP['add']}}}Action", nsmap={'add': settings.NSMAP['add']})
        header.text = value
        print(f'ACTION: {value}')
        return {'value': value, 'header': header}

    def generate_to(self, action):
        value = {
            'availability': 'https://nodeD1.test.webservices.amadeus.com/1ASIWCARCPJ'
        }[action]
        header = etree.Element(f"{{{settings.NSMAP['add']}}}To", nsmap={'add': settings.NSMAP['add']})
        header.text = value
        print(f'TO: {value}')
        return {'value': value, 'header': header}

    def generate_session_id(self):
        value = '01HFHCODVI'
        header = etree.Element(f"{{{settings.NSMAP['awsse']}}}SessionId", nsmap={'awsse': settings.NSMAP['awsse']})
        header.text = value
        print(f'SESSION ID: {value}')
        return {'value': value, 'header': header}

    def generate_sequence_number(self, number):
        header = etree.Element(f"{{{settings.NSMAP['awsse']}}}SequenceNumber", nsmap={'awsse': settings.NSMAP['awsse']})
        header.text = str(number)
        print(f'SEQUENCE NUMBER: {number}')
        return {'value': number, 'header': header}

    def generate_security_token(self):
        value = '1SP31VH87S9T310EWJIH27JLRI'
        header = etree.Element(f"{{{settings.NSMAP['awsse']}}}SecurityToken", nsmap={'awsse': settings.NSMAP['awsse']})
        header.text = value
        print(f'SECURITY TOKEN: {value}')
        return {'value': value, 'header': header}

    def generate_username(self):
        value = settings.AMADEUS_CONFIG['USERNAME']
        header = etree.Element(f"{{{settings.NSMAP['oas']}}}Username", nsmap={'oas': settings.NSMAP['oas']})
        header.text = value
        print(f'USERNAME: {value}')
        return {'value': value, 'header': header}

    def generate_nonce(self):
        self.nonce = 'IMegbs6mAN7ieAI+kd01mA=='
        header = etree.Element(f"{{{settings.NSMAP['oas']}}}Nonce", nsmap={'oas': settings.NSMAP['oas']})
        header.attrib[
            'EncodingType'] = 'http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-soap-message-security-1.0#Base64Binary'
        header.text = self.nonce
        print(f'NONCE: {self.nonce}')
        return {'value': self.nonce, 'header': header}

    def generate_user_id(self):
        root_header = etree.Element('AMA_SecurityHostedUser')
        root_header.attrib['xmlns'] = 'http://xml.amadeus.com/2010/06/Security_v1'

        header = etree.Element('UserID')
        header.attrib['AgentDutyCode'] = 'SU'
        header.attrib['POS_Type'] = '1'
        header.attrib['PseudoCityCode'] = settings.AMADEUS_CONFIG['OFFICE_ID']
        header.attrib['RequestorType'] = 'U'

        root_header.append(header)

        return {'value': None, 'header': root_header}

    def generate_password(self):
        value = self.generate_password_digest()
        header = etree.Element(f"{{{settings.NSMAP['oas']}}}Password", nsmap={'oas': settings.NSMAP['oas']})
        header.attrib[
            'Type'] = 'http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-username-token-profile-1.0#PasswordDigest'
        header.text = value
        print(f'PASSWORD: {value}')
        return {'value': value, 'header': header}

    def generate_created_at(self):
        self.created_at = self.get_created_at()
        header = etree.Element(f"{{{settings.NSMAP['oas1']}}}Created", nsmap={'oas1': settings.NSMAP['oas1']})
        header.text = self.created_at
        print(f'CREATED AT: {self.created_at}')
        return {'value': self.created_at, 'header': header}

    def generate_session(self, sequence):
        header = etree.Element(f"{{{settings.NSMAP['awsse']}}}Session", nsmap={'awsse': settings.NSMAP['awsse']})
        header.attrib['TransactionStatusCode'] = 'InSeries'
        header.append(self.generate_session_id()['header'])
        header.append(self.generate_sequence_number(sequence)['header'])
        header.append(self.generate_security_token()['header'])
        return {'value': None, 'header': header}

    def generate_security(self):
        header_security = etree.Element(f"{{{settings.NSMAP['oas']}}}Security", nsmap={'oas': settings.NSMAP['oas']})

        header_username_token = etree.Element(f"{{{settings.NSMAP['oas']}}}UsernameToken",
                                              nsmap={'oas1': settings.NSMAP['oas1']})
        header_username_token.attrib[f'{{{settings.NSMAP['oas1']}}}Id'] = 'UsernameToken-1'
        header_username_token.append(self.generate_username()['header'])
        header_username_token.append(self.generate_nonce()['header'])
        header_username_token.append(self.generate_password()['header'])
        header_username_token.append(self.generate_created_at()['header'])

        header_security.append(header_username_token)
        return {'value': None, 'header': header_security}

    def get_created_at(self):
        return datetime.datetime.now(datetime.UTC).strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + "Z"

    def generate_password_encrypt(self):
        if settings.AMADEUS_CONFIG['PASSWORD'] is None or len(settings.AMADEUS_CONFIG['PASSWORD']) == 0:
            raise ValueError('Password is not defined at project level')
        sha = hashlib.new('SHA1')
        sha.update(settings.AMADEUS_CONFIG['PASSWORD'].encode('utf-8'))
        print(f'EL PASSWORD ENCRYPT SE GENERA CON SHA1 PARA EL PASSWORD {settings.AMADEUS_CONFIG["PASSWORD"]}')
        return sha.digest()

    def generate_password_digest(self):
        b1 = self.nonce.encode('utf-8')
        b2 = self.created_at.encode('utf-8')
        b3 = self.generate_password_encrypt()

        print(f'EL DIGEST SE GENERA CON NONCE {b1} - CREATED {b2} - PASSWORD ENCRYPT {b3}')

        sha1 = hashlib.sha1()
        sha1.update(b1 + b2 + b3)
        return base64.b64encode(sha1.digest()).decode('utf-8')


"""<soap-env:Header>
    <add:MessageID xmlns:add="http://www.w3.org/2005/08/addressing">WbsConsu-ae1d3f05-79c6-4800-91ca-a7837ce88497</add:MessageID>
    <add:Action xmlns:add="http://www.w3.org/2005/08/addressing">http://webservices.amadeus.com/FMPTBQ_23_1_1A</add:Action>
    <add:To xmlns:add="http://www.w3.org/2005/08/addressing">https://nodeD1.test.webservices.amadeus.com/1ASIWCARCPJ</add:To>
    <oas:Security xmlns:oas="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-secext-1.0.xsd">
      <oas:UsernameToken xmlns:oas1="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-utility-1.0.xsd" oas1:Id="UsernameToken-1">
        <oas:Username>WSCPJCAR</oas:Username>
        <oas:Nonce EncodingType="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-soap-message-security-1.0#Base64Binary">IMegbs6mAN7ieAI+kd01mA==</oas:Nonce>
        <oas:Password Type="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-username-token-profile-1.0#PasswordDigest">Iv5ZHz8ZauOXJXW9ZRuSJ8IJiAE=</oas:Password>
        <oas1:Created>2025-07-25T14:27:23.553Z</oas1:Created>
      </oas:UsernameToken>
    </oas:Security>
    <AMA_SecurityHostedUser xmlns="http://xml.amadeus.com/2010/06/Security_v1">
      <UserID AgentDutyCode="SU" POS_Type="1" PseudoCityCode="KIN1S2312" RequestorType="U"/>
    </AMA_SecurityHostedUser>
  </soap-env:Header>"""

"""<soapenv:Header xmlns:add="http://www.w3.org/2005/08/addressing">
      <add:MessageID>WbsConsu-4aVFOgNlIrMYlteE7y7oPmTgMDZ0G17-SFvAwVUvh</add:MessageID>
      <add:Action>http://webservices.amadeus.com/FMPTBQ_24_1_1A</add:Action>
      <add:To>https://nodeD1.test.webservices.amadeus.com/1ASIWCARCPJ</add:To>
      <oas:Security xmlns:oas="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-secext-1.0.xsd" xmlns:oas1="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-utility-1.0.xsd">
         <oas:UsernameToken oas1:Id="UsernameToken-1">
            <oas:Username>WSCPJCAR</oas:Username>
            <oas:Nonce EncodingType="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-soap-message-security-1.0#Base64Binary">IMegbs6mAN7ieAI+kd01mA==</oas:Nonce>
            <oas:Password Type="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-username-token-profile-1.0#PasswordDigest">Sh/wLA7nsSgCNZzv2YZothzxLVM=</oas:Password>
            <oas1:Created>2025-07-25T04:01:05.564Z</oas1:Created>
         </oas:UsernameToken>
      </oas:Security>
      <AMA_SecurityHostedUser xmlns="http://xml.amadeus.com/2010/06/Security_v1">
         <UserID AgentDutyCode="SU" RequestorType="U" PseudoCityCode="KIN1S2312" POS_Type="1"/>
      </AMA_SecurityHostedUser>
   </soapenv:Header>"""

"""
"""