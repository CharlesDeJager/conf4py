from typing import Optional

from pydantic import (
    BaseModel,
    ConfigDict,
)

from pydantic_settings import (
    BaseSettings,
    PydanticBaseSettingsSource,
    SettingsConfigDict,
    JsonConfigSettingsSource,
)


class ProfiseeSetting(BaseModel):
    profisee_url: str = None
    client_id: str = None
    model_config = ConfigDict()


class LibreTranslateSetting(BaseModel):
    server_url: str = None
    api_key: Optional[str] = None
    model_config = ConfigDict()


class Settings(BaseModel):
    default: str = None
    development: ProfiseeSetting = None
    sandbox: ProfiseeSetting = None
    libreTranslate: LibreTranslateSetting = None
    model_config = ConfigDict()


class Config(BaseSettings):
    # default: str
    # profisee_url: str
    # client_id: str
    # libretranslate_url: str
    # api_key: str

    # # to override domains:
    # # export my_prefix_domains='["foo.com", "bar.com"]'
    # domains: set[str] = set()

    # # to override more_settings:
    # # export my_prefix_more_settings='{"foo": "x", "apple": 1}'
    # more_settings: SubModel = SubModel()
    settings: Settings = Settings()
    # default: str = None
    # Annotated[int | None, Field(deprecated=True)] = None
    # development: Annotated[ProfiseeSetting | None, Field(default=None)] = None
    # sandbox: Annotated[ProfiseeSetting | None, Field(default=None)] = None
    # production: Annotated[ProfiseeSetting | None, Field(default=None)] = None
    # libreTranslate: LibreTranslateSetting = None

    model_config = SettingsConfigDict(
        json_file="appsettings.json",
        extra="allow",
        from_attributes=True,
        title="Profisee Translate Settings",
        populate_by_name=True,
    )

    @classmethod
    def settings_customise_sources(
        cls,
        settings_cls: type[BaseSettings],
        init_settings: PydanticBaseSettingsSource,
        env_settings: PydanticBaseSettingsSource,
        dotenv_settings: PydanticBaseSettingsSource,
        file_secret_settings: PydanticBaseSettingsSource,
    ) -> tuple[PydanticBaseSettingsSource, ...]:
        return (JsonConfigSettingsSource(settings_cls),)


s: Config = Config().settings
