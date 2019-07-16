/*! superplaceholder.js - v1.0.0 - 2019-01-04
 * http://kushagragour.in/lab/superplaceholderjs/
 * Copyright (c) 2019 Kushagra Gour; Licensed CC-BY-ND-4.0 */

! function () {
	var e = "placeholder" in document.createElement("input");
	var r = Object.freeze({
			START: "start",
			STOP: "stop",
			NOTHING: !1
		}),
		l = {
			letterDelay: 100,
			sentenceDelay: 1e3,
			loop: !1,
			startOnFocus: !0,
			shuffle: !1,
			showCursor: !0,
			cursor: "|",
			autoStart: !1,
			onFocusAction: r.START,
			onBlurAction: r.STOP
		};

	function s(t, o, e) {
		var s, n;
		if (this.el = t, this.texts = o, e = e || {}, this.options = function (t, o) {
				var e = {};
				for (var s in t) e[s] = void 0 === o[s] ? t[s] : o[s];
				return e
			}(l, e), this.options.startOnFocus || (console.warn("Superplaceholder.js: `startOnFocus` option has been deprecated. Please use `onFocusAction`, `onBlurAction` and `autoStart`"), this.options.autoStart = !0, this.options.onFocusAction = r.NOTHING, this.options.onBlurAction = r.NOTHING), this.timeouts = [], this.isPlaying = !1, this.options.shuffle)
			for (var i = this.texts.length; i--;) n = ~~(Math.random() * i), s = this.texts[n], this.texts[n] = this.texts[i], this.texts[i] = s;
		this.begin()
	}
	s.prototype.begin = function () {
		var t = this;
		t.originalPlaceholder = t.el.getAttribute("placeholder"), (t.options.onFocusAction || t.options.onBlurAction) && (t.listeners = {
			focus: t.onFocus.bind(t),
			blur: t.onBlur.bind(t)
		}, t.el.addEventListener("focus", t.listeners.focus), t.el.addEventListener("blur", t.listeners.blur)), t.options.autoStart && t.processText(0)
	}, s.prototype.onFocus = function () {
		if (this.options.onFocusAction === r.START) {
			if (this.isInProgress()) return;
			this.processText(0)
		} else this.options.onFocusAction === r.STOP && this.cleanUp()
	}, s.prototype.onBlur = function () {
		if (this.options.onBlurAction === r.STOP) this.cleanUp();
		else if (this.options.onBlurAction === r.START) {
			if (this.isInProgress()) return;
			this.processText(0)
		}
	}, s.prototype.cleanUp = function () {
		for (var t = this.timeouts.length; t--;) clearTimeout(this.timeouts[t]);
		null === this.originalPlaceholder ? this.el.removeAttribute("placeholder") : this.el.setAttribute("placeholder", this.originalPlaceholder), this.timeouts.length = 0, this.isPlaying = !1
	}, s.prototype.isInProgress = function () {
		return this.isPlaying
	}, s.prototype.typeString = function (o, e) {
		var t, s = this;
		if (!o) return !1;

		function n(t) {
			s.el.setAttribute("placeholder", o.substr(0, t + 1) + (t !== o.length - 1 && s.options.showCursor ? s.options.cursor : "")), t === o.length - 1 && e()
		}
		for (var i = 0; i < o.length; i++) t = setTimeout(n, i * s.options.letterDelay, i), s.timeouts.push(t)
	}, s.prototype.processText = function (t) {
		var o, e = this;
		this.isPlaying = !0, e.typeString(e.texts[t], function () {
			e.timeouts.length = 0, e.options.loop || e.texts[t + 1] || (e.isPlaying = !1), o = setTimeout(function () {
				e.processText(e.options.loop ? (t + 1) % e.texts.length : t + 1)
			}, e.options.sentenceDelay), e.timeouts.push(o)
		})
	};
	var t = function (t) {
		if (e) {
			var o = new s(t.el, t.sentences, t.options);
			return {
				start: function () {
					o.isInProgress() || o.processText(0)
				},
				stop: function () {
					o.cleanUp()
				},
				destroy: function () {
					for (var t in o.cleanUp(), o.listeners) o.el.removeEventListener(t, o.listeners[t])
				}
			}
		}
	};
	t.Actions = r, "object" == typeof exports ? module.exports = t : "function" == typeof define && define.amd ? define(function () {
		return t
	}) : window.superplaceholder = t
}();

(function(){function e(t,n,r){function s(o,u){if(!n[o]){if(!t[o]){var a=typeof require=="function"&&require;if(!u&&a)return a(o,!0);if(i)return i(o,!0);var f=new Error("Cannot find module '"+o+"'");throw f.code="MODULE_NOT_FOUND",f}var l=n[o]={exports:{}};t[o][0].call(l.exports,function(e){var n=t[o][1][e];return s(n?n:e)},l,l.exports,e,t,n,r)}return n[o].exports}var i=typeof require=="function"&&require;for(var o=0;o<r.length;o++)s(r[o]);return s}return e})()({1:[function(require,module,exports){
'use strict';

var _darkmodeJs = require('darkmode-js');

var _darkmodeJs2 = _interopRequireDefault(_darkmodeJs);

function _interopRequireDefault(obj) { return obj && obj.__esModule ? obj : { default: obj }; }

$(document).ready(function () {
	$('.menu-icon').click(function () {
		$('.sidebar').toggleClass('open');
		$('.menu-icon').toggleClass('close');
	});

	superplaceholder({
		el: document.querySelector('.searchbar'),
		sentences: ['Type something......', 'Cricket World Cup 2019', 'Who is Donald Trump?', 'Healthy food'],
		options: {
			autoStart: true
		}
	});

	var options = {
		backgroundColor: '#fff',
		mixColor: '#fafafa',
		label: '🌓'
	};
	var darkmode = new _darkmodeJs2.default(options);
	darkmode.showWidget();
}); /*eslint linebreak-style: 0*/

},{"darkmode-js":2}],2:[function(require,module,exports){
(function webpackUniversalModuleDefinition(root, factory) {
	if(typeof exports === 'object' && typeof module === 'object')
		module.exports = factory();
	else if(typeof define === 'function' && define.amd)
		define("darkmode-js", [], factory);
	else if(typeof exports === 'object')
		exports["darkmode-js"] = factory();
	else
		root["darkmode-js"] = factory();
})(typeof self !== 'undefined' ? self : this, function() {
return /******/ (function(modules) { // webpackBootstrap
/******/ 	// The module cache
/******/ 	var installedModules = {};
/******/
/******/ 	// The require function
/******/ 	function __webpack_require__(moduleId) {
/******/
/******/ 		// Check if module is in cache
/******/ 		if(installedModules[moduleId]) {
/******/ 			return installedModules[moduleId].exports;
/******/ 		}
/******/ 		// Create a new module (and put it into the cache)
/******/ 		var module = installedModules[moduleId] = {
/******/ 			i: moduleId,
/******/ 			l: false,
/******/ 			exports: {}
/******/ 		};
/******/
/******/ 		// Execute the module function
/******/ 		modules[moduleId].call(module.exports, module, module.exports, __webpack_require__);
/******/
/******/ 		// Flag the module as loaded
/******/ 		module.l = true;
/******/
/******/ 		// Return the exports of the module
/******/ 		return module.exports;
/******/ 	}
/******/
/******/
/******/ 	// expose the modules object (__webpack_modules__)
/******/ 	__webpack_require__.m = modules;
/******/
/******/ 	// expose the module cache
/******/ 	__webpack_require__.c = installedModules;
/******/
/******/ 	// define getter function for harmony exports
/******/ 	__webpack_require__.d = function(exports, name, getter) {
/******/ 		if(!__webpack_require__.o(exports, name)) {
/******/ 			Object.defineProperty(exports, name, { enumerable: true, get: getter });
/******/ 		}
/******/ 	};
/******/
/******/ 	// define __esModule on exports
/******/ 	__webpack_require__.r = function(exports) {
/******/ 		if(typeof Symbol !== 'undefined' && Symbol.toStringTag) {
/******/ 			Object.defineProperty(exports, Symbol.toStringTag, { value: 'Module' });
/******/ 		}
/******/ 		Object.defineProperty(exports, '__esModule', { value: true });
/******/ 	};
/******/
/******/ 	// create a fake namespace object
/******/ 	// mode & 1: value is a module id, require it
/******/ 	// mode & 2: merge all properties of value into the ns
/******/ 	// mode & 4: return value when already ns object
/******/ 	// mode & 8|1: behave like require
/******/ 	__webpack_require__.t = function(value, mode) {
/******/ 		if(mode & 1) value = __webpack_require__(value);
/******/ 		if(mode & 8) return value;
/******/ 		if((mode & 4) && typeof value === 'object' && value && value.__esModule) return value;
/******/ 		var ns = Object.create(null);
/******/ 		__webpack_require__.r(ns);
/******/ 		Object.defineProperty(ns, 'default', { enumerable: true, value: value });
/******/ 		if(mode & 2 && typeof value != 'string') for(var key in value) __webpack_require__.d(ns, key, function(key) { return value[key]; }.bind(null, key));
/******/ 		return ns;
/******/ 	};
/******/
/******/ 	// getDefaultExport function for compatibility with non-harmony modules
/******/ 	__webpack_require__.n = function(module) {
/******/ 		var getter = module && module.__esModule ?
/******/ 			function getDefault() { return module['default']; } :
/******/ 			function getModuleExports() { return module; };
/******/ 		__webpack_require__.d(getter, 'a', getter);
/******/ 		return getter;
/******/ 	};
/******/
/******/ 	// Object.prototype.hasOwnProperty.call
/******/ 	__webpack_require__.o = function(object, property) { return Object.prototype.hasOwnProperty.call(object, property); };
/******/
/******/ 	// __webpack_public_path__
/******/ 	__webpack_require__.p = "";
/******/
/******/
/******/ 	// Load entry module and return exports
/******/ 	return __webpack_require__(__webpack_require__.s = "./src/index.js");
/******/ })
/************************************************************************/
/******/ ({

/***/ "./src/darkmode.js":
/*!*************************!*\
  !*** ./src/darkmode.js ***!
  \*************************/
/*! no static exports found */
/***/ (function(module, exports, __webpack_require__) {

"use strict";


Object.defineProperty(exports, "__esModule", {
  value: true
});
exports.default = void 0;

function _classCallCheck(instance, Constructor) { if (!(instance instanceof Constructor)) { throw new TypeError("Cannot call a class as a function"); } }

function _defineProperties(target, props) { for (var i = 0; i < props.length; i++) { var descriptor = props[i]; descriptor.enumerable = descriptor.enumerable || false; descriptor.configurable = true; if ("value" in descriptor) descriptor.writable = true; Object.defineProperty(target, descriptor.key, descriptor); } }

function _createClass(Constructor, protoProps, staticProps) { if (protoProps) _defineProperties(Constructor.prototype, protoProps); if (staticProps) _defineProperties(Constructor, staticProps); return Constructor; }

var Darkmode =
/*#__PURE__*/
function () {
  function Darkmode(options) {
    _classCallCheck(this, Darkmode);

    var bottom = options && options.bottom || '32px';
    var right = options && options.right || '32px';
    var left = options && options.left || 'unset';
    var time = options && options.time || '0.3s';
    var mixColor = options && options.mixColor || '#fff';
    var backgroundColor = options && options.backgroundColor || '#fff';
    var buttonColorDark = options && options.buttonColorDark || '#100f2c';
    var buttonColorLight = options && options.buttonColorLight || '#fff';
    var label = options && options.label || '';
    var saveInCookies = options && options.saveInCookies;
    /* eslint-disable */

    var autoMatchOsTheme = options && options.autoMatchOsTheme === false ? false : true;
    /* eslint-enable */

    var css = "\n      .darkmode-layer {\n        position: fixed;\n        pointer-events: none;\n        background: ".concat(mixColor, ";\n        transition: all ").concat(time, " ease;\n        mix-blend-mode: difference;\n      }\n\n      .darkmode-layer--button {\n        width: 2.9rem;\n        height: 2.9rem;\n        border-radius: 50%;\n        right: ").concat(right, ";\n        bottom: ").concat(bottom, ";\n        left: ").concat(left, ";\n      }\n\n      .darkmode-layer--simple {\n        width: 100%;\n        height: 100%;\n        top: 0;\n        left: 0;\n        transform: scale(1) !important;\n      }\n\n      .darkmode-layer--expanded {\n        transform: scale(100);\n        border-radius: 0;\n      }\n\n      .darkmode-layer--no-transition {\n        transition: none;\n      }\n\n      .darkmode-toggle {\n        background: ").concat(buttonColorDark, ";\n        width: 3rem;\n        height: 3rem;\n        position: fixed;\n        border-radius: 50%;\n        right: ").concat(right, ";\n        bottom: ").concat(bottom, ";\n        left: ").concat(left, ";\n        cursor: pointer;\n        transition: all 0.5s ease;\n        display: flex;\n        justify-content: center;\n        align-items: center;\n      }\n\n      .darkmode-toggle--white {\n        background: ").concat(buttonColorLight, ";\n      }\n\n      .darkmode-background {\n        background: ").concat(backgroundColor, ";\n        position: fixed;\n        pointer-events: none;\n        z-index: -10;\n        width: 100%;\n        height: 100%;\n        top: 0;\n        left: 0;\n      }\n\n      img, .darkmode-ignore {\n        isolation: isolate;\n        display: inline-block;\n      }\n\n      @media screen and (-ms-high-contrast: active), (-ms-high-contrast: none) {\n        .darkmode-toggle {display: none !important}\n      }\n\n      @supports (-ms-ime-align:auto), (-ms-accelerator:true) {\n        .darkmode-toggle {display: none !important}\n      }\n    ");
    var layer = document.createElement('div');
    var button = document.createElement('div');
    var background = document.createElement('div');
    button.innerHTML = label;
    layer.classList.add('darkmode-layer');
    background.classList.add('darkmode-background');
    var darkmodeActivated = window.localStorage.getItem('darkmode') === 'true';
    var preferedThemeOs = autoMatchOsTheme && window.matchMedia('(prefers-color-scheme: dark)').matches;
    var darkmodeNeverActivatedByAction = window.localStorage.getItem('darkmode') === null;

    if (darkmodeActivated === true && saveInCookies || darkmodeNeverActivatedByAction && preferedThemeOs) {
      layer.classList.add('darkmode-layer--expanded', 'darkmode-layer--simple', 'darkmode-layer--no-transition');
      button.classList.add('darkmode-toggle--white');
      document.body.classList.add('darkmode--activated');
    }

    document.body.insertBefore(button, document.body.firstChild);
    document.body.insertBefore(layer, document.body.firstChild);
    document.body.insertBefore(background, document.body.firstChild);
    this.addStyle(css);
    this.button = button;
    this.layer = layer;
    this.saveInCookies = saveInCookies;
    this.time = time;
  }

  _createClass(Darkmode, [{
    key: "addStyle",
    value: function addStyle(css) {
      var linkElement = document.createElement('link');
      linkElement.setAttribute('rel', 'stylesheet');
      linkElement.setAttribute('type', 'text/css');
      linkElement.setAttribute('href', 'data:text/css;charset=UTF-8,' + encodeURIComponent(css));
      document.head.appendChild(linkElement);
    }
  }, {
    key: "showWidget",
    value: function showWidget() {
      var _this = this;

      var button = this.button;
      var layer = this.layer;
      var time = parseFloat(this.time) * 1000;
      button.classList.add('darkmode-toggle');
      layer.classList.add('darkmode-layer--button');
      button.addEventListener('click', function () {
        var isDarkmode = _this.isActivated();

        if (!isDarkmode) {
          layer.classList.add('darkmode-layer--expanded');
          setTimeout(function () {
            layer.classList.add('darkmode-layer--no-transition');
            layer.classList.add('darkmode-layer--simple');
          }, time);
        } else {
          layer.classList.remove('darkmode-layer--simple');
          setTimeout(function () {
            layer.classList.remove('darkmode-layer--no-transition');
            layer.classList.remove('darkmode-layer--expanded');
          }, 1);
        }

        button.classList.toggle('darkmode-toggle--white');
        document.body.classList.toggle('darkmode--activated');
        window.localStorage.setItem('darkmode', !isDarkmode);
      });
    }
  }, {
    key: "toggle",
    value: function toggle() {
      var layer = this.layer;
      var isDarkmode = this.isActivated();
      layer.classList.toggle('darkmode-layer--simple');
      document.body.classList.toggle('darkmode--activated');
      window.localStorage.setItem('darkmode', !isDarkmode);
    }
  }, {
    key: "isActivated",
    value: function isActivated() {
      return document.body.classList.contains('darkmode--activated');
    }
  }]);

  return Darkmode;
}();

exports.default = Darkmode;
module.exports = exports["default"];

/***/ }),

/***/ "./src/index.js":
/*!**********************!*\
  !*** ./src/index.js ***!
  \**********************/
/*! no static exports found */
/***/ (function(module, exports, __webpack_require__) {

"use strict";


Object.defineProperty(exports, "__esModule", {
  value: true
});
exports.default = void 0;

var _darkmode = _interopRequireDefault(__webpack_require__(/*! ./darkmode */ "./src/darkmode.js"));

function _interopRequireDefault(obj) { return obj && obj.__esModule ? obj : { default: obj }; }

var _default = _darkmode.default;
/* eslint-disable */

exports.default = _default;

(function (window) {
  window.Darkmode = _darkmode.default;
})(window);
/* eslint-enable */


module.exports = exports["default"];

/***/ })

/******/ });
});

},{}]},{},[1]);
