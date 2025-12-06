document.addEventListener('DOMContentLoaded', () => {
    const input = document.getElementById('searchbar');
    const searchButton = document.getElementById('searchButton');
    const output = document.getElementById('displayContainer');

    let currentController = null;

    async function doSearch() {
        const query = input.value.trim();
        if(!query){return;}

        if(currentController) {currentController.abort();}
        currentController = new AbortController();
        const signal  = currentController.signal;

        const url = `/search?q=${encodeURIComponent(query)}`;

        try{
            const resp = await fetch(url);
            if(!resp.ok){
                output.innerHTML = `<div> Error: ${resp.status}</div>`;
                return;
            }
            const data = await resp.text();
            output.innerHTML = data;
        } catch(err) {
            console.error(err);
        } finally {
            currentController = null;
        }
    }

    async function doSearchAPI() {
        const query = input.value.trim();
        if(!query){return;}

        // abort if new query is entered
        if(currentController) {currentController.abort();}
        currentController = new AbortController();
        const signal  = currentController.signal;

        output.innerHTML = '<div>Searching...</div>';

        const url = `/api/search?q=${encodeURIComponent(query)}`;

        try {
            const resp = await fetch(url, { method: 'GET', signal});
            if(!resp.ok){
                
                output.innerHTML = `<div> Error: ${resp.status}</div>`;
                return;
            }
            const data = await resp.json();
            // use results if possible, otherwise return empty array
            const results = (data.results || []).map(result => {
                // get title and lyrics, otherwise defaults
                const title = result.title || 'Untitled';
                const snippet = result.lyrics || '';
                return `<div>${title}</div> <div>${snippet}</div>`;
            });
            // if any results: join them together. else: display no results
            // replace this with createElement once I have DOM elements for songs
            output.innerHTML = results.length ? results.join('') : '<div>No results</div>';
        } catch(err) { 
            // ignore if request was aborted
            if(err.name === 'AbortError'){
                return;
            }
            console.error(err);
            output.innerHTML = '<div> Internal error </div>';
        } finally {
            currentController = null; 
        }
    }

    searchButton.addEventListener('click', doSearch);
    input.addEventListener('keydown', e => {
        if(e.key === 'Enter'){
            doSearch();
        }
    });

})