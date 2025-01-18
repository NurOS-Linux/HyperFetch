import platform
from colorama import Fore, Style

def get_architecture_info():
    """
    Возвращает информацию о архитектуре системы.
    """
    architecture = platform.architecture()
    machine = platform.machine()
    
    return {
        'architecture': architecture,
        'machine': machine,
    }

def run():
    info = get_architecture_info()
    print(f'{Fore.GREEN}Architecture:{Style.RESET_ALL} {info["architecture"][0]}')
    print(f'{Fore.GREEN}Machine:{Style.RESET_ALL} {info["machine"]}')