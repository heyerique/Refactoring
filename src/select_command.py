class SelectCommand:

    _resource_type = None
    _create_file = False
    _file_name = None
    _resource_types = '-csv', '-db'
    _create_file_keyword = '-a'
    _commands = []

    default_csv_file = 'staffinfo.csv'

    def __init__(self, line):
        self._commands = \
            list(command.lower() for command in str(line).split())

    @property
    def resource_type(self):
        if self._commands[0] in self._resource_types:
            self._resource_type = self._commands[0][1:]
        return self._resource_type

    @property
    def create_file(self):
        if len(self._commands) == 3 \
                and self._commands[1] == self._create_file_keyword:
            self._create_file = True
        return self._create_file

    @property
    def file_name(self):
        if len(self._commands) == 2:
            self._file_name = self._commands[1]
        if len(self._commands) == 3:
            self._file_name = self._commands[2]
        return self._file_name
