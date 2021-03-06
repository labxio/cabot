
import os

CABOT_FROM_EMAIL = os.environ.get('CABOT_FROM_EMAIL')
GRAPHITE_API = os.environ.get('GRAPHITE_API')
GRAPHITE_USER = os.environ.get('GRAPHITE_USER')
GRAPHITE_PASS = os.environ.get('GRAPHITE_PASS')
JENKINS_API = os.environ.get('JENKINS_API')
JENKINS_USER = os.environ.get('JENKINS_USER')
JENKINS_PASS = os.environ.get('JENKINS_PASS')
HIPCHAT_ALERT_ROOM = os.environ.get('HIPCHAT_ALERT_ROOM')
HIPCHAT_API_KEY = os.environ.get('HIPCHAT_API_KEY')
HIPCHAT_URL = os.environ.get('HIPCHAT_URL')
SLACK_COMPANY_NAME = os.environ.get('SLACK_COMPANY_NAME')
SLACK_ALERT_ROOM = os.environ.get('SLACK_ALERT_ROOM')
SLACK_API_KEY = os.environ.get('SLACK_API_KEY')
SLACK_URL = os.environ.get('SLACK_URL')
TWILIO_ACCOUNT_SID = os.environ.get('TWILIO_ACCOUNT_SID')
TWILIO_AUTH_TOKEN = os.environ.get('TWILIO_AUTH_TOKEN')
TWILIO_OUTGOING_NUMBER = os.environ.get('TWILIO_OUTGOING_NUMBER')
CALENDAR_ICAL_URL = os.environ.get('CALENDAR_ICAL_URL')
WWW_HTTP_HOST = os.environ.get('WWW_HTTP_HOST')
WWW_SCHEME = os.environ.get('WWW_SCHEME', "https")
ALERT_INTERVAL = os.environ.get('ALERT_INTERVAL', 10)
NOTIFICATION_INTERVAL = os.environ.get('NOTIFICATION_INTERVAL', 120)
