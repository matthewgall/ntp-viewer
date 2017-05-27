<footer class="footer">
    <div class="container">
        <p class="text-muted">&copy; 2016 - <script type="text/javascript">document.write(new Date().getFullYear());</script> Matthew Gall - <a href="https://github.com/matthewgall/ntp-viewer">GitHub</a></p>
    </div>
</footer>

<script src="/static/js/jquery.min.js"></script>
<script src="/static/js/bootstrap.min.js"></script>
<script type="text/javascript">
	$(document).ready(function(){
		setInterval(function(){
			$.getJSON( "/api/update", function( data ) {
				$.each( data, function( key, val ) {
					console.log("Updating #" + key + " to: " + val )
					$("#" + key).text(val);
				});
			});
		}, 10000);
	});
</script>
</body>
</html>