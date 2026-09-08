
YG = {
	config: {
		lottery_check_time: 1000, // 倒计时揭晓 检查开奖结果的间隔时间
		lottery_refresh_time_index: 5000, // [首页]页面每次读取最新开奖的间隔时间
		lottery_refresh_time_result: 5000, // [最新揭晓]页面每次读取最新开奖的间隔时间
		lottery_interval_time: 35,// 毫秒倒计时更新器的间隔时间
		shopping_time: 5000,// 正在云购 更新时间
		end: 0
	},
	_api_one: {},

	// 多个请求只生效一个，完成后下次请求才有效
	api_one: function (sendurl, action, params, callback) {
		if (this._api_one[action]) {
			return;
		}

		this.api(sendurl, action, params, callback);
	},

	_api_cached: {},

	// 带缓存
	api_cached: function (webpath, action, params, callback) {
		if (!params) {
			params = {};
		}
		if (!callback) {
			callback = function () { };
		}
		if (typeof (params) == 'function') {
			callback = params;
			params = {};
		}
		params['action'] = action;

		var key = $.param(params);
		if (this._api_cached[key]) {
			return callback(this._api_cached[key]);
		}

		$.ajax({
			type: "POST",
			url: webpath + 'Api/' + action,
			dataType: 'json',
			cache: false,
			data: params,
			success: function (r) {
				YG._api_cached[key] = r;
				callback(r);
			},
			complete: function () {
				delete YG._api_one[action];
			},
			beforeSend: function () {
				YG._api_one[action] = 1;
			}
		});
	},

	api: function (webpath, action, params, callback) {
		if (!params) {
			params = {};
		}
		if (!callback) {
			callback = function () { };
		}
		if (typeof (params) == 'function') {
			callback = params;
			params = {};
		}
		params['action'] = action;

		$.ajax({
			type: "POST",
			url: webpath + 'Api/' + action,
			dataType: 'json',
			cache: false,
			data: params,
			success: callback,
			complete: function () {
				delete YG._api_one[action];
			},
			beforeSend: function () {
				YG._api_one[action] = 1;
			}
		});
	},

	_events_data: {},
	_events_callback: {},
	get: function (key, callback) {
		if (!callback) {
			return this._events_data[key];
		}
		if (typeof (this._events_data[key]) == 'undefined') {
			if (typeof (this._events_callback[key]) == 'undefined') {
				this._events_callback[key] = new Array();
			}
			this._events_callback[key].push(callback);
		} else {
			callback(this._events_data[key]);
		}
	},
	set: function (key, data) {
		this._events_data[key] = data;
		if (this._events_callback[key]) {
			var callback;
			while (callback = this._events_callback[key].shift()) {
				callback(data);
			}
		}
	}
};


