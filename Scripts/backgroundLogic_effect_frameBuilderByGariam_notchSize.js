'use strict';

export var scriptProperties = createScriptProperties()
	.addSlider({name: 'baseNotch', label: 'Base Notch Size', value: 0.5, min: 0, max: 1, integer: false})
.finish();

export function update(value) {
	return scriptProperties.baseNotch * thisLayer.scale.y;
}
