import requests, urllib.parse
from colorama import Fore, Style

class Fuckvertise:
    def __init__(self, verbose = False):
        self.verbose = verbose
        self.datas = None
        self.url = 'https://api.bypass.vip/'
        self.session = requests.Session()
        self.session.headers['content-type'] = 'application/x-www-form-urlencoded;charset=UTF-8'
        self.results = []

    def load_from_txt(self, filename):
        if not filename.endswith('.txt'):
            raise ValueError('Wrong file format!')

        with open(filename, 'r') as f:
            self.datas = f.read().split()

    def get_direct_link(self, datas = None):
        if datas:
            self.datas = datas

        for data in self.datas:
            try:
                res = self.session.post(self.url, f'url={urllib.parse.quote(data)}').json()
            except Exception as e:
                raise e

            if self.verbose:
                if res['success']:
                    print(f"{Fore.GREEN}[SUCCESS]{Fore.YELLOW}[{res['time_ms']} ms]{Style.RESET_ALL} {res['query']} -> {res['destination']}")
                else:
                    print(f"{Fore.RED}[FAILED ]{Fore.YELLOW}[{res['time_ms']} ms]{Style.RESET_ALL} {res['query']} -> {res['response']}")

            self.results.append(res)

    def save_result(self, filename):
        s = ''
        failed = 0

        if not filename.endswith('.txt'):
            raise ValueError('Wrong file format!')

        for result in self.results:
            if result['destination']:
                s += f"{result['destination']}\n"
            else:
                failed += 1

        with open(f'{filename}', 'w') as outfile:
            outfile.write(s)

        if self.verbose:
            print(f'\n{len(self.results)} Total results | {len(self.results) - failed} Success | {failed} Failed')