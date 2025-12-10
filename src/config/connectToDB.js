const mysql = require('mysql2/promise');

const db = mysql.createPool({
    host:'localhost',
    port: '3306',
    user: 'admin',
    password: 'REDACTED',
    database: 'LilBLibrary'
});

module.exports = db;
