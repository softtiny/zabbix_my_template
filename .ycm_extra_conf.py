import os


if "PYTHONPATH" in os.environ:
    os.environ['PYTHONPATH'] = f'.:{os.environ["PYTHONON"]}'
else:
    os.environ['PYTHONPATH'] = '.'
