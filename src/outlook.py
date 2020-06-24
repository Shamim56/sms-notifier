from O365 import Account
import yaml


def read_yaml():
   """
   reads in the config file as a map

   return<Map>: a map of the configs.yml
   """
   data = None
   with open('../config.yml') as f:
      data = yaml.load(f, Loader=yaml.FullLoader)
   return data


def main():
   config = read_yaml()
   print(config["outlook"]["client_id"])
   credentials = (config["outlook"]["client_id"], config["outlook"]["secret_id"])
   account = Account(credentials)
   if account.authenticate(scopes=['https://graph.microsoft.com/Mail.Send']):
      print('Authenticated!')
      m = account.new_message()
      m.to.add(config["outlook"]["test_email"])
      m.subject = 'Testing!'
      m.body = "Culero Incorparated."
      m.send()


if __name__ == "__main__":
   main()
