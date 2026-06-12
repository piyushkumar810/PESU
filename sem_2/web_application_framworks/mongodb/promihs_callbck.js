const { mongoClient } = require('mongodb');

const uri = 'mongodb://localhost:27017';
const dbName = 'nodeDB';
const collectionName = 'promise';

// Function to connect to MongoDB and perform an operation using callbacks  

function insertwithCallback(client, callbacck) {
  const db = client.db(dbName);
  const collection = db.collection(collectionName);

    collection.insertOne({ name: 'John Doe', age: 30 }, (err, result) => {  
        if (err) {
            return callbacck(err);
        }
        console.log('Document inserted with callback:', result.insertedId);
        callbacck(null, result);
    });
}   

async function insertWithPromise(client) {
    const db = client.db(dbName);
    const collection = db.collection(collectionName);

    const document = { name: 'Jane Doe', age: 25 };

    try {
        const result = await collection.insertOne(document);
        console.log('Document inserted with promise:', result.insertedId);
    } catch (err) {
        console.error('Error inserting document with promise:', err);
    }
}
