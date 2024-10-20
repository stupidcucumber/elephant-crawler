from dataclasses import dataclass


@dataclass
class Connection:
    host: str
    port: str

    def buildURL(self, endpoint: str | None = None) -> str:
        return f"{self.host}:{self.port}" + endpoint if endpoint else ""
