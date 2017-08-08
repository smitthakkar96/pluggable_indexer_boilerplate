### Boilerplate for creating a custom indexer for ascii_binder_search_plugin

- Add appriporate information in setup.py and get started
- Rename indexer_name.py to appriporate name for indexer and make sure it is consistent accross the place.
- You can override methods index, parse_indexer_arguments, parse_html in your indexer class.
- In your search.js you must provide the implementation of preInit and onSearch method
- onSearch method must return the data via promise and you must make sure the data looks like below

``` javascript
{
   "topic_url":"",
   "title":"",
   "content":"",
   "site_name":""
}
```

- Deploy the plugin on pypi