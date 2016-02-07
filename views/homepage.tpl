<html>
<head>
	<script type="text/javascript" src="/static/js/knockout.min.js"></script>
	<script type="text/javascript" src="/static/js/jquery.min.js"></script>
	<script type="text/javascript" src="/static/js/bootstrap.min.js"></script>
	<script type="text/javascript" src="/static/js/homepage.js" defer="defer"></script>

	<link rel="stylesheet" type="text/css" href="/static/css/bootstrap.min.css">
	<link rel="stylesheet" type="text/css" href="/static/css/bootstrap-flex.min.css">
	<link rel="stylesheet" type="text/css" href="/static/css/bootstrap-theme.min.css">
	<link rel="stylesheet" type="text/css" href="/static/css/styles.css">
</head>
<body class="homepage text-center">
	<div class="vertical-center horizontal-center">

		<h1>Code<strong><small>NAMES</small></strong></h1>

		<div class="container">
			<div class="row horizontal-center">
				<div class="col-xs-12 col-md-6">
					<div class="panel panel-default">
						<div class="panel-body vertical-center horizontal-center">
							<input type="button" class="btn btn-lg btn-primary" value="New Game" onclick="startNewGame()"/>
						</div>
					</div>
				</div>
				<div class="col-xs-12 col-md-6">
					<div class="panel panel-default">
						<div class="panel-body vertical-center horizontal-center">
							<form class="form-inline">
								<div class="form-group">
									<label for="gameToJoin" class="sr-only">Join a Game</label>
									<input type="text" class="form-control" id="gameToJoin" placeholder="Join a game">
								</div>
								<button type="submit" class="btn btn-danger">Go!</button>
							</form>
						</div>
					</div>
				</div>
			</div>
		</div>
	</div>
</body>
	
</html>