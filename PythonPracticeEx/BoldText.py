import webbrowser

f = open('helloworld.html','w')

message = """
<html>
<head>
<meta content="text/html; charset=utf-8" http-equiv="Content-Type" />
<title>Untitled 1</title>
</head>
<body>
<form style="align = center"><input name="code" id="code" type="text" value="" >
<script type="text/javascript">
    function makeid() {
    return Math.floor(Math.random()*2)
}
</script>
<input type="button" style="font-size:50pt" value="Toss" onclick="document.getElementById('code').value = makeid()">
</input>
</form>
</body>
</html>"""

f.write(message)
f.close()

webbrowser.open_new_tab('helloworld.html')