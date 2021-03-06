'use strict';

var angular = require('angular');
require('angular-animate');
require('angular-toastr');
require('angular-local-storage');
require('./third-party/uikit/datepicker');
require('./third-party/uikit/notify');
require('./third-party/jquery.caret.min');
require('./third-party/jquery.tag-editor.min');
var moment = require('moment');

angular
    .module('adminApp', [ 
        'ngAnimate', 
        'toastr',
        'LocalStorageModule'
    ])
    .constant('moment', moment);
    
require('./core');
require('./editor-tools');
require('./editor/index');