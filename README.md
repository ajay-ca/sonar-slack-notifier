# SonarQube Analysis Report to Slack

This is a Flask application that receives webhook events from SonarQube and sends analysis reports to a specified Slack channel.

## Preview

<img src="https://github.com/ajay-ca/sonar-slack-notifier/assets/87013178/1e818cd5-a440-4d85-9c70-e565e664d13a" align="left" width="450">&nbsp;&nbsp;
<img src="https://github.com/ajay-ca/sonar-slack-notifier/assets/87013178/933a060b-4af4-4aab-a914-9511fa547fc6" align="middle" width="450">&nbsp;&nbsp;
<br /> 

## Requirements
- Python 3.7+
- Flask
- requests
- python-dateutil

**NOTE:** If you are getting `Command 'python' not found`, then use `python3` instead of `python` or alias the same in your **bashrc** file

## Installation

1. Clone the repository:

```bash
git clone https://github.com/ajay-ca/sonar-slack-notifier.git
cd sonar-slack-notifier
```
2. Create and activate a virtual environment:

```
python -m venv .
source bin/activate  # On Windows, use `venv\Scripts\activate`
```

3. Install the dependencies:

```
pip install -r requirements.txt
```

## Configuration
Before running the application, you need to provide your [Slack webhook URL](https://slack.com/apps/A0F7XDUAZ-incoming-webhooks?tab=more_info). The application will prompt you to enter this URL when it starts.

## Running the Application
To start the Flask application, run:

```
python app.py
```

## Usage
1. Set up a webhook in SonarQube through ***Administration -> Configuration -> Webhooks***. Click on **Create** button and provide a name along with the URL or the *ip_address:port* of your server.
   ![image](https://github.com/ajay-ca/sonar-slack-notifier/assets/87013178/fb17de46-ab45-4d1c-a4b7-116bc9d32fdd)

3. The application will process the incoming webhook events and send formatted messages to the Slack channel.

## Example Payload
Here is an example of the JSON payload that the application expects from SonarQube:

```
{
  "serverUrl": "https://sonarqube.com",
  "taskId": "AZasdpSq4yMhHqU3334gm",
  "status": "SUCCESS",
  "analysedAt": "2024-06-24T05:07:48+0000",
  "revision": "2bb759eb7fd6161882cb1efdd637ef1d71ef6c68",
  "changedAt": "2024-06-24T05:07:48+0000",
  "project": {
    "key": "new-python-key",
    "name": "new-python-name",
    "url": "https://sonarqube.com/dashboard?id=new-python-key"
  },
  "branch": {
    "name": "main",
    "type": "BRANCH",
    "isMain": true,
    "url": "https://sonarqube.gewaninfotech.com/dashboard?id=new-python-key"
  },
  "qualityGate": {
    "name": "Python",
    "status": "OK",
    "conditions": [
      {
        "metric": "new_reliability_rating",
        "operator": "GREATER_THAN",
        "value": "1",
        "status": "OK",
        "errorThreshold": "1"
      },
      {
        "metric": "new_security_rating",
        "operator": "GREATER_THAN",
        "value": "1",
        "status": "OK",
        "errorThreshold": "1"
      },
      {
        "metric": "security_rating",
        "operator": "GREATER_THAN",
        "value": "1",
        "status": "OK",
        "errorThreshold": "1"
      },
      {
        "metric": "new_maintainability_rating",
        "operator": "GREATER_THAN",
        "value": "1",
        "status": "OK",
        "errorThreshold": "1"
      },
      {
        "metric": "new_coverage",
        "operator": "LESS_THAN",
        "value": "0.0",
        "status": "OK",
        "errorThreshold": "0"
      },
      {
        "metric": "new_duplicated_lines_density",
        "operator": "GREATER_THAN",
        "value": "1.52555",
        "status": "OK",
        "errorThreshold": "20"
      },
      {
        "metric": "blocker_violations",
        "operator": "GREATER_THAN",
        "value": "0",
        "status": "OK",
        "errorThreshold": "0"
      },
      {
        "metric": "code_smells",
        "operator": "GREATER_THAN",
        "value": "0",
        "status": "OK",
        "errorThreshold": "0"
      },
      {
        "metric": "critical_violations",
        "operator": "GREATER_THAN",
        "value": "0",
        "status": "OK",
        "errorThreshold": "0"
      },
      {
        "metric": "major_violations",
        "operator": "GREATER_THAN",
        "value": "0",
        "status": "OK",
        "errorThreshold": "0"
      },
      {
        "metric": "new_blocker_violations",
        "operator": "GREATER_THAN",
        "value": "0",
        "status": "OK",
        "errorThreshold": "0"
      },
      {
        "metric": "new_bugs",
        "operator": "GREATER_THAN",
        "value": "0",
        "status": "OK",
        "errorThreshold": "0"
      },
      {
        "metric": "new_major_violations",
        "operator": "GREATER_THAN",
        "value": "0",
        "status": "OK",
        "errorThreshold": "0"
      },
      {
        "metric": "new_minor_violations",
        "operator": "GREATER_THAN",
        "value": "0",
        "status": "OK",
        "errorThreshold": "10"
      },
      {
        "metric": "new_security_hotspots_reviewed",
        "operator": "LESS_THAN",
        "status": "NO_VALUE",
        "errorThreshold": "0"
      },
      {
        "metric": "tests",
        "operator": "LESS_THAN",
        "value": "1",
        "status": "OK",
        "errorThreshold": "0"
      },
      {
        "metric": "vulnerabilities",
        "operator": "GREATER_THAN",
        "value": "0",
        "status": "OK",
        "errorThreshold": "0"
      }
    ]
  },
  "properties": {
    "sonar.analysis.detectedscm": "git",
    "sonar.analysis.detectedci": "Github Actions"
  }
}
```
## Extracted Fields
Here is the list of the extracted fields from the payload

- project.name
- project.key
- quality_gate.status
- branch.name

## License
This project is licensed under the MIT License. See the [LICENSE](https://github.com/ajay-ca/sonar-slack-notifier?tab=MIT-1-ov-file#MIT-1-ov-file) file for details.

