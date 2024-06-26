import requests
from flask import Flask, request, jsonify
from datetime import datetime
from dateutil import parser

app = Flask(__name__)

# Replace with your Slack webhook URL
slack_webhook_url = 'https://<slack-webhook-url>'

def send_to_slack(payload):
    try:
        response = requests.post(slack_webhook_url, json=payload)
        response.raise_for_status()
        print(f"Message sent to Slack. Response: {response.status_code}, {response.text}")
    except requests.exceptions.RequestException as e:
        print(f"Failed to send message to Slack: {str(e)}")

@app.route('/', methods=['POST'])
def handle_webhook():
    if request.method == 'POST':
        try:
            data = request.get_json()
            if data:
                project_key = data.get('project', {}).get('key')
                project_name = data.get('project', {}).get('name')
                project_url = data.get('project', {}).get('url')
                branch_name = data.get('branch', {}).get('name')
                quality_gate_status = data.get('qualityGate', {}).get('status')
                # analysed_at = data.get('analysedAt')

                # # Parse the analysedAt value to extract the time in hh:mm format
                # analysed_time = datetime.fromisoformat(analysed_at).strftime('%H:%M')
                
                # Set color based on quality gate status
                color = "#FFFF00"  # Default color
                if quality_gate_status == "OK":
                    color = "#00FF00"  # Green for OK
                else:
                    color = "#FF0000"  # Red for others

                # Construct Slack message payload
                slack_message = {
                    "blocks": [
                        {
                            "type": "header",
                            "text": {
                                "type": "plain_text",
                                "text": ":mag: SonarQube Analysis Report",
                                "emoji": True
                            }
                        },
                        {
                            "type": "divider"
                        }
                    ],
                    "attachments": [
                        {
                            "color": color,
                            "fields": [
                                {
                                    "title": "*Project Name:*",
                                    "value": project_name,
                                    "short": True
                                },
                                {
                                    "title": "*Project Key:*",
                                    "value": project_key,
                                    "short": True
                                },
                                {
                                    "title": "*Status:*",
                                    "value": quality_gate_status,
                                    "short": True
                                },
                                {
                                    "title": "*Branch:*",
                                    "value": branch_name,
                                    "short": True
                                }
                                # {
                                #     "title": "*Time Analyzed:*",
                                #     "value": analysed_time,
                                #     "short": True
                                # }
                            ],
                            "footer": f"<{project_url} |SonarQube Dashboard>",
                            "ts": datetime.now().timestamp()
                        }
                    ]
                }

                # Send message to Slack
                send_to_slack(slack_message)

                return jsonify({'message': 'Received and processed JSON payload.'}), 200
            else:
                return jsonify({'error': 'No JSON data received.'}), 400
        except Exception as e:
            return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run()
