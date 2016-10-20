//
// This file auto-generated with generate-wrappers.js
// Date: Thu Oct 20 2016 15:52:38 GMT-0700 (PDT)
//

var _ = require('underscore');
var widgets = require('jupyter-js-widgets');

var GeometryModel = require('../../core/Geometry').GeometryModel;
var GeometryView = require('../../core/Geometry').GeometryView;


var EdgesGeometryModel = GeometryModel.extend({

    defaults: _.extend({}, GeometryModel.prototype.defaults, {

        _view_name: 'EdgesGeometryView',
        _model_name: 'EdgesGeometryModel',


    }),

    constructThreeObject: function() {

        return new THREE.EdgesGeometry();

    },

    createPropertiesArrays: function() {

        GeometryModel.prototype.createPropertiesArrays.call(this);

    },

});

var EdgesGeometryView = GeometryView.extend({});

module.exports = {
    EdgesGeometryView: EdgesGeometryView,
    EdgesGeometryModel: EdgesGeometryModel,
};
