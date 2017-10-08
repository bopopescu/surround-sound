const video = require('./video.js')

function authCloudExplicit() {
	console.log("AUTH")
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

var callVideo = (genre, pic1, pic2, pic3) => {
	return new Promise((resolve, reject) => {
		console.log("BOUT TO CREATE VID")
		video.videoMain(genre, pic1, pic2, pic3).then((message) => {
			resolve("SUCCESS")
		})
	})
}

function main(genre, pic1, pic2, pic3) {
	callVideo(genre, pic1, pic2, pic3).then((message) => {
			console.log("BOUT TO AUTH")
			authCloudExplicit()
		})
		.catch((fail) => {
			console.log("failed to upload")
		})
}

main("pop", __dirname + '/pics/jaj.png',
  __dirname + '/pics/ny.png',
  __dirname + '/pics/john.png')

  module.exports{
    main
  }
