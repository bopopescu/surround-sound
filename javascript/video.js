var videoshow = require('videoshow')
var spotify = require('./spotify.js')

var images = [
	__dirname + '/pics/jaj.png',
	__dirname + '/pics/ny.png',
	__dirname + '/pics/john.png'
]

var audio = __dirname + '/song.mp3'

var audioParams = {
	fade: true,
	delay: 0 // seconds
}

var name = ""
for (var x = 0; x < images.length; x++) {
	var image = images[x]
	var splitted = image.split("/")
	var title = splitted[splitted.length - 1]
	name = name + title.substring(0, title.length - 4) + "-"
}
name = name.substring(0, name.length - 1)

function generateVideo(pic1, pic2, pic3) {
	console.log("GENERATEVIDEO")
  var images = [
  	pic1, pic2, pic3
  ]
	videoshow(images, {
			size: '562x?',
			format: 'mp4',
			pixelFormat: 'yuv420p'
		})
		.audio(audio, audioParams)
		.save(name + '.mp4')
		.on('start', function(command) {
			console.log('ffmpeg process STARTED')
		})
		.on('error', function(err) {
			console.error('Error:', err)
		})
		.on('end', function(output) {
			console.log('Video created in:', output)
		})
}

var callSpotify = (genre) => {
	return new Promise((resolve, reject) => {
    console.log("BOUT TO CALL SPOTIFY")
		spotify.spotifyMain(genre).then((message) => {
			resolve("SUCCESS")
		})
	})
}

var videoMain = (genre, pic1, pic2, pic3) => {
  return new Promise((resolve, reject) => {
    console.log("BOUT TO GENERATE VIDEO")
  	callSpotify(genre).then((message) => {
  		generateVideo(pic1, pic2, pic3)
  	})
  })
}

module.exports = {
	videoMain
}
