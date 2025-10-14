'use strict';

// App Launcher Dock by seekay V1.21
// Main logic used for icon layer origins and to decide which icons are visible.
// Also calculating various shared values used throughout the system as a whole.

export var scriptProperties = createScriptProperties()
    .addCheckbox({ name: 'autoHide', label: 'Auto Hide Dock', value: false })
    .addCheckbox({ name: 'autoHideOverwrite', label: 'Auto Hide Overwrite \<small> (for changing settings w/ autohide) \</small>', value: false })

    .addSlider({ name: 'minScale', label: 'Base Icon Scale', value: 0.5, min: 0.1, max: 2, integer: false })
    .addSlider({ name: 'baseRadius', label: 'Base Cursor Radius', value: 0.5, min: 0, max: 1, integer: false })

    // The Dock will automatically use a vertical layout when it´s within this percentage of the left or right edge of the canvas.
    // Mind that this also works with negative values. A user with an ultrawide screen might need those if your wallpaper is created to also be used with "fill" alignment.
    .addSlider({ name: 'edgeThreshold', label: 'Vertical Alignment Threshold \<small> (canvas %) \</small>', value: 10, min: 0, max: 50, integer: false })

    .addCheckbox({ name: 'enable1', label: 'Enable #1', value: true })
    .addCheckbox({ name: 'enable2', label: 'Enable #2', value: true })
    .addCheckbox({ name: 'enable3', label: 'Enable #3', value: true })
    .addCheckbox({ name: 'enable4', label: 'Enable #4', value: true })
    .addCheckbox({ name: 'enable5', label: 'Enable #5', value: true })
    .addCheckbox({ name: 'enable6', label: 'Enable #6', value: true })
    .addCheckbox({ name: 'enable7', label: 'Enable #7', value: false })
    .addCheckbox({ name: 'enable8', label: 'Enable #8', value: false })
    .addCheckbox({ name: 'enable9', label: 'Enable #9', value: false })
    .addCheckbox({ name: 'enable10', label: 'Enable #10', value: false })
    .addCheckbox({ name: 'enable11', label: 'Enable #11', value: false })
    .addCheckbox({ name: 'enable12', label: 'Enable #12', value: false })
    .addCheckbox({ name: 'enable13', label: 'Enable #13', value: false })
    .addCheckbox({ name: 'enable14', label: 'Enable #14', value: false })
    .addCheckbox({ name: 'enable15', label: 'Enable #15', value: false })
    .addCheckbox({ name: 'enable16', label: 'Enable #16', value: false })
    .addCheckbox({ name: 'enable17', label: 'Enable #17', value: false })
    .addCheckbox({ name: 'enable18', label: 'Enable #18', value: false })
    .addCheckbox({ name: 'enable19', label: 'Enable #19', value: false })
    .addCheckbox({ name: 'enable20', label: 'Enable #20', value: false })
    .addCheckbox({ name: 'enable21', label: 'Enable #21', value: false })
    .addCheckbox({ name: 'enable22', label: 'Enable #22', value: false })
    .addCheckbox({ name: 'enable23', label: 'Enable #23', value: false })
    .addCheckbox({ name: 'enable24', label: 'Enable #24', value: false })
.finish();



// Icon layer names ("Launcher [N]", Default: 24)
// To add more icons, simply change the "24" to the number of icons you want, add more checkbox properties to this script and add more icon layers. Done! 
const ICON_NAMES = Array.from({ length: 24 }, (_, i) => `Launcher ${i + 1}`);

const JUMP_HEIGHT = 72;                         // Fixed jump height as having it scale with icons results in funky stuff.
const BOUNCES = 5;                              // Number of "jumps" the icon does after being clicked.
const DURATION = 2.5;                           // Total duration of the "jumping" after being clicked.

const ICON_SIZE = 128;                          // Base icon size/resolution.
const BASE_SPACING = 46;                        // Base spacing in-between icons.

const SCALE_MULTIPLIER = 1.75;                  // Base multiplier for icon size.
const MAX_RAW_SCALE_LIMIT = 3.3;                // uuuhhh... I think this is the absolute max multiplier for the base-scale.
const MINIMUM_ADD = 1                           // Minimum base scale added to the icon for when hovered. Yes, I suck at coding.

const SCALE_RANGE = { min: 0.5, max: 1.25 };    // Range for raw input scale.

const MIN_DISTANCE_FACTOR = 1.085;              // The cursor distance at which icons will be their max scale (1 = one icon layer).

const USER_RADIUS = { min: 4.8, max: 12.0 };    // Range for cursor radius. User will only see a range of 0-1 as these numbers don't really mean anything to them.

// Max vertical height before the dock is forced to point down, regardless of what scriptProperties.edgeThreshod is set to.
// This is done so the docks behaviour can be adjusted to also fit ultrawide screens (18:9, 21:9, 32:9) with "Fill" alignment while still allowing the dock to react properly to the upper screen edge.
const MIN_Y_THRESHOLD = 0.9;

const BACKGROUND_BASE_WIDTH = 100;              // This layers resolution



// Runtime variables
let icons = [];
let bounceTimers = {};
let parentLayer;
let canvasSize;
let thresholdY;
let iconHideTimer = 0.0;
let mode;
let alignment;
let bounceDirection;
let lastParentPos = new Vec3(0, 0, 0);



export function init() {
    icons = ICON_NAMES.map(name => thisScene.getLayer(name));
    parentLayer = thisLayer.getParent();
    canvasSize = engine.canvasSize;
    thresholdY = canvasSize.y * Math.min(MIN_Y_THRESHOLD, 1 - (scriptProperties.edgeThreshold * 0.01)); // Percent

    shared.dockAlpha = 1.0;
}



export function update() {
    if (!shared.appDockEnabled) return; // Return early if app dock is disabled (parent layer is invisible)

    updateAlignment();

    // Filter visible icons and calculate total size
    const sizes = [];
    for (let i = 0; i < icons.length; i++) {
        const icon = icons[i];
        const enabled = scriptProperties[`enable${i + 1}`];
        if (icon.visible !== enabled) icon.visible = enabled;
        if (enabled) {
            if (icon.alignment !== alignment) icon.alignment = alignment;
            sizes.push(mode === 'horizontal' ? icon.size.x * icon.scale.x : icon.size.y * icon.scale.y);
        }
    }

    if (sizes.length === 0) return;

    shared.cursorWorldPosition = input.cursorWorldPosition;

    updateShared();
    autoHideDock();

    const totalSize = sizes.reduce((a, b) => a + b, 0) + (sizes.length - 1) * shared.spacing;
    
    updateScale(totalSize);

    shared.appDockWidth = totalSize; // Shared scale for "Drag and Drop"-layer so it doesn´t need to be re-calculated

    let offset = -totalSize * 0.5;
    let visibleIndex = 0;
    
    for (let i = 0; i < icons.length; i++) {
        if (!scriptProperties[`enable${i + 1}`]) continue; // if an icon is not enabled, skip to the next

        const icon = icons[i];
        const size = sizes[visibleIndex++]; // Cache sizes of all icons to compute their origin
        let bounceOffset = 0;

        // Check if icons have been clicked and if so apply "bounce" animation
        // Icon layers have a custom object "layer.clicked"
        if (icon.clicked) {
            bounceTimers[i] = engine.runtime;
            icon.clicked = false;
        }

        if (bounceTimers[i] !== undefined) {
            const t = (engine.runtime - bounceTimers[i]) / DURATION;
            if (t >= 1) {
                delete bounceTimers[i];
            } else {
                const progress = t * BOUNCES;
                const bounceIndex = Math.floor(progress);
                const localT = progress - bounceIndex;
                const decay = 1 - bounceIndex / BOUNCES;
                bounceOffset = Math.sin(localT * Math.PI) * JUMP_HEIGHT * decay * bounceDirection;
            }
        }

        // Compute and apply layout and origin
        let origin;
        if (mode === 'horizontal') {
            origin = new Vec3(offset + size * 0.5, thisLayer.origin.y + shared.spacing * bounceDirection + bounceOffset, 0);
            offset += size + shared.spacing;
        } else {
            origin = new Vec3(thisLayer.origin.x + shared.spacing * bounceDirection + bounceOffset, offset + size * 0.5, 0);
            offset += size + shared.spacing;
        }

        icon.origin = origin;
    }
}



function updateAlignment() {
    const currentPos = parentLayer.origin;

    // Skip if parent hasn't moved since last frame
    if (currentPos === lastParentPos) return;
    // Cache current position for next frame comparison
    lastParentPos = new Vec3(currentPos.x, currentPos.y, currentPos.z);

    // Proceed only when changed
    shared.edgeThreshold = scriptProperties.edgeThreshold * 0.01;

    const thresholdX = canvasSize.x * shared.edgeThreshold;
    thresholdY = canvasSize.y * Math.min(MIN_Y_THRESHOLD, 1 - shared.edgeThreshold);

    // Determine orientation and alignment automatically
    if (currentPos.x <= thresholdX) {
        mode = "vertical";
        alignment = "left";
        bounceDirection = 1;
    } else if (currentPos.x >= canvasSize.x - thresholdX) {
        mode = "vertical";
        alignment = "right";
        bounceDirection = -1;
    } else if (currentPos.y <= thresholdY) {
        mode = "horizontal";
        alignment = "bottom";
        bounceDirection = 1;
    } else {
        mode = "horizontal";
        alignment = "top";
        bounceDirection = -1;
    }

    thisLayer.alignment = alignment;
}



// Calculate scaling and radius
// All returned to 'shared' so we only need to tie slider properties ONCE
function updateShared() {
    const minScale = scriptProperties.minScale;
    const baseRadius = scriptProperties.baseRadius;

    const clampedScale = Math.max(SCALE_RANGE.min, Math.min(SCALE_RANGE.max, minScale));

    const userRadius = USER_RADIUS.min + baseRadius * (USER_RADIUS.max - USER_RADIUS.min);
    const scaledRadius = clampedScale * userRadius;
    const iconScale = ICON_SIZE * minScale;

    shared.minScale = minScale;
    shared.maxScale = Math.min(MAX_RAW_SCALE_LIMIT, MINIMUM_ADD + minScale * SCALE_MULTIPLIER);
    shared.radius = scaledRadius * ICON_SIZE;
    shared.minDistance = iconScale * MIN_DISTANCE_FACTOR;
    shared.spacing = minScale * BASE_SPACING;
}



function autoHideDock() {
	if (scriptProperties.autoHide && !scriptProperties.autoHideOverwrite) {
		let anyHovered = false;

		for (let i = 0; i < icons.length; i++) {
			if (icons[i].cursorDetected) {
				anyHovered = true;
				break;
			}
		}

        if (!anyHovered && iconHideTimer == 0 && shared.dockAlpha == 0) return;

		const fadeSpeed = 12.0;
		const hideDelay = 3.5;

		if (anyHovered) {
			iconHideTimer = 0.0;
			shared.dockAlpha += (1.0 - shared.dockAlpha) * fadeSpeed * engine.frametime;
		} else {
			iconHideTimer += engine.frametime;
			if (iconHideTimer >= hideDelay) {
				shared.dockAlpha += (0.0 - shared.dockAlpha) * fadeSpeed * engine.frametime;
			}
		}
	} else {
		shared.dockAlpha = 1.0;
		iconHideTimer = 0.0;
	}
}



function updateScale(totalSpan) {
	const minScale = shared.minScale || 1;
	const spacing = shared.spacing || 0;
	const extent = (ICON_SIZE * minScale) + (spacing * 2);

	let scaleX = 1;
	let scaleY = 1;

	if (mode === 'horizontal') {
		scaleX = (totalSpan + (spacing * 2)) / BACKGROUND_BASE_WIDTH;
		scaleY = extent / BACKGROUND_BASE_WIDTH;
	} else {
		scaleY = (totalSpan + (spacing * 2)) / BACKGROUND_BASE_WIDTH;
		scaleX = extent / BACKGROUND_BASE_WIDTH;
	}

	thisLayer.scale = new Vec3(scaleX, scaleY, 1);
}
