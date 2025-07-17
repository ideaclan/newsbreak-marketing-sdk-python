from newsbreak_marketing import Status
from newsbreak_marketing.ad import Ad, CreativeType
import strawberry
from typing import Optional, List
from schema import STAd

@strawberry.type
class SMAd:

    @strawberry.mutation
    async def create_ad(
        self,
        ad_account_id: strawberry.ID,
        ad_set_id: strawberry.ID,
        name: str,
        type: strawberry.enum(CreativeType),  # type: ignore
        headline: str,
        asset_url: str,
        description: str,
        call_to_action: str,
        brand_name: str,
        click_through_url: str,
        logo_url: Optional[str] = None,
        cover_url: Optional[str] = None,
        height: Optional[int] = None,
        width: Optional[int] = None,
        click_tracking_url: Optional[List[str]] = None,
        impression_tracking_url: Optional[List[str]] = None,
    ) -> STAd:
        #####################################################################################
        #####################################################################################
        ad = Ad(ad_account_id=ad_account_id, ad_set_id=ad_set_id)

        ad = await ad.create(
            name=name,
            type=CreativeType(type.value),  # type: ignore
            headline=headline,
            asset_url=asset_url,
            description=description,
            call_to_action=call_to_action,
            brand_name=brand_name,
            click_through_url=click_through_url,
            logo_url=logo_url,
            cover_url=cover_url,
            height=height,
            width=width,
            click_tracking_url=click_tracking_url,
            impression_tracking_url=impression_tracking_url
        )
        #####################################################################################
        #####################################################################################
        return STAd(
            id=ad.id,  # type: ignore
            name=ad.name,  # type: ignore
            campaign_id=ad.campaign_id,  # type: ignore
            click_tracking_url=ad.click_tracking_url,
            impression_tracking_url=ad.impression_tracking_url,
            status=ad.status,
            audit_status=ad.audit_status,
            status_txt=ad.status_txt,
            creative=ad.creative,  
            type=ad.type
        )
    
    @strawberry.mutation
    async def update_ad(
        self,
        ad_id: strawberry.ID,
        ad_account_id: strawberry.ID,
        ad_set_id: strawberry.ID,
        name: str,
        type: strawberry.enum(CreativeType),  # type: ignore
        headline: str,
        asset_url: str,
        description: str,
        call_to_action: str,
        brand_name: str,
        click_through_url: str,
        logo_url: Optional[str] = None,
        cover_url: Optional[str] = None,
        height: Optional[int] = None,
        width: Optional[int] = None,
        click_tracking_url: Optional[List[str]] = None,
        impression_tracking_url: Optional[List[str]] = None,
    ) -> STAd:
        #####################################################################################
        #####################################################################################
        ad = Ad(ad_account_id=ad_account_id, ad_set_id=ad_set_id)

        ad = await ad.update(
            ad_id=ad_id,
            name=name,
            type=CreativeType(type.value),  # type: ignore
            headline=headline,
            asset_url=asset_url,
            description=description,
            call_to_action=call_to_action,
            brand_name=brand_name,
            click_through_url=click_through_url,
            logo_url=logo_url,
            cover_url=cover_url,
            height=height,
            width=width,
            click_tracking_url=click_tracking_url,
            impression_tracking_url=impression_tracking_url
        )
        #####################################################################################
        #####################################################################################
        return STAd(
            id=ad.id,  # type: ignore
            name=ad.name,  # type: ignore
            campaign_id=ad.campaign_id,  # type: ignore
            click_tracking_url=ad.click_tracking_url,
            impression_tracking_url=ad.impression_tracking_url,
            status=ad.status,
            audit_status=ad.audit_status,
            status_txt=ad.status_txt,
            creative=ad.creative,  
            type=ad.type
        )

    @strawberry.mutation
    async def update_ad_status(
        self,
        ad_id: strawberry.ID,
        ad_account_id: strawberry.ID,
        ad_set_id: strawberry.ID,
        status: strawberry.enum(Status)  # type: ignore
    ) -> STAd:
        #####################################################################################
        #####################################################################################
        ad = Ad(ad_account_id=ad_account_id, ad_set_id=ad_set_id)

        ad = await ad.update_status(
            ad_id=ad_id,
            status=status
        )
        #####################################################################################
        #####################################################################################
        return STAd(
            id=ad.id,  # type: ignore
            name=ad.name,  # type: ignore
            campaign_id=ad.campaign_id,  # type: ignore
            click_tracking_url=ad.click_tracking_url,
            impression_tracking_url=ad.impression_tracking_url,
            status=ad.status,
            audit_status=ad.audit_status,
            status_txt=ad.status_txt,
            creative=ad.creative,  
            type=ad.type
        )
    
    @strawberry.mutation
    async def delete_ad(
        self,
        ad_id: strawberry.ID,
        ad_account_id: strawberry.ID,
        ad_set_id: strawberry.ID
    ) -> STAd:
        #####################################################################################
        #####################################################################################
        ad = Ad(ad_account_id=ad_account_id, ad_set_id=ad_set_id)

        ad = await ad.delete(ad_id=ad_id)
        #####################################################################################
        #####################################################################################
        return STAd(
            id=ad.id,  # type: ignore
            name=ad.name,  # type: ignore
            campaign_id=ad.campaign_id,  # type: ignore
            click_tracking_url=ad.click_tracking_url,
            impression_tracking_url=ad.impression_tracking_url,
            status=ad.status,
            audit_status=ad.audit_status,
            status_txt=ad.status_txt,
            creative=ad.creative,  
            type=ad.type
        )
    


@strawberry.type
class SQAd:
    @strawberry.field
    async def get_ad(
        self,
        ad_id: strawberry.ID,
        ad_account_id: strawberry.ID,
        ad_set_id: strawberry.ID
    ) -> STAd:
        #####################################################################################
        #####################################################################################
        ad = Ad(ad_account_id=ad_account_id, ad_set_id=ad_set_id)

        ad = await ad.get(ad_id=ad_id)
        #####################################################################################
        #####################################################################################
        return STAd(
            id=ad.id,  # type: ignore
            name=ad.name,  # type: ignore
            campaign_id=ad.campaign_id,  # type: ignore
            click_tracking_url=ad.click_tracking_url,
            impression_tracking_url=ad.impression_tracking_url,
            status=ad.status,
            audit_status=ad.audit_status,
            status_txt=ad.status_txt,
            creative=ad.creative,  
            type=ad.type
        )