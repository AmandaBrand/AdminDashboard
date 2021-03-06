(function(angular) {
	'use strict';

	angular
		.module('adminApp')
		.config(configure)
		.run(function($http) {
			$http.defaults.headers.common['X-CSRFToken'] = $('input[name=csrfmiddlewaretoken]').val();
		})
		.config(function(toastrConfig) {
			angular.extend(toastrConfig, {
				progressBar: true,
				timeOut: 7000,
			});
		})
		.factory('dataService', require('./data.service'));


	configure.$inject = ['$httpProvider'];
	function configure($httpProvider) {
		$httpProvider.defaults.xsrfCookieName = 'csrftoken';
		$httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
	}
}(window.angular));