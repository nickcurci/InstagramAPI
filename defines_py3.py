import requests
import json


def getCreds():
    """ Get creds required for use in the applications

    Returns:
        dictonary: credentials needed globally
    """
    # IGQVJWUEtPaTNSc01ocVBUeG52UUtBcG1rdkp2OEk0TEZAROXgtWTNrZAk8zVXF6bzFIMm5ISmVWcHlPMTJMa200OFlXNFE5R3NzcDBjODFaQ2oyOXlLLVkwTnRCc3BxY1M0UnhMVXc1S0tWVGNYLWpKRwZDZD
    creds = dict()  # dictionary to hold everything
    creds['access_token'] = 'EAAFZAcnnt6zgBACimSVSBoklh8Vd6EJSZAZBvb4ZBeC2ZAgdGwE4hcCOLdoi4795IraPf2NZCzxffS7ZCDjT5xR5XuHjrEOKWQQOSxHxWKkdV0EEelnfn5M4PIlqmdBAMAW3Wli21SpdsWifVzCd1MFZBfKcMMLbiwYOZCMKbzNRqNtUoo1MjI8DGqjhw26xZBES8dZBJQ2KiBUdOUBo2W7zjTWBZA0VwiIBCFlHZAYNxZBbi9n5rJgrgHHZCMP2QCoyyZCZCqV0ZD'  # access token for use with all api calls
    creds['graph_domain'] = 'https://graph.facebook.com/'  # base domain for api calls
    creds['graph_version'] = 'v13.0'  # version of the api we are hitting
    creds['endpoint_base'] = creds['graph_domain'] + creds['graph_version'] + '/'  # base endpoint with domain and version
    creds['instagram_account_id'] = '17841451732172670'  # users instagram account id

    return creds


def makeApiCall(url, endpointParams, type):
    """ Request data from endpoint with params

    Args:
        url: string of the url endpoint to make request from
        endpointParams: dictionary keyed by the names of the url parameters
    Returns:
        object: data from the endpoint
    """

    if type == 'POST':  # post request
        data = requests.post(url, endpointParams)
    else:  # get request
        data = requests.get(url, endpointParams)

    response = dict()  # hold response info
    response['url'] = url  # url we are hitting
    response['endpoint_params'] = endpointParams  # parameters for the endpoint
    response['endpoint_params_pretty'] = json.dumps(endpointParams, indent=4)  # pretty print for cli
    response['json_data'] = json.loads(data.content)  # response data from the api
    response['json_data_pretty'] = json.dumps(response['json_data'], indent=4)  # pretty print for cli

    return response  # get and return content