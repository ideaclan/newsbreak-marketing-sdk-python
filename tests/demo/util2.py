from dataclasses import field, make_dataclass, fields, dataclass
from typing import Optional, List, get_args, get_origin, Union
from newsbreak_marketing.ad_set import Targeting, Gender, GenderType
from enum import Enum
import strawberry
from pydantic import BaseModel
from copy import deepcopy

def instance_model_to_dataclass(instance, dataclass_type):
    if dataclass_type in (int, str, float, bool):
        return instance
    if get_origin(dataclass_type) is list:
        arg = get_args(dataclass_type)[0]
        _instance = []
        for i in instance:
            _instance.append(instance_model_to_dataclass(i, arg))
        return _instance
    if get_origin(dataclass_type) is Union:
        return instance_model_to_dataclass(instance, get_args(dataclass_type)[0])
    if issubclass(dataclass_type, Enum):
        return dataclass_type(instance.value)
    if isinstance(instance, BaseModel):
        _data_fields = {f.name: f.type for f in fields(dataclass_type)}
        model_dump = instance.model_dump()
        data_dump = {}
        for var in model_dump:
            new_instance = instance_model_to_dataclass(model_dump[var], _data_fields[var])
            data_dump[var] = new_instance
        return dataclass_type(**data_dump)



def model_to_dataclass(model):
    if model in (int, str, float, bool):
        return model
    if get_origin(model) is list:
        item_type = get_args(model)[0]
        return List[model_to_dataclass(item_type)]
    if issubclass(model, Enum):
        return strawberry.enum(model)
    if issubclass(model, BaseModel):
        _fields = model.model_fields.items()
        _data_fields = []
        for name, _field_info in _fields:
            _field_type = _field_info.annotation
            _field_default = _field_info.default

            _new_field_type = model_to_dataclass(_field_type)

            if _field_default is not None:
                _new_default = instance_model_to_dataclass(_field_default, _new_field_type)
                _data_field = (name, Optional[_new_field_type], field(default_factory=lambda obj=_new_default: obj))
                # print(f"Field {name} with default {_field_default} converted to {_new_default}")
            else:
                _data_field = (name, _new_field_type)
            
            _data_fields.append(_data_field)
        return strawberry.input(make_dataclass(model.__name__, _data_fields))
    else:
        raise TypeError(f"{model} is not a valid Pydantic model or type for conversion to dataclass.")
    

tar = model_to_dataclass(Targeting)

from dataclasses import fields, MISSING, is_dataclass

def print_dataclass_fields_info(obj_or_cls):
    # Handle both class and instance
    if not is_dataclass(obj_or_cls):
        raise TypeError(f"{obj_or_cls} is not a dataclass class or instance.")

    cls = obj_or_cls if isinstance(obj_or_cls, type) else obj_or_cls.__class__

    print(f"Field info for dataclass '{cls.__name__}':")
    for f in fields(cls):
        name = f.name
        typ = f.type

        if isinstance(obj_or_cls, type):
            # working with class — just report default
            if f.default is not MISSING:
                default = f.default
            elif f.default_factory is not MISSING:
                try:
                    default = f.default_factory()
                except Exception as e:
                    default = f"<factory raised {e}>"
            else:
                default = "<no default>"
        else:
            # working with instance — get actual value
            default = getattr(obj_or_cls, name)

        print(f"  {name}: type={typ}, value={default}")

# print_dataclass_fields_info(tar)