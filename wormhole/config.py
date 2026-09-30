import os
from wormhole.errors import CredentialError
from dataclasses import dataclass, field
from dotenv import load_dotenv
load_dotenv(".env")

PREFIX = "WORMHOLE_"

@dataclass
class Config:
    OPENSEARCH_HOST: str = os.getenv("WORMHOLE_OPENSEARCH_HOST", "")
    OPENSEARCH_USERNAME: str = os.getenv("WORMHOLE_OPENSEARCH_USERNAME", "")
    OPENSEARCH_PASSWORD: str = os.getenv("WORMHOLE_OPENSEARCH_PASSWORD", "")
    OPENSEARCH_PORT: int = int(os.getenv("WORMHOLE_OPENSEARCH_PORT", "9200"))

    # using this flag for local opensearch setup, since it will be in http
    USE_SSL: bool = bool(os.getenv("WORMHOLE_USE_SSL") == "true")

    def __post_init__(self):
        if not self.OPENSEARCH_HOST:
            raise CredentialError("OPENSEARCH_HOST is required")

        if not self.OPENSEARCH_USERNAME:
           raise CredentialError("OPENSEARCH_USERNAME is required")

        if not self.OPENSEARCH_USERNAME:
            raise CredentialError("OPENSEARCH_USERNAME is required")

config = Config()
