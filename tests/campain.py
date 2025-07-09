import sys
if '/Users/sumansaurabh/IdeaClan/newsbreak_marketing/src' not in sys.path:
    sys.path.append('/Users/sumansaurabh/IdeaClan/newsbreak_marketing/src')

access_token = '3d8a7a49-bb3e-4201-b03b-29d0a1f3b348'
ad_account_id = '1942158153761857538'

from newsbreak_marketing import APISession

session = APISession(access_token=access_token)

from newsbreak_marketing.campaign import Campaign, CampaignObjective

camp = Campaign(ad_account_id=ad_account_id)

import asyncio

camp = asyncio.run(camp.create(name='testpy',objective=CampaignObjective.WEB_CONVERSION,ad_account_id=ad_account_id))