from lxml import etree
from zeep.plugins import Plugin


class HeaderAttributePlugin(Plugin):
    def egress(self, envelope, http_headers, operation, binding_options):
        SOAP_ENV = 'http://schemas.xmlsoap.org/soap/envelope/'
        ADD_NS = 'http://www.w3.org/2005/08/addressing'

        header = envelope.find(f'{{{SOAP_ENV}}}Header')
        if header is not None:
            new_nsmap = dict(header.nsmap)
            if 'add' not in new_nsmap:
                new_nsmap['add'] = ADD_NS

            new_header = etree.Element(f'{{{SOAP_ENV}}}Header', nsmap=new_nsmap)

            for child in list(header):
                header.remove(child)
                new_header.append(child)

            parent = envelope
            parent.remove(header)
            parent.insert(0, new_header)

        return envelope, http_headers
