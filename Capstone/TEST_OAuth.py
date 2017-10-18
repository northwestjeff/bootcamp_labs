from quickbooks import Oauth2SessionManager

from quickbooks import QuickBooks

session_manager = Oauth2SessionManager(
    sandbox=True,
    client_id="Q0AaC7Zk5JlBRJqGjBkLthuJ7RV8Jpdg8xab0vtviZAYJWF16g",
    client_secret="s5I3D2Wn22tsbcXcUwkdrVV5d1LGcH7bTimWD6Bb",
    base_url='http://localhost:8000',
    )

# client = QuickBooks(
#     sandbox=True,
#     session_manager=session_manager,
#     company_id="193514632414899"
# )

callback_url = 'http://localhost:8000' # Quickbooks will send the response to this url
session_manager.get_access_tokens(request.GET['code'])
authorize_url = client.get_authorize_url(callback_url)
request_token = client.request_token
request_token_secret = client.request_token_secret

#
# from quickbooks import *
#
# consumerKey =           "fromApiConsole"
# consumerSecret =        "fromApiConsole"
# callbackUrl =           "https://quickbooks.api.intuit.com/v3"
#
# qbObject = QuickBooks(
#         consumer_key = consumerKey,
#         consumer_secret = consumerSecret,
#         callback_url = callbackUrl
#         )
#
# authorize_url = qbObject.get_authorize_url() # will create a service, and further set up the qbObject.
#
# oauth_token = request.GET['oauth_token']
# oauth_verifier = request.GET['oauth_verifier']
# realm_id = request.GET['realmId']
#
# session = qbObject.get_access_tokens(oauth_verifier)
#
# # say you want access to the reports
#
# reportType = "ProfitAndLoss"
#
# url = "https://quickbooks.api.intuit.com/v3/company/asdfasdfas/"
# url += "reports/%s" % reportType
#
# r = session.request( #This is just a Rauth request
#     "POST",
#     url,
#     header_auth = True,
#     realm = realm_id,
#     params={"format":"json"}
#     )
#
# qb = QuickBooks(consumer_key = QB_OAUTH_CONSUMER_KEY,
#         consumer_secret = QB_OAUTH_CONSUMER_SECRET,
#         access_token = "Q0115083560322t85LAitprRk5Fb7ueVGAD8xSuS0bUHelYX2L",
#         access_token_secret = QB_ACCESS_TOKEN_SECRET,
#         company_id = "193514632414899"
#         )
#
# qbText = str(qb.query_objects(business_object, params, query_tail))
# #
# print qbText