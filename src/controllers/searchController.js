const Album = require('../models/albumModel');
const Song = require('../models/songModel');

// This file is essentially a go-between for client and model classes

exports.searchSongsByTitle = async (req, res) => {
    try{
        q = req.query.q;
        if(!q){
            return res.render('searchResults', {results: [], query: q});
        }
        const songs = await Song.findSongsByTitle(q);

        const results = songs.map(s => ({
            id: s.song_id,
            album_id: s.album_id,
            title: s.title,
            lyrics: s.lyrics,
            snippet: s.lyrics.substring(0, 100),
        }))

        return res.render('searchResults', {results, query: q});
    
    } catch (error) {
        console.error('error in searchSongsByTitle:', error);
        // code 500 means internal error, couldn't process request
        return res.status(500).send('Internal server error')
    }
}

exports.searchSongsByTitleAPI = async (req, res) => {
    try{
        const q = (req.query.q || '').trim();
        if(!q){
            return res.json({results: []});
        }
        const songs = await Song.findSongsByTitle(q) || [];
        const results = (songs || []).map(s => ({
            id: s.song_id,
            album_id: s.album_id,
            title: s.title,
            lyrics: s.lyrics,
            snippet: s.lyrics.substring(0, 100),
        }));

        return res.json({results: results});
    } catch (error) {
        console.error('error in searchSongsByTitleAPI:', error);
        return res.status(500).json({error: 'Internal server error'});
    }
}