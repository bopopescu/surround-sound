var SpotifyWebApi = require("spotify-web-api-node");
var fs = require('fs')
var request = require('request');

var spotifyApi = new SpotifyWebApi({
	clientId: '41606d07c5f3410faa3c16c55a47b47f',
	clientSecret: '8322cddac5804f24ae8eda242e09ef58',
});


function generateSong(genre) {
	console.log("GENERATE SONG")
	var title = 'genre:' + genre
	spotifyApi.searchTracks(title)
		.then(function(data) {
			var firstPage = data.body.tracks.items;
			var str = ""
			firstPage.forEach(function(track, index) {
				console.log(track.name + " BY: " + track.artists[0].name)
				if (track.preview_url != null && str == "") {
					str = track.preview_url;
					console.log(track.name)
				}
			});
			console.log(str)

			request
				.get(str)
				.on('error', function(err) {
					console.log("Counld not find an available song")
				})
				.pipe(fs.createWriteStream('song.mp3'));

		}, function(err) {
			console.log('Something went wrong!', err);
		});
}

// Retrieve an access token
// function authenticate() {
// 	console.log("AUTHENTICATE SPOTIFY")
// 	spotifyApi.clientCredentialsGrant()
// 		.then(function(data) {
// 			console.log('The access token expires in ' + data.body['expires_in']);
// 			console.log('The access token is ' + data.body['access_token']);
// 			spotifyApi.setAccessToken(data.body['access_token']);
// 		}, function(err) {
// 			console.log('Something went wrong when retrieving an access token', err);
// 		});
// }

var authenticate = new Promise((resolve, reject) => {
  console.log("AUTHENTICATE SPOTIFY")
	spotifyApi.clientCredentialsGrant()
		.then(function(data) {
			console.log('The access token expires in ' + data.body['expires_in']);
			console.log('The access token is ' + data.body['access_token']);
			spotifyApi.setAccessToken(data.body['access_token']);
      resolve("SUCCESS")
		}, function(err) {
			console.log('Something went wrong when retrieving an access token', err);
      reject(err)
		});
})


var auth = new Promise((resolve, reject) => {
	authenticate.then((message) => {
    resolve("SUCCESS")
  })
})

var spotifyMain = (genre) => {
	return new Promise((resolve, reject) => {
		auth.then((message) => {
			generateSong(genre)
      resolve("SUCCESS")
		})
	})
}


module.exports = {
	spotifyMain
}
