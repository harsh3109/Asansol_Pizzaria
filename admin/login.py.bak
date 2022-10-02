#!"C:/Users/HARSH PRASAD/anaconda3/python.exe"
import cgi
import mysql.connector as conn

formData = cgi.FieldStorage()
username = formData.getvalue('username')
password = formData.getvalue('password')
error = formData.getvalue('error')
print('''Content-type:text/html\n\n
<!DOCTYPE html>
<html lang="en">
<head>
  <script src="https://code.jquery.com/jquery-1.9.1.js"></script>
    <!-- Basic Page Needs
  ================================================== -->
    <meta charset="utf-8">
    <title>Asansol Pizzaria | Admin Login</title>
    <link rel="shortcut icon" href="images/favicon.png" type="image/x-icon">
    <meta name="keyword" content="Asansol Pizzaria">
    <meta name="Description" content="Pizza Online Delivery">''')
if username == "Harsh" and password == 'password':
    print('<meta HTTP-EQUIV="REFRESH" content="0; url=dashboard.html">')
else:
    print('<meta HTTP-EQUIV="REFRESH" content="0; url=index.py?error=1">')
print("""    <!-- Mobile Specific Metas
  ================================================== -->
    <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1">

    <!-- CSS
  ================================================== -->
    <script src="js/admin-js.js"></script>
    <link href="css/admin-css.css" rel="stylesheet"/>
    <!--[if lt IE 9]>
		<script src="https://html5shim.googlecode.com/svn/trunk/html5.js"></script>
	<![endif]-->
</head>
<body>
</html>

""")