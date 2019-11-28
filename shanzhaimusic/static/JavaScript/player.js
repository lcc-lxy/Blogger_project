var btnnext = document.getElementById('btnnext')
    var music
    musiclist = new Array(
        'Rain.mp3',
        '世间美好与你环环相扣.mp3',
        '天堂和地狱之间.mp3',
        '樱花.mp3'
    )
    var musicindex = 0
    $('#btnnext').click(function(){
        musicindex++;
        console.log(musicindex)
        if(musicindex>=musiclist.length){
            musicindex = 0
        }
        getmusic()
        aud.play()
  })

    $('#btnpre').click(function(){
        musicindex--;

        if(musicindex < 0 ){
            musicindex = musiclist.length-1
        }
        console.log(musicindex);
        getmusic()
        aud.play()
    })



  function getmusic(){
      aud.src = 'music/'+musiclist[musicindex]
  }