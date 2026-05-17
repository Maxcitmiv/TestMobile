from pathlib import Path

from dotenv import dotenv_values


PROJECT_ROOT = Path(__file__).parent


class Config:
    def __init__(self, context: str):
        self.context = context
        self.env_path = PROJECT_ROOT / f".env.{context}"

        if not self.env_path.exists():
            raise FileNotFoundError(f"Config file not found: {self.env_path}")

        env = dotenv_values(self.env_path)

        self.remote_url = env["REMOTE_URL"]
        self.platform_name = env["PLATFORM_NAME"]
        self.automation_name = env["AUTOMATION_NAME"]
        self.device_name = env["DEVICE_NAME"]

        self.udid = env.get("UDID")
        self.platform_version = env.get("PLATFORM_VERSION")

        self.app = env.get("APP")
        self.app_package = env.get("APP_PACKAGE")
        self.app_activity = env.get("APP_ACTIVITY")

        self.no_reset = env.get("NO_RESET", "false").lower() == "true"
        self.full_reset = env.get("FULL_RESET", "false").lower() == "true"

        self.language = env.get("LANGUAGE", "en")
        self.locale = env.get("LOCALE", "US")

        self.bstack_user_name = env.get("BSTACK_USER_NAME")
        self.bstack_access_key = env.get("BSTACK_ACCESS_KEY")

    @property
    def app_path(self) -> str | None:
        if not self.app:
            return None

        if self.app.startswith("bs://"):
            return self.app

        return str(PROJECT_ROOT / self.app)