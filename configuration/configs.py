import os

from dynaconf import Dynaconf, Validator

current_dir: str = os.path.dirname(__file__)
root: str = os.path.abspath(
    os.path.join(
        current_dir,
        os.pardir,
    )
)

settings: Dynaconf = Dynaconf(
    root_path=root,
    envvar_prefix="IAHEMSCAN",
    settings_files=[
        "./configuration/settings.toml",
        "./configuration/.secrets.toml",
    ],
    environments=[
        "production",
        "development",
        "testing"
    ],
    env_switcher="IAHEMSCAN_APP_RUNNING_MODE",
    validators=[
        Validator(
            "APP_RUNNING_MODE",
            must_exist=True,
        )
    ],
    load_dotenv=False
)
