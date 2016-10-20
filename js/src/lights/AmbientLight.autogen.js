//
// This file auto-generated with generate-wrappers.js
// Date: Thu Oct 20 2016 15:52:38 GMT-0700 (PDT)
//

var _ = require('underscore');
var widgets = require('jupyter-js-widgets');

var LightModel = require('./Light').LightModel;
var LightView = require('./Light').LightView;


var AmbientLightModel = LightModel.extend({

    defaults: _.extend({}, LightModel.prototype.defaults, {

        _view_name: 'AmbientLightView',
        _model_name: 'AmbientLightModel',


    }),

    constructThreeObject: function() {

        return new THREE.AmbientLight(
            this.get('color'),
            this.get('intensity')
        );

    },

    createPropertiesArrays: function() {

        LightModel.prototype.createPropertiesArrays.call(this);

    },

});

var AmbientLightView = LightView.extend({});

module.exports = {
    AmbientLightView: AmbientLightView,
    AmbientLightModel: AmbientLightModel,
};
