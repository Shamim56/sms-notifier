import boto3, yaml
from botocore.exceptions import ClientError


def read_yaml():
  """
  reads in the config file as a map

  return<Map>: a map of the configs.yml
  """
  data = None
  with open('config.yml') as f:
    data = yaml.load(f, Loader=yaml.FullLoader)
  return data


def main():
    config = read_yaml()
    client = boto3.client("sns",region_name="us-east-1")
    try:
        response = client.publish(
            PhoneNumber="+1xxxxxxxxxx!",
            Message="hwllo! This is a test message!"
        )
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        print('sms sent!')
        print(response)


if __name__ == '__main__':
    main()
