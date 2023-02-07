import ui
import requests as rq


class Paste:
    API_URL = "https://pastebin.com/api/api_post.php"

    def __init__(self, api_dev_key, file) -> None:
        self.dev_key = api_dev_key
        self._file = file

        self.file = ''
        self.filename = ''

    def validate(self):
        try:
            self.file = open(self._file, 'r')
            self.filename = str(self._file)
        except FileNotFoundError:
            print(ui.nor, 'file not found!. specify your file with -f.')
            exit(1)

    def request(self):
        self.validate()
        data = {
            'api_dev_key': (None, self.dev_key),
            'api_option': (None, 'paste'),
            'api_paste_code': (None, self.file),
            'api_paste_name': (None, self.filename),
        }
        res = rq.post(self.API_URL, files=data)
        content = res.content.decode('utf-8')

        if content.endswith('invalid api_dev_key'):
            print(ui.nor, 'invalid api key!. specify your key with -k.')
            print(ui.nor, 'if you have no idea what the key is, try use plain -h.')
        if content.startswith('https'):
            print(ui.okg, 'file submited! here\'s your code:',
                  ui.c.B, ui.c.WARN, content.split('/')[3], ui.c.RES)


def read(args):
    print(ui.okg, 'here you go!')
    API_URL = 'https://pastebin.com/raw/'
    res = rq.get(API_URL + args.get)
    print(res.text)
