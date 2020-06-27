import boto3
from botocore.exceptions import ClientError

def main():
    # make sure all emails mentioned are verified in ses, recipient as well if in sandbox
    # ensure credentials stored in ~/.aws/
    SENDER = "FirstName Lastname <sender email address between these arrows>"

    RECIPIENT = "recipient email address here"

    # CONFIGURATION_SET = "ConfigSet"

    AWS_REGION = "us-east-1"

    SUBJECT = "AWS SES TEST SDK FOR PYTHON"

    BODY_TEXT = ("Amazon SES Test (Python)\r\n"
             "This email was sent with Amazon SES using the "
             "AWS SDK for Python (Boto)."
        )
    
    # The HTML body of the email.
    BODY_HTML = """<html>
            <head></head>
            <body>
            <h1>Amazon SES Test (SDK for Python)</h1>
            <p>This email was sent with
                <a href='https://aws.amazon.com/ses/'>Amazon SES</a> using the
                <a href='https://aws.amazon.com/sdk-for-python/'>
                AWS SDK for Python (Boto)</a>.</p>
            </body>
            </html>
        """
    
    CHARSET = "UTF-8"

    client = boto3.client('ses', region_name=AWS_REGION)

    # Try to send the email.
    try:
        #Provide the contents of the email.
        response = client.send_email(
            Destination={
                'ToAddresses': [
                    RECIPIENT,
                ],
            },
            Message={
                'Body': {
                    'Html': {
                        'Charset': CHARSET,
                        'Data': BODY_HTML,
                    },
                    'Text': {
                        'Charset': CHARSET,
                        'Data': BODY_TEXT,
                    },
                },
                'Subject': {
                    'Charset': CHARSET,
                    'Data': SUBJECT,
                },
            },
            Source=SENDER,
            # If you are not using a configuration set, comment or delete the
            # following line
            # ConfigurationSetName=CONFIGURATION_SET,
        )
    # Display an error if something goes wrong.	
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        print("Email sent! Message ID:"),
        print(response['MessageId'])


if __name__ == "__main__":
    main()
    