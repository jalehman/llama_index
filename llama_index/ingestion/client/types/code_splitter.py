# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic

from ..core.datetime_utils import serialize_datetime


class CodeSplitter(pydantic.BaseModel):
    """
    Split code using a AST parser.

    Thank you to Kevin Lu / SweepAI for suggesting this elegant code splitting solution.
    https://docs.sweep.dev/blogs/chunking-2m-files
    """

    include_metadata: typing.Optional[bool] = pydantic.Field(
        description="Whether or not to consider metadata when splitting."
    )
    include_prev_next_rel: typing.Optional[bool] = pydantic.Field(
        description="Include prev/next node relationships."
    )
    callback_manager: typing.Optional[typing.Dict[str, typing.Any]]
    language: str = pydantic.Field(
        description="The programming language of the code being split."
    )
    chunk_lines: typing.Optional[int] = pydantic.Field(
        description="The number of lines to include in each chunk."
    )
    chunk_lines_overlap: typing.Optional[int] = pydantic.Field(
        description="How many lines of code each chunk overlaps with."
    )
    max_chars: typing.Optional[int] = pydantic.Field(
        description="Maximum number of characters per chunk."
    )
    class_name: typing.Optional[str]

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
