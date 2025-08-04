import json

import requests
import xmltodict


class AmadeusSDK:

    @staticmethod
    def execute(url, query, http_headers=None, timeout=10, convert_to_json=True):
        if not http_headers:
            http_headers = {}
        http_headers.update({
            'Content-Type': 'application/soap+xml; charset=utf-8'
        })

        response = requests.post(
            url,
            data=query.encode('utf-8'),
            headers=http_headers,
            timeout=timeout
        )

        if not convert_to_json:
            return response.status_code, response

        return response.status_code, json.dumps(xmltodict.parse(response.text))
