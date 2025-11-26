const mysql = require('mysql2');

const connection = mysql.createConnection({
    host:'REDACTED',
    port: '3306',
    user: 'admin',
    password: 'REDACTED',
    database: 'LilBLibrary'
});

connection.connect((err) => {
    if(err) {
        console.error('error connecting to database');
        return;
    }
    console.log('connected to mySQL')
});

module.exports = connection;