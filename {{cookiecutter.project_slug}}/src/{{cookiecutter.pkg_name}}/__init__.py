# version determination

# original Hatchlor version
# from importlib.metadata import PackageNotFoundError, version
# try:
#     __version__ = version('{{ cookiecutter.project_slug }}')
# except PackageNotFoundError:  # pragma: no cover
#     __version__ = 'unknown'
# finally:
#     del version, PackageNotFoundError

# latest import requirement for hatch-vcs-footgun-example
from {{ cookiecutter.pkg_name }}.version import __version__
