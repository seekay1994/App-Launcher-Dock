'use strict';

export var scriptProperties = createScriptProperties()
	.addSlider({name: 'alpha', label: 'Opacity Slider', value: 0.35, min: 0, max: 1, integer: false})
.finish();

export function update(value) {
	let alpha = scriptProperties.alpha * shared.dockAlpha
	return new Vec2(alpha, alpha);
}