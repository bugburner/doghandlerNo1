print "Content-type: text/html"
print """
<html>
<head><title>Hammerhigh</title></head>
<link href="css/design.css" rel="stylesheet" type="text/css" />
<link href="css/page.css" rel="stylesheet" type="text/css" />
<style type="text/css">
<!--a:link { font-weight:bold; color:#202E2C; text-decoration:none;
                                     #}-->
<!--a:visited { font-weight:bold; color:#202E2C; text-decoration:none; }-->
<!--a:focus { font-weight:bold; color:#202E2C; text-decoration:underline; }-->
<!--a:hover { font-weight:bold; background-color:#eeeeee; text-decoration:none; }-->
<!--a:active { font-weight:bold; color:lime; text-decoration:underline; }-->
</style>
<script src="../js/page.js"   type="text/javascript"></script>
<script src="../js/menu.js"   type="text/javascript"></script>
<script src="../js/overlib.js"   type="text/javascript"></script>
</head>
<body>

<div id="links">
<br />

<p align="center">


<div class="rootMenuContainer" id="rdmenu">
                <div class="menuItem">
                <a onmouseover="switchMenu(this.parentNode,true)" onmouseout="switchMenu(this.parentNode,false)" href="index.py?action="  >Startpage</a>
                </div>
                </div>               
<div class="rootMenuContainer" id="rdmenu">
                <div class="menuItem">
                <a      onmouseover="switchMenu(this.parentNode,true)" onmouseout="switchMenu(this.parentNode,false)" href="index.py?action=dogs">Hunde</a>
                </div>
                </div>
<div class="rootMenuContainer" id="rdmenu">
                <div class="menuItem">
                <a      onmouseover="switchMenu(this.parentNode,true)" onmouseout="switchMenu(this.parentNode,false)" href="index.py?action=persons">Personen</a>
                </div>
                </div>
<div class="rootMenuContainer" id="rdmenu">
                <div class="menuItem">
                <a      onmouseover="switchMenu(this.parentNode,true)" onmouseout="switchMenu(this.parentNode,false)" href="index.py?action=tracks">Strecken</a>
                </div>
                </div>

</div>

<div id="mitte_oben"><p align="center" style="font-size:20pt;">hammerhigh[doghandlerNo1]<br></div>


"""
