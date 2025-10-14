'use strict';

// Make sure this layer is invisible if App Dock is not enabled. This way all logic is stopped.

export function update(value) {
	shared.appDockEnabled = thisLayer.visible;
}