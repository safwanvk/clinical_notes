from pydantic_settings import BaseSettings


class Settings(BaseSettings):
      POSTGRES_HOST: str
      POSTGRES_PORT: int
      POSTGRES_DB: str
      POSTGRES_USER: str
      POSTGRES_PASSWORD: str
      ENV: str = "development"

      @property
      def database_url(self):
            return (
                  f"postgresql+asyncpg://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}"
                  f"@{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"
            )

      class Config:
            env_file = ".env"


settings = Settings()