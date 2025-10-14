'use strict';

// Applying layer alpha on an opacity effect as a workaround for the fact that user textures currently cannot be controlled via iLayer.alpha

export function update(value) {
	return thisLayer.alpha;
}