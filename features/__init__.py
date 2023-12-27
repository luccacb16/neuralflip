from os.path import dirname, basename, isfile, join
import glob
import importlib

# Encontra todos os arquivos .py no diretório, começando com 'F'
modulos = glob.glob(join(dirname(__file__), "F*.py"))

# Lista para armazenar as funções
features_list = []

for f in modulos:
    if isfile(f) and not f.endswith('__init__.py') and not f.endswith('features_tests.py'):
        module_name = basename(f)[:-3]
        module = importlib.import_module('.' + module_name, package=__name__)

        # Itera sobre os atributos do módulo e coleta as funções
        for attribute_name in dir(module):
            attribute = getattr(module, attribute_name)
            if callable(attribute):
                features_list.append(attribute)

features_list = sorted(features_list, key=lambda f: int(f.__name__[1:]))