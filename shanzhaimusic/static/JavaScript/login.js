var zc = document.getElementById('zc')
        var dl = document.getElementById('dl')
        var hengtiao1 = document.getElementById('hengtiao1')
        var hengtiao2 = document.getElementById('hengtiao2')
        var submit1 = document.getElementById('submit1')
        var submit2 = document.getElementById('submit2')
        
        zc.onclick=function(){
            submit2.style.display='none';
            submit1.style.display='block'
            dl.style.opacity=0.3;
            zc.style.opacity=1;
            hengtiao1.style.opacity=1;
            hengtiao2.style.opacity=0.3;
            document.getElementsByClassName('login_pw_q')[0].style.display='block';
            document.getElementById('lname').style.display = 'none';
            document.getElementById('lpw').style.display = 'none';
            document.getElementById('zname').style.display = 'block';
            document.getElementById('zpw').style.display = 'block';
        }
        dl.onclick=function(){
            submit1.style.display='none'
            submit2.style.display='block'
            zc.style.opacity=0.3;
            dl.style.opacity=1;
            hengtiao1.style.opacity=0.3;
            hengtiao2.style.opacity=1;
            document.getElementsByClassName('login_pw_q')[0].style.display='none';
            document.getElementById('zname').style.display = 'none';
            document.getElementById('zpw').style.display = 'none';
            document.getElementById('lname').style.display = 'block';
            document.getElementById('lpw').style.display = 'block';
        }
        