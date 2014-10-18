/*
 * Api
*/

function Api() {
//	"use strict";

	this.request = function (call_parameter_target, call_parameter_arguments, call_parameter_callback) {

		var connection = new XMLHttpRequest();
			connection.open(
				"GET", 
				'x-js-py:'
					+('call_parameter_target='+call_parameter_target)
				+'|:|'
					+('call_parameter_arguments='+call_parameter_arguments)
				+'|:|'
					+('call_parameter_callback='+call_parameter_callback)
			);
			connection.send();

	};

}

var Api = new Api();
