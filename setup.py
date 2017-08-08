from setuptools import setup


setup(
    name="<give a meaning full name to the indexer>",
    version="0.0.1",
    author="<author_name>",
    author_email="author_email",
    description=("<add some description>"),
    packages=[
                'ascii_binder_search',
                'ascii_binder_search.indexers',
            ],
    license="BSD",
    keywords="Asciibinder, ascii_binder_search, ascii_binder_search_<name_of_indexer>",
    url="<link_to_git_repo>",
    install_requires=[],
    include_package_data=True,
    zip_safe=False,
    namespaces=[
        'ascii_binder_search.indexers'
    ],
)