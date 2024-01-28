from os.path import dirname, basename, isfile, join
import glob
import importlib

# Encontra todos os arquivos .py no diretório, começando com 'F'
modulos = glob.glob(join(dirname(__file__), "F*.py"))

ignore = ['__init__.py', 'skew', 'Counter', 'kurtosis']

# Lista para armazenar as funções
functions = []

for f in modulos:
    if isfile(f):
        module_name = basename(f)[:-3]
        
        module = importlib.import_module('.' + module_name, package=__name__)

        for attribute_name in dir(module):
            attribute = getattr(module, attribute_name)
            if callable(attribute):
                if attribute.__name__ not in ignore:
                    functions.append(attribute)

functions = sorted(functions, key=lambda f: int(f.__name__[1:]))