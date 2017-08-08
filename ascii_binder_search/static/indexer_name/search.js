var distro_name;
var distro_name;
var es_url;
var index_name;

function preInit() {
    console.log("preInit called");
}


let onSearch = function(searchText) {
    return new Promise(function(resolve, reject) {
        resolve({});
    });
}

initPlugin(preInit, onSearch);