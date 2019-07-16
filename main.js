function  showResult(str){
    if (str.length==0) {
      document.getElementById("rh").innerHTML="";
      return;
    }
    if (window.XMLHttpRequest) {
      xmlhttp=new XMLHttpRequest();
    } else {
      xmlhttp=new ActiveXObject("Microsoft.XMLHTTP");
    }
    xmlhttp.onreadystatechange=function() {
      if (this.readyState==4 && this.status==200) {
        document.getElementById("rh").innerHTML=this.responseText;
      }
    }
    xmlhttp.open("GET","fetch.php?q="+str,true);
    xmlhttp.send();
}
