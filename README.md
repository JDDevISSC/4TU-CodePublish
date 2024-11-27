# 4TU-CodePublish
Docker image to make publishing code to 4TU.ResearchData easy

## Development Setup

### Checkout code
Git clone the repository

### setup (once) and activate  virtual environment
In repository directory:
```
python -m venv venv
. ./venv/bin/activate
```

### Install build tools

```
pip install --upgrade pip
pip install setuptools setuptools-scm build
```

### Build module from source

```
./module_build.sh
```

### Install latest build module
```
./module_install.sh
```

### Environment variables
Either make sure you have a .env file in your project directory that supplies that necessary configuration or supply them using environment variables.

#### Example .env
```
4TU_API_TOKEN="my-4tu-api-token"
4TU_BASE_URL="https://data.4tu.nl"
4TU_LOG_LEVEL="INFO"
4TU_LOG_FILE="/path/to/4TU-CODEPUBLISH.log"
```

### Try the installed module

Start the publish process:
```
4tu-codepublish
```

Or start the metadata creation funnel:
```
4tu-codepublish --create
```