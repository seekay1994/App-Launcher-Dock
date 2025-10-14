'use strict';

export var scriptProperties = createScriptProperties()
    .addCheckbox({ name: 'isMovable',    label: 'Drag And Drop',     value: false })
.finish();

const BACKGROUND_BASE_WIDTH = 100;

let parentLayer;
let canvasSize;
let centerY;
let lastParentPos = new Vec3(0, 0, 0);
let mode;
let isDragging = false;
let dragOffset;
let currentPos;
const STORAGE_KEY = "AppDockPosition";

export function init(value) {
	parentLayer = thisLayer.getParent();
	canvasSize = engine.canvasSize;
	centerY = canvasSize.y * Math.min(1, 1 - shared.edgeThreshold);
	
	thisLayer.visible = false;

    let stored = localStorage.get(STORAGE_KEY);
    parentLayer.origin = stored || parentLayer.origin;
}

export function update(value) {	
	if (!shared.appDockEnabled) {
		return;
	}
	
    currentPos = parentLayer.origin;
    if (currentPos == lastParentPos) return;

    lastParentPos = currentPos;

	updateAlignment();

	let totalSpan = shared.appDockWidth;

	let scaleX, scaleY;
	if (mode === 'horizontal') {
		scaleX = (totalSpan / BACKGROUND_BASE_WIDTH) * 0.33;
		scaleY = 32 * 0.01;
	} else {
		scaleY = (totalSpan / BACKGROUND_BASE_WIDTH) * 0.33;
		scaleX = 32 * 0.01;
	}

	thisLayer.scale = new Vec3(scaleX, scaleY, value.z);
}

function updateAlignment() {
	centerY = canvasSize.y * Math.min(0.9, 1 - shared.edgeThreshold);
	const thresholdX = canvasSize.x * shared.edgeThreshold;

	let alignment;

	if (currentPos.x <= thresholdX) {
		mode = 'vertical';
		alignment = 'right';
	} else if (currentPos.x >= canvasSize.x - thresholdX) {
		mode = 'vertical';
		alignment = 'left';
	} else if (currentPos.y <= centerY) {
		mode = 'horizontal';
		alignment = 'top';
	} else if (currentPos.y > centerY) {
		mode = 'horizontal';
		alignment = 'bottom';
	} else {
		mode = 'horizontal';
		alignment = 'bottom';
	}

	thisLayer.alignment = alignment;
}

export function cursorDown(event) {
    if (scriptProperties.isMovable) {
        isDragging = true;
		dragOffset = parentLayer.origin.subtract(event.worldPosition);
    }
}

export function cursorUp(event) {
    isDragging = false;
    localStorage.set(STORAGE_KEY, parentLayer.origin);
}

export function cursorMove(event) {
    if (isDragging && scriptProperties.isMovable && parentLayer.visible) {
        let newPos = event.worldPosition.add(dragOffset);
        parentLayer.origin = newPos;
    }
}

export function cursorEnter(event) {
    if (scriptProperties.isMovable) {
	thisLayer.visible = true;
    }
}

export function cursorLeave(event) {
	thisLayer.visible = false;
}
