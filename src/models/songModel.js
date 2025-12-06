const db = require('../config/connectToDB.js');

class Song {
    constructor(song_id, album_id, title, track_number, lyrics){
        this.song_id = song_id;
        this.album_id = album_id;
        this.title = title;
        this.track_number = track_number;
        this.lyrics = lyrics;
    }

    static async findSongsByAlbumID(album_id) {
        const query = 'SELECT * FROM songs WHERE album_id = ?';
        try {
            const [results] = await db.query(query, [album_id]);
            if(results) {
                return results.map(data => {
                    new Song(data.song_id, data.album_id, data.title, data.track_number, data.lyrics)
                });
            }
            return null;
        } catch (error) {
            console.error('error fetching songs by album id:', error);
            throw error;
        }
    }

    static async findSongsByTitle(title) { 
        if(!title){return [];}
        const query = 'SELECT * FROM songs WHERE title LIKE ?';
        const pattern = `%${title}%`;
        try{
            const [results] = await db.query(query, [pattern]);
            if(results) {
                const songArray = results.map(data => {
                    return new Song(data.song_id, data.album_id, data.title, data.track_number, data.lyrics)
                });
                return songArray;
            }
            return null;
        } catch (error) {
            console.error('error fetching songs by title:', error);
            throw error;
        }
    }
}
module.exports = Song;