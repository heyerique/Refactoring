class ImportCommand:

    _file_type = None
    _file_name = None
    _file_types = '-csv', '-pk'
    _commands = []

    def __init__(self, line):
        self._commands = \
            list(command.lower() for command in str(line).split())

    @property
    def file_type(self):
        if self._commands[0] in self._file_types:
            self._file_type = self._commands[0][1:]
        return self._file_type

    @property
    def file_name(self):
        if len(self._commands) == 2:
            self._file_name = self._commands[1]
        return self._file_name
