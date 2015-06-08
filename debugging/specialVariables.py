'''
Created on 25 mar 2014

@author: Dominik


>>> dir(sys)  
['__displayhook__', '__doc__', '__excepthook__', '__name__', '__package__',
 '__stderr__', '__stdin__', '__stdout__', '_clear_type_cache',
 '_current_frames', '_getframe', '_mercurial', 'api_version', 'argv',
 'builtin_module_names', 'byteorder', 'call_tracing', 'callstats',
 'copyright', 'displayhook', 'dont_write_bytecode', 'exc_clear', 'exc_info',
 'exc_traceback', 'exc_type', 'exc_value', 'excepthook', 'exec_prefix',
 'executable', 'exit', 'flags', 'float_info', 'float_repr_style',
 'getcheckinterval', 'getdefaultencoding', 'getdlopenflags',
 'getfilesystemencoding', 'getobjects', 'getprofile', 'getrecursionlimit',
 'getrefcount', 'getsizeof', 'gettotalrefcount', 'gettrace', 'hexversion',
 'long_info', 'maxint', 'maxsize', 'maxunicode', 'meta_path', 'modules',
 'path', 'path_hooks', 'path_importer_cache', 'platform', 'prefix', 'ps1',
 'py3kwarning', 'setcheckinterval', 'setdlopenflags', 'setprofile',
 'setrecursionlimit', 'settrace', 'stderr', 'stdin', 'stdout', 'subversion',
 'version', 'version_info', 'warnoptions']
 
 
##### YOU SHOULDN'T OVERRIDE ANY BUILTIN VARIABLES/FUNCTIONS ##############
 
>>> import __builtin__
>>> dir(__builtin__)  
['ArithmeticError', 'AssertionError', 'AttributeError', 'BaseException',
 'BufferError', 'BytesWarning', 'DeprecationWarning', 'EOFError',
 'Ellipsis', 'EnvironmentError', 'Exception', 'False', 'FloatingPointError',
 'FutureWarning', 'GeneratorExit', 'IOError', 'ImportError', 'ImportWarning',
 'IndentationError', 'IndexError', 'KeyError', 'KeyboardInterrupt',
 'LookupError', 'MemoryError', 'NameError', 'None', 'NotImplemented',
 'NotImplementedError', 'OSError', 'OverflowError',
 'PendingDeprecationWarning', 'ReferenceError', 'RuntimeError',
 'RuntimeWarning', 'StandardError', 'StopIteration', 'SyntaxError',
 'SyntaxWarning', 'SystemError', 'SystemExit', 'TabError', 'True',
 'TypeError', 'UnboundLocalError', 'UnicodeDecodeError',
 'UnicodeEncodeError', 'UnicodeError', 'UnicodeTranslateError',
 'UnicodeWarning', 'UserWarning', 'ValueError', 'Warning',
 'ZeroDivisionError', '_', '__debug__', '__doc__', '__import__',
 '__name__', '__package__', 'abs', 'all', 'any', 'apply', 'basestring',
 'bin', 'bool', 'buffer', 'bytearray', 'bytes', 'callable', 'chr',
 'classmethod', 'cmp', 'coerce', 'compile', 'complex', 'copyright',
 'credits', 'delattr', 'dict', 'dir', 'divmod', 'enumerate', 'eval',
 'execfile', 'exit', 'file', 'filter', 'float', 'format', 'frozenset',
 'getattr', 'globals', 'hasattr', 'hash', 'help', 'hex', 'id', 'input',
 'int', 'intern', 'isinstance', 'issubclass', 'iter', 'len', 'license',
 'list', 'locals', 'long', 'map', 'max', 'memoryview', 'min', 'next',
 'object', 'oct', 'open', 'ord', 'pow', 'print', 'property', 'quit',
 'range', 'raw_input', 'reduce', 'reload', 'repr', 'reversed', 'round',
 'set', 'setattr', 'slice', 'sorted', 'staticmethod', 'str', 'sum', 'super',
 'tuple', 'type', 'unichr', 'unicode', 'vars', 'xrange', 'zip']
 

### TO INSPECT MODULES/OBJECTS USE FOLLOWING MODULE
>>> import inspect
>>> dir(inspect)
['ArgInfo', 'ArgSpec', 'Arguments', 'Attribute', 'BlockFinder', 'CO_GENERATOR', 'CO_NESTED', 'CO_NEWLOCALS', 
'CO_NOFREE', 'CO_OPTIMIZED', 'CO_VARARGS', 'CO_VARKEYWORDS', 'EndOfBlock', 'ModuleInfo', 
'TPFLAGS_IS_ABSTRACT', 'Traceback', '__author__', '__builtins__', '__date__', '__doc__', '__file__', 
'__name__', '__package__', '_filesbymodname', '_searchbases', 'attrgetter', 'classify_class_attrs', 
'cleandoc', 'currentframe', 'dis', 'findsource', 'formatargspec', 'formatargvalues', 'getabsfile', 
'getargs', 'getargspec', 'getargvalues', 'getblock', 'getcallargs', 'getclasstree', 'getcomments', 
'getdoc', 'getfile', 'getframeinfo', 'getinnerframes', 'getlineno', 'getmembers', 'getmodule', 
'getmoduleinfo', 'getmodulename', 'getmro', 'getouterframes', 'getsource', 'getsourcefile', 
'getsourcelines', 'imp', 'indentsize', 'isabstract', 'isbuiltin', 'isclass', 'iscode', 'isdatadescriptor', 
'isframe', 'isfunction', 'isgenerator', 'isgeneratorfunction', 'isgetsetdescriptor', 'ismemberdescriptor', 
'ismethod', 'ismethoddescriptor', 'ismodule', 'isroutine', 'istraceback', 'joinseq', 'linecache', 
'modulesbyfile', 'namedtuple', 'os', 're', 'stack', 'string', 'strseq', 'sys', 'tokenize', 'trace',
'types', 'walktree']



'''
