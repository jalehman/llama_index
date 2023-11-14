# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic

from ..core.datetime_utils import serialize_datetime
from .eval_llm_model_data import EvalLlmModelData
from .supported_eval_llm_model_names import SupportedEvalLlmModelNames


class SupportedEvalLlmModel(pydantic.BaseModel):
    """
    Response Schema for a supported eval LLM model.
    """

    name: SupportedEvalLlmModelNames = pydantic.Field(
        description="The name of the supported eval LLM model."
    )
    details: EvalLlmModelData = pydantic.Field(
        description="The details of the supported eval LLM model."
    )

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {
            "by_alias": True,
            "exclude_unset": True,
            **kwargs,
        }
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {
            "by_alias": True,
            "exclude_unset": True,
            **kwargs,
        }
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        smart_union = True
        json_encoders = {dt.datetime: serialize_datetime}
