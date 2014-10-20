/*
 * Api
*/

function Api() {
//	"use strict";

	this.request = function (call_parameter_target, call_parameter_arguments, call_parameter_callback) {

		var connection = (
			'x-js-py:'
					+('call_parameter_target='+call_parameter_target)
				+'|:|'
					+('call_parameter_arguments='+call_parameter_arguments)
				+'|:|'
					+('call_parameter_callback='+call_parameter_callback)
			);
		document.location.assing(connection);

	};

}

var Api = new Api();
