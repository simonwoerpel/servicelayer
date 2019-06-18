import logging
from pkg_resources import iter_entry_points

log = logging.getLogger(__name__)
EXTENSIONS = {}


def get_entry_points(section):
    """Load all Python classes registered at a given entry point."""
    if section not in EXTENSIONS:
        EXTENSIONS[section] = {}
    if not EXTENSIONS[section]:
        for ep in iter_entry_points(section):
            try:
                EXTENSIONS[section][ep.name] = ep.load()
            except Exception:
                log.exception("Error loading: %s", ep.name)
    return EXTENSIONS[section]


def get_entry_point(section, name):
    return get_entry_points(section).get(name)


def get_extensions(section):
    """Iterate entry point objects."""
    return list(get_entry_points(section).values())
