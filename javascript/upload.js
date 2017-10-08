const video = require('./video.js')

function authCloudExplicit () {
  // [START auth_cloud_explicit]
  // Imports the Google Cloud client library.
  const Storage = require('@google-cloud/storage');

  // Instantiates a client. Explicitly use service account credentials by
  // specifying the private key file. All clients in google-cloud-node have this
  // helper, see https://googlecloudplatform.github.io/google-cloud-node/#/docs/google-cloud/latest/guides/authentication
  const storage = Storage({
    keyFilename: './calhacks-cc6b4c9dd3fa.json'
  });

  const filename = './jaj-ny-john.mp4'
  const bucketName = 'calhacks_moosic'
  // Makes an authenticated API request.
  storage
  	.bucket(bucketName)
  	.upload(filename)
  	.then(() => {
  		console.log(`${filename} uploaded to ${bucketName}.`);
  	})
  	.catch(err => {
  		console.error('ERROR:', err);
  	});
}

function firstFunction(genre, _callback){
    // do some asynchronous work
    // and when the asynchronous stuff is complete
    video.secondFunction(genre)
    _callback();
}

function secondFunction(genre){
    // call first function and pass in a callback function which
    // first function runs when it has completed
    firstFunction(genre, authCloudExplicit);
}
