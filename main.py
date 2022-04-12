import os;import regex;import httpx; import json; import colorama; from colorama import Fore;from pystyle import Colors, Colorate;from datetime import datetime; import threading

threads = []

def __title__(title):
    os.system(
        'title ' + title
        )

def __DTI__(token):
    __amount__                          = sum(1 for line in open('tokens.txt'))
    __threads__                         = {len(threads)}
    __title__(f"DTI Using {__amount__} Tokens, {__threads__} Threads")
    with open('tokens.txt') as e:
        for line in e:
            _token                      =      line.strip('')
            _censorship                 =      regex.sub(r'[^.^-{10}$]', '*', _token) 
            _headers                    =      {'Authorization': _token}
    try:
        _api       = "https://discord.com/api/v9/users/@me/outbound-promotions/codes"
        _inventory =  httpx.get(
            _api,
            headers                     =      _headers)
        if 'code' in _inventory.text:
            codes                       =      json.loads(_inventory.text)
            for code in codes:
                _reset                  =      Fore.RESET
                _pink                   =      Fore.LIGHTMAGENTA_EX
                _sucess                 =      Fore.LIGHTGREEN_EX + "●" + _reset
                _now                    =      datetime.now()
                _currently              =      _now.strftime("%H:%M:%S")
                _code                   =      code['code']
                _title                  =      code['promotion']['outbound_title']
                print(_sucess, Colorate.Horizontal(Colors.blue_to_white, f"{_censorship} |  Code -> {_code} | {_title}", 1))
                with open('codes.txt', 'a') as f:
                    f.write(f"{_code} | {_title}\n")        
    except: pass

def __run__():
    for token in open('tokens.txt', 'r').readlines():
        threads.append(
            threading.Thread(
                target = __DTI__, 
            args = (
                token.strip(),
                )
                )
            )
    for x in threads: x.start()
    for x in threads: x.join()
    open('tokens.txt', 'r').close()

if __name__ == '__main__':
    __run__()
