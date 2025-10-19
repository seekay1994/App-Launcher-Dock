'use strict';

import * as WEMath from 'WEMath';

// This needs to contain the NAME of the user shortcut property you want to tie to this
// Mind that it needs to be the NAME and not the label. The label is what is visible to the user while the NAME is the thing you see in the editors property settings UNDER the textbox where you edit the label.
export var scriptProperties = createScriptProperties()
	.addText({name: 'shortcutName', label: 'User Shortcut Property Name', value: ''})
.finish();

let originalScale = 0.5;
let currentScale  = originalScale;
let parent;

export function init(value) {
	// Create a new layer object "layer.clicked" that is used by the main script to detect if a layer has been clicked
	// This is done as the main layer has to compute icon layer origins in a central place and therefore the "bounce" animation when clicking an icon needs this object
	Object.defineProperty(thisLayer, "clicked", {
		enumerable: true,
		configurable: true,
		writable: true,
		value: false
	});	
	Object.defineProperty(thisLayer, "cursorDetected", {
		enumerable: true,
		configurable: true,
		writable: true,
		value: false
	});

	parent        = thisLayer.getParent();
	const rawOriginalScale = value.copy()
	originalScale = rawOriginalScale.x;
	currentScale  = originalScale;
}

export function update(value) {
	// Return early if App Launcher Dock is disabled (parent layer is invisible) or if this layer is invisible (icon not enabled)
	if (!parent.visible || !thisLayer.visible) {
		return value;
	}

	thisLayer.alpha = shared.dockAlpha;

	const cursor   = input.cursorWorldPosition;				// Get cursor world position
	const worldPos = parent.origin.add(thisLayer.origin);	// Calculate this layers world position
	const dist     = cursor.subtract(worldPos).length();	// Calculate the distance to the cursor

	thisLayer.cursorDetected = dist <= shared.radius; // Set layer.cursorDetected to true if cursor was detected in range

	let t = (dist - shared.minDistance) / (shared.radius - shared.minDistance);
	t = WEMath.smoothStep(0, 1, t);

	let targetScale = WEMath.mix(shared.maxScale, shared.minScale, t);

	currentScale = WEMath.mix(currentScale, targetScale, engine.frametime * 18);
	currentScale = Math.max(shared.minScale, Math.min(shared.maxScale, currentScale));

	return new Vec3(currentScale, currentScale, currentScale);
}

// When layer is clicked, set layer.clicked to true and run the user shortcut defined by the textbox
export function cursorClick(event) {
	if (thisLayer.visible && parent.visible) {
		thisLayer.clicked = true;
		engine.openUserShortcut(scriptProperties.shortcutName);
	}
}
