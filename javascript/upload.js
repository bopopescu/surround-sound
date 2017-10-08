// // Imports the Google Cloud client library
// const Storage = require('@google-cloud/storage');
// const GOOGLE_APPLICATION_CREDENTIALS = './calhacks-cc6b4c9dd3fa.json'
//
// const filename = './jaj-ny-john.mp4'
// const bucketName = 'tester'
//
// google.auth.getApplicationDefault(function(err, authClient) {
// 	if (err) {
// 		return cb(err);
// 	}
// });
//
// if (authClient.createScopedRequired &&
// 	authClient.createScopedRequired()) {
// 	authClient = authClient.createScoped(
// 		['https://www.googleapis.com/auth/devstorage.read_write']);
// }
//
// var storage = google.storage('v1');
// storage.buckets.list({
// 	auth: authClient,
// 	project: projectId
// }, cb);
//
//
// // Uploads a local file to the bucket
// storage
// 	.bucket(bucketName)
// 	.upload(filename)
// 	.then(() => {
// 		console.log(`${filename} uploaded to ${bucketName}.`);
// 	})
// 	.catch(err => {
// 		console.error('ERROR:', err);
// 	});


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
  const bucketName = 'calhacks'
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
  // storage
  //   .getBuckets()
  //   .then((results) => {
  //     const buckets = results[0];
  //
  //     console.log('Buckets:');
  //     buckets.forEach((bucket) => {
  //       console.log(bucket.name);
  //     });
  //   })
  //   .catch((err) => {
  //     console.error('ERROR:', err);
  //   });
  // [END auth_cloud_explicit]
}

//authCloudImplicit()
authCloudExplicit()
// const Storage = require('@google-cloud/storage');
//
// var storage = google.storage('v1');
// storage.buckets.list({
// 	auth: authClient,
// 	project: projectId
// }, cb);
//
// storage
// 	.bucket(bucketName)
// 	.upload(filename)
// 	.then(() => {
// 		console.log(`${filename} uploaded to ${bucketName}.`);
// 	})
// 	.catch(err => {
// 		console.error('ERROR:', err);
// 	});
