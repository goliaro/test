class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def print_color(text, color):
    print(f"{color}{text}{bcolors.ENDC}")


print_color("Test text in color...", bcolors.HEADER)
print_color("Test text in color...", bcolors.OKBLUE)
print_color("Test text in color...", bcolors.OKCYAN)
print_color("Test text in color...", bcolors.OKGREEN)
print_color("Test text in color...", bcolors.WARNING)
print_color("Test text in color...", bcolors.FAIL)
print_color("Test text in color...", bcolors.BOLD)
