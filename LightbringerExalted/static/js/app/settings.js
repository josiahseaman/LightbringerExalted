require.config({
	deps: ['jquery'],
	paths: {
		'backbone': '/static/vendor/backbone/backbone',
		'jquery': '/static/vendor/jquery/dist/jquery.min',
		'underscore': '/static/vendor/underscore/underscore',
		'handlebars': '/static/vendor/handlebars/handlebars',
		// 'templates': '/static/templates',
		'hbs': '/static/vendor/requirejs-hbs/hbs'
	},
	shim: {
		'backbone': {
			deps: ['underscore', 'jquery'],
			exports: 'Backbone'
		},
		'underscore': {
			exports: '_'
		},
		'jquery': {
			exports: 'jQuery'
		}
	}
});

require(['index']);