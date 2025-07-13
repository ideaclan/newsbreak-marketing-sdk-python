from newsbreak_marketing.ad_set import Targeting, GenderType, Location, Gender
import strawberry
from pydantic import BaseModel, create_model
from typing import get_args, Union, get_origin, List, Optional
from enum import Enum
from dataclasses import make_dataclass, field, is_dataclass, fields as ff

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

# print(Targeting())

# def print_tree(cls):
#     if get_origin(cls) is list:
#         for arg in get_args(cls):
#             print('Found list')
#             print_tree(arg)

#     elif issubclass(cls, Enum):
#         print('Found enum')
#         for value in cls:
#             print('name ->', value.name)
#             print('value ->', value.value)
#             print('--------------------------------------------------------------------')

#     elif cls in (int,str,bool,float):
#         print('Found primitive')
#         print ('type ->', cls)

#     elif issubclass(cls, BaseModel):
#         print('Found model')
#         for key, value in cls.model_fields.items():
#             print('name ->', key)
#             print('type ->', value.annotation)
#             print('default ->',value.default)
#             print('--------------------------------------------------------------------')

#             print_tree(value.annotation)


#     else:
#         raise TypeError(f"Invalid input type: {type(cls)}")

        
# print_tree(Targeting)

def build_input(cls):
    if get_origin(cls) is list:
        arg = build_input(get_args(cls)[0])
        return List[arg]


    elif issubclass(cls, Enum):
        st_enum = strawberry.enum(cls)
        return st_enum

    elif cls in (int,str,bool,float):
        return cls

    elif issubclass(cls, BaseModel):
        fields = []
        for key, value in cls.model_fields.items():
            f = (key,)
            ty = build_input(value.annotation)
            f += (Optional[ty],)
            if value.default is not None:
                if get_origin(ty) is list:
                    default = value.default
                elif issubclass(ty,Enum):
                    default = ty(value.default.value)
                elif is_dataclass(ty):
                    default = ty(**(value.default.model_dump()))
                else:
                    default = value.default
            f += (field(default_factory=lambda: default),)
            
            fields.append(f)
            
        input = make_dataclass(cls.__name__, fields = fields)
        

        return strawberry.input(input)

    else:
        raise TypeError(f"Invalid input type: {type(cls)}")

tr = build_input(Targeting)
# tr = tr()
# print(tr.gender)
# # t = Targeting()
# print(t)


