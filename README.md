# 4TU-CodePublish
Docker image to make publishing code to 4TU.ResearchData easy

## Setup
Either make sure you have a .env file in your project directory that supplies that necessary configuration or supply them using environment variables.

### Example .env
```
4TU_API_TOKEN="my-4tu-api-token"
4TU_BASE_URL="https://data.4tu.nl"
4TU_LOG_LEVEL="INFO"
4TU_LOG_FILE="/path/to/4TU-CODEPUBLISH.log"
```