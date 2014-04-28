var LightbringerExalted = LightbringerExalted || {};
var BASE_URL = '/api/v1.0';

LightbringerExalted.Models = LightbringerExalted.Models || {};
LightbringerExalted.Collections = LightbringerExalted.Collections || {};
LightbringerExalted.Views = LightbringerExalted.Views || {};
LightbringerExalted.Router = LightbringerExalted.Router || Backbone.Router.extend({
	routes: {
		'': 'main',
		'charms': 'charm_list',
		'charm/:id': 'charm_detail'
	},

	main: function() {
		console.log('main!');
	},

	charm_list: function() {
		var charms = new LightbringerExalted.Collections.Charms();
		new LightbringerExalted.Views.Charms({
			el: $('#charm-list'),
			collection: charms
		});

		charms.fetch({reset: true});
	},

	charm_detail: function(charm_id) {
		var charm = new LightbringerExalted.Models.Charm({id: charm_id});
		var charm_detail = new LightbringerExalted.Views.CharmDetail({
			model: charm
		});

		$('#main-view').html(charm_detail.$el);

		charm.fetch();
	}
});

LightbringerExalted.Collections.Base = Backbone.Collection.extend({
	parse: function(data) {
		return data.objects;
	}
});


(function(){
	LightbringerExalted.Models.Charm = Backbone.Model.extend({
		urlRoot: BASE_URL + '/charm'
	});
	LightbringerExalted.Collections.Charms = LightbringerExalted.Collections.Base.extend({
		url: BASE_URL + '/charm'
	});
	LightbringerExalted.Views.Charms = Backbone.View.extend({
		events: {
			// TODO
		},

		initialize: function() {
			this.listenTo(this.collection, 'reset', this.render);
			_.bindAll(this, 'renderSubView');
		},

		render: function(){
			this.$el.html(this.collection.map(this.renderSubView));
		},

		renderSubView: function(model) {
			var subView = new LightbringerExalted.Views.Charm({ model: model});
			subView.render();
			return subView.$el;
		}
	});

	LightbringerExalted.Views.Charm = Backbone.View.extend({
		tagName: "li",

		events: {
			click: 'navigate'
		},

		render: function() {
			this.$el.html(this.model.get('name'));
		},

		navigate: function() {
			Backbone.history.navigate('charm/' + this.model.id, {trigger: true});
		}
	});

	LightbringerExalted.Views.CharmDetail = Backbone.View.extend({
		initialize: function() {
			this.listenTo(this.model, 'change', this.render);
		},
		render: function(){
			this.$el.html(this.model.get('name'));
		}
	});
})();
new LightbringerExalted.Router();
Backbone.history.start({pushState: true});