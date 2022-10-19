from errbot import BotPlugin, botcmd, webhook
import requests

class Coletor(BotPlugin):
    """
    This is a very basic plugin to try out your new installation and get you started.
    Feel free to tweak me to experiment with Errbot.
    You can find me in your init directory in the subdirectory plugins.
    """

    @botcmd  # flags a command
    def coletor(self, msg, args):  # a command callable with !tryme

        self.send(
            self.build_identifier("~town-square"), #Mattermost: ~ for channels; @ for users.
            "~~~ Boo! Bet you weren't expecting me, were you?",
        )

        return "o coletor"  # This string format is markdown.

    @botcmd
    def hello_card(self, msg, args):
        """Say a card in the chatroom."""
        self.send_card(title="Title",
                       body='text body to put in the card',
                       thumbnail='https://raw.githubusercontent.com/errbotio/errbot/master/docs/_static/errbot.png',
                       image='https://www.google.com/images/branding/googlelogo/2x/googlelogo_color_272x92dp.png',
                       link='http://www.google.com',
                       fields=(('First Key','Value1'), ('Second Key','Value2')),
                       color='red',
                       in_reply_to=msg)

    @webhook 
    def github_issues(self, payload):
        if type(payload) != str: 
            for room in self.rooms(): 
                self.send( 
                    self.build_identifier(f"~{room.name}"), 
                    'Title: Issue {0}!\n Issue URL:  {1}'.format(payload['action'], payload['issue']['url']),
                )

    @botcmd  # flags a command
    def test_post(self, msg, args):  # a command callable with !tryme

        url = 'https://botconforto.cloud.mattermost.com'
        myobj = {"channel_id":"~town-square", "message":"Test message #testing", "props":{"attachments": [{"pretext": "This is the attachment pretext.","text": "This is the attachment text."}]}}

        x = requests.post(url, json = myobj)

        print("<<< AQUI >>>")
        print(x.text)

        return "o coletor: https://forms.gle/TVAFsehZoxCpwt6k7"  # This string format is markdown.