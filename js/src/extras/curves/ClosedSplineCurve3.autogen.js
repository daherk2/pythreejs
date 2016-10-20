//
// This file auto-generated with generate-wrappers.js
// Date: Thu Oct 20 2016 15:52:38 GMT-0700 (PDT)
//

var _ = require('underscore');
var widgets = require('jupyter-js-widgets');

var ThreeModel = require('../../_base/Three').ThreeModel;
var ThreeView = require('../../_base/Three').ThreeView;


var ClosedSplineCurve3Model = ThreeModel.extend({

    defaults: _.extend({}, ThreeModel.prototype.defaults, {

        _view_name: 'ClosedSplineCurve3View',
        _model_name: 'ClosedSplineCurve3Model',


    }),

    constructThreeObject: function() {

        return new THREE.ClosedSplineCurve3();

    },

    createPropertiesArrays: function() {

        ThreeModel.prototype.createPropertiesArrays.call(this);

    },

});

var ClosedSplineCurve3View = ThreeView.extend({});

module.exports = {
    ClosedSplineCurve3View: ClosedSplineCurve3View,
    ClosedSplineCurve3Model: ClosedSplineCurve3Model,
};
