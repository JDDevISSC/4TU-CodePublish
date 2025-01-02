# 4TU-CodePublish
Docker image to make publishing code to 4TU.ResearchData easy

## Usage
The main usages of 4TU-CodePublish consist of two features, namely:
- Creating a metadata file in JSON format.
- Publishing a GIT repository using said metadata file. (⚠️ NOTE: This feature is still under construction and does not work at the time of writing.⚠️)

### Prerequisites
Make sure the following prerequisites are met:
- A terminal supporting sh (Shell Command Language).
- Python >=3.8, pip and curl
- Setup an account at https://data.4tu.nl and create an API token.
- The repository with the code you want to publish has a .env file as such:
```
4TU_API_TOKEN="my-4tu-api-token"
4TU_BASE_URL="https://data.4tu.nl"
4TU_LOG_LEVEL="INFO"
4TU_LOG_FILE="./4TU-CODEPUBLISH.log"
4TU_OUTPUT_FILE="./metadata.json"
```
Note that you might not want to include the 4TU_API_TOKEN into your repository. It is highly recommended to remove the API token from the .env file after creating a metadata file. Define the 4TU_API_TOKEN environment variable as a CI/CD variable, such as the [GitLab CI/CD variables](https://docs.gitlab.com/ee/ci/variables/#define-a-cicd-variable-in-the-ui).

### Install latest 4TU-CodePublish
Install the wheel from the latest 4TU-CodePublish release:
```
pip install $(curl -s https://api.github.com/repos/JDDevISSC/4TU-CodePublish/releases/latest \
| grep "browser_download_url" \
| grep ".whl" \
| cut -d '"' -f 4)
```

### Creating a metadata file
After installing we can use 4TU-CodePublish to create a metadata file like such:

```
4tu-codepublish --create
```
This will start the metadata creation funnel after which a *metadata.json* file is generated in the specified location. Commit this file into your repository together with the project for which you want to publish the metadata. This will ensure you can publish new versions of your project with all the necessary metadata.

### Setup a GitLab pipeline for automatic publication to 4TU

⚠️ NOTE: This feature is still under construction and does not work at the time of writing.⚠️

Now that we have a metadata file in our repository we can use a GitLab CI/CD pipeline configuration file such as the example below to configure a pipeline that automatically publishes to 4TU.ResearchData including the metadata from the file that we generated. 

Please note that you can configure your GitLab CI/CD pipelines in any way you want. You might want to automatically publish your code when:
- Your code is pushed to a certain branch.
- A tag is pushed to GitLab.
- A button in the GitLab UI is pressed.

#### Example .gitlab-ci.yml
```

stages:          # List of stages for jobs, and their order of execution
  - publish

publish-job:       # This job runs in the publish stage, which runs first.
  stage: publish
  image: 
    name: ghcr.io/jddevissc/4tu-codepublish:latest
```

## Development Setup
### setup and activate  virtual environment
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
### Create a new release
Creating a new release is as simple as push a new (SEMVER based) tag on a commit on the main branch. After the tag is pushed onto the main branch you can create a new release on the repository page by *Drafting a new release* and selecting the desired tag. Use *4TU-CodePublish major.minor.patch* as the *Release title*. The release description isn't necesary for now, although in the future it should contain atleast a changelog. 

Creating the release should trigger Github Actions that will build the module artifacts and add them to the release. Furthermore a Github Action will run that will build and push a Docker image to the repo's container registry as a *Package* that can be accessed at the repository page under *Packages* and by external systems such as GitLab Runners as examplified in the pipeline_examples directory.


## Future development
### Publishing feature
For now development of 4TU-CodePublish is dependent on the development of [Djehuty](https://github.com/4TUResearchData/djehuty), the software that makes up 4TU.ResearchData. For now there are talks to add API support for aquiring the url of the internal 4TUResearchData .git repository related to the dataset which acts as a temporary GIT remote. This will make it possible to automatically push code to 4TU from a diverse set of environments.

### Support for embargoed access and restricted access
For now only Open access publications are supported.

### Support for GitHub Actions / BitBucket / etc
Since 4TU-CodePublish uses a docker container for packaging, it is quite easy to support other code collaboration platforms such as GitHub and BitBucket. For now we want to see how the GitLab workflow works for researchers to be able to iterate on the functionality.

### Support for more metadata
For now only the required metadata is supported in the metadata funnel because of resource constraints. Please feel free to add more metadata support though pull requests.