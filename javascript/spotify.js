var SpotifyWebApi = require("spotify-web-api-node");
var fs = require('fs')
var request = require('request');

var spotifyApi = new SpotifyWebApi({
  clientId : '41606d07c5f3410faa3c16c55a47b47f',
  clientSecret : '8322cddac5804f24ae8eda242e09ef58',
});


function generateSong(artist){
  var title = 'artist:'+artist
  spotifyApi.searchTracks(title)
    .then(function(data) {
      var firstPage = data.body.tracks.items;
      var str = ""
        firstPage.forEach(function(track, index) {
          if(track.preview_url != null && str == ""){
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
function authenticate(artist){
  spotifyApi.clientCredentialsGrant()
  .then(function(data) {
    spotifyApi.setAccessToken(data.body['access_token']);
    generateSong(artist)
  }, function(err) {
        console.log('Something went wrong when retrieving an access token', err);
  });
}

module.exports = {
  authenticate,
  generateSong
}
