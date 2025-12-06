const db = require('../config/connectToDB.js');

class Album {
    constructor(id, title, date){
        this.id = id;
        this.title = title;
        this.date = date;
    }

    // static because we can call this on the class as a whole
    // we would never need to call this on an instance
    static async findByTitle(title){ async () => {
        const query = 'SELECT * FROM albums WHERE title LIKE ?';
        const pattern = `%${title}%`
        try{
            //results in format [rows, fields]
            const results = await db.query(query, [pattern]);
            // return one for now but likely will want to return more than 1 result in future
            if(results) {
                const data = results[0]
                return Album(data.id, data.title, data.date)
            }
            return null;
        } catch (error) {
            console.error('error fetching album by title: ', error)
            throw error
        }
    }}

    static async getAllAlbums() { async () => {
        const query = 'SELECT * FROM albums';
        try {
            const results = await db.query(query);
            // now map all results to album objects
            return results.map(data => new Album(data.id, data.title, data.date));
        } catch (error) {
            console.error('error fetching all albums:', error);
            throw error;
        }
    }}
}

module.exports = Album;