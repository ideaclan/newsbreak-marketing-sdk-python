# Newsbreak Marketing SDK (Python)

A modern, fully asynchronous Python SDK for the Newsbreak Marketing API. This library provides a convenient, modular, and async interface for managing campaigns, ad sets, ads, and asset uploads on the Newsbreak platform.

---

## Features

- **Async API**: All API calls are asynchronous for high-performance and scalable integrations.
- **Modular**: Separate modules for campaigns, ad sets, ads, and asset management.
- **GraphQL Ready**: Designed for use with Strawberry GraphQL, but can be used directly.
- **Extensible**: Easily extend or customize for your own use cases.

---

## Installation

Install via [Poetry](https://python-poetry.org/) (recommended):

```bash
poetry add newsbreak_marketing
```

Or via pip:

```bash
pip install newsbreak_marketing
```

---

## Project Structure

```
src/newsbreak_marketing/
    campaign/        # Campaign management
    ad_set/          # Ad set management
    ad/              # Ad management & asset upload
    core/            # Core utilities and schemas
    utils/           # API request utilities
    exceptions/      # Custom exceptions
```

---

## Quick Start

### 1. API Session

```python
from newsbreak_marketing import APISession

session = APISession(access_token="YOUR_ACCESS_TOKEN")
```

---

## Campaign Management

### Create, Update, Delete, and Query Campaigns

```python
from newsbreak_marketing.campaign import Campaign, CampaignObjective

campaign = Campaign(ad_account_id="ACCOUNT_ID")

# Create
created = await campaign.create(
    name="Test Campaign",
    objective=CampaignObjective.TRAFFIC
)

# Update
updated = await campaign.update(
    campaign_id=created.id,
    name="Updated Campaign"
)

# Update Status
await campaign.update_status(
    campaign_id=created.id,
    status="PAUSED"
)

# Delete
await campaign.delete(campaign_id=created.id)

# Get
fetched = await campaign.get(campaign_id=created.id)
```

---

## Ad Set Management

### Create, Update, Delete, and Query Ad Sets

```python
from newsbreak_marketing.ad_set import AdSet, AdSetBudgetType, AdSetBidType, AdSetDeliveryRate, Targeting

ad_set = AdSet(ad_account_id="ACCOUNT_ID", campaign_id="CAMPAIGN_ID")

# Create
created = await ad_set.create(
    name="Test AdSet",
    budget_type=AdSetBudgetType.DAILY,
    budget=1000,
    start_time=START_TIMESTAMP,
    end_time=END_TIMESTAMP,
    bid_type=AdSetBidType.CPC,
    bit_rate=100,
    delivery_rate=AdSetDeliveryRate.STANDARD,
    tracking_id="TRACKING_ID",
    targeting=Targeting(...),
    optimization=True
)

# Update
updated = await ad_set.update(
    ad_set_id=created.id,
    name="Updated AdSet",
    # ...other params
)

# Update Status
await ad_set.update_status(
    ad_set_id=created.id,
    status="PAUSED"
)

# Delete
await ad_set.delete(ad_set_id=created.id)

# Get
fetched = await ad_set.get(ad_set_id=created.id)
```

---

## Ad Management

### Create, Update, Delete, and Query Ads

```python
from newsbreak_marketing.ad import Ad, CreativeType

ad = Ad(ad_account_id="ACCOUNT_ID", ad_set_id="AD_SET_ID")

# Create
created = await ad.create(
    name="Test Ad",
    type=CreativeType.IMAGE,
    headline="Headline",
    asset_url="https://...",
    description="Description",
    call_to_action="LEARN_MORE",
    brand_name="Brand",
    click_through_url="https://...",
    # ...other optional params
)

# Update
updated = await ad.update(
    ad_id=created.id,
    name="Updated Ad",
    # ...other params
)

# Update Status
await ad.update_status(
    ad_id=created.id,
    status="PAUSED"
)

# Delete
await ad.delete(ad_id=created.id)

# Get
fetched = await ad.get(ad_id=created.id)
```

---

## Asset Upload

### Uploading Ad Assets

```python
import io
from newsbreak_marketing.ad.asset import upload

with open("path/to/image.jpg", "rb") as f:
    asset_url = await upload(session, ad_account_id="ACCOUNT_ID", media=f)
    print("Uploaded asset URL:", asset_url)
```

---

## Demo & Examples

See the [`tests/demo/`](./tests/demo/) directory for end-to-end examples:

- `main.py`: Full GraphQL API demo using Strawberry and Starlette.
- `campaign.py`: Campaign operations.
- `ad_set.py`: Ad set operations.
- `ad.py`: Ad operations.
- `util2.py`: Utilities for dataclass and schema conversion.

---

## Requirements

- Python 3.8+
- [httpx](https://www.python-httpx.org/) (for async HTTP requests)
- [pydantic](https://pydantic-docs.helpmanual.io/) (for data validation)
- [strawberry-graphql](https://strawberry.rocks/) (for GraphQL integration, optional)
- [starlette](https://www.starlette.io/) (for API server, optional)

---

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/my-feature`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature/my-feature`)
5. Create a new Pull Request

---

## License

[MIT License](./LICENSE)

---

## Contact

For questions, issues, or feature requests, please open an issue on GitHub or contact the maintainer.