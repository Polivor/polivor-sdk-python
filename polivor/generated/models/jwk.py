from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.jwk_use import JwkUse
from ..types import UNSET, Unset
from typing import cast
from typing import Literal, cast
import datetime






T = TypeVar("T", bound="Jwk")



@_attrs_define
class Jwk:
    """ 
        Attributes:
            kty (Literal['OKP']):
            crv (Literal['Ed25519']):
            x (str):
            kid (str):
            use (JwkUse):
            alg (Literal['EdDSA'] | Unset):
            revoked_at (datetime.datetime | None | Unset):
     """

    kty: Literal['OKP']
    crv: Literal['Ed25519']
    x: str
    kid: str
    use: JwkUse
    alg: Literal['EdDSA'] | Unset = UNSET
    revoked_at: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        kty = self.kty

        crv = self.crv

        x = self.x

        kid = self.kid

        use = self.use.value

        alg = self.alg

        revoked_at: None | str | Unset
        if isinstance(self.revoked_at, Unset):
            revoked_at = UNSET
        elif isinstance(self.revoked_at, datetime.datetime):
            revoked_at = self.revoked_at.isoformat()
        else:
            revoked_at = self.revoked_at


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "kty": kty,
            "crv": crv,
            "x": x,
            "kid": kid,
            "use": use,
        })
        if alg is not UNSET:
            field_dict["alg"] = alg
        if revoked_at is not UNSET:
            field_dict["revoked_at"] = revoked_at

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        kty = cast(Literal['OKP'] , d.pop("kty"))
        if kty != 'OKP':
            raise ValueError(f"kty must match const 'OKP', got '{kty}'")

        crv = cast(Literal['Ed25519'] , d.pop("crv"))
        if crv != 'Ed25519':
            raise ValueError(f"crv must match const 'Ed25519', got '{crv}'")

        x = d.pop("x")

        kid = d.pop("kid")

        use = JwkUse(d.pop("use"))




        alg = cast(Literal['EdDSA'] | Unset , d.pop("alg", UNSET))
        if alg != 'EdDSA'and not isinstance(alg, Unset):
            raise ValueError(f"alg must match const 'EdDSA', got '{alg}'")

        def _parse_revoked_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                revoked_at_type_0 = datetime.datetime.fromisoformat(data)



                return revoked_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        revoked_at = _parse_revoked_at(d.pop("revoked_at", UNSET))


        jwk = cls(
            kty=kty,
            crv=crv,
            x=x,
            kid=kid,
            use=use,
            alg=alg,
            revoked_at=revoked_at,
        )


        jwk.additional_properties = d
        return jwk

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
