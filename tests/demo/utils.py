from newsbreak_marketing.ad_set import Targeting, GenderType, Location
import strawberry
from pydantic import BaseModel
from typing import get_args, Union, get_origin
from enum import Enum
from dataclasses import make_dataclass

# def build_input(cls):
#     if issubclass(cls, BaseModel):
#         print(cls.model_fields)

#     else:
#         raise TypeError(f"Invalid input type: {type(cls)}")
    
# build_input(Targeting)

# for key, value in Targeting.model_fields.items():
#     print('name ->', key)
#     print('type ->', value.annotation)
#     print('default ->',value.default)
#     print('--------------------------------------------------------------------')

print(Targeting())