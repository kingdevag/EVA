from urllib.parse import quote_plus

from openai import error
from openai.api_resources.abstract.api_resource import APIResource
from openai.util import ApiType

class DeletableAPIResource(APIResource):
    @classmethod
    def delete(cls, sid, api_type=None, api_version=None, **params):
        if isinstance(cls, APIResource):
            raise ValueError(".delete may only be called as a class method now.")

        base = cls.class_url()
        extn = quote_plus(sid)

        typed_api_type, api_version = cls._get_api_type_and_version(api_type, api_version)
        if typed_api_type == ApiType.AZURE:
            url = "/%s%s/%s?api-version=%s" % (cls.azure_api_prefix, base, extn, api_version)
        elif typed_api_type == ApiType.OPEN_AI:
            url = "%s/%s" % (base, extn)
        else:
            raise error.InvalidAPIType('Unsupported API type %s' % api_type)            
        
        return cls._static_request("delete", url, api_type=api_type, api_version=api_version, **params)