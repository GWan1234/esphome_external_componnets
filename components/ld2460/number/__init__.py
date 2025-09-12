import esphome.codegen as cg
from esphome.components import number
import esphome.config_validation as cv
from esphome.const import (
    ENTITY_CATEGORY_CONFIG,
    CONF_HEIGHT,
    CONF_ANGLE,
    UNIT_METER,
    UNIT_DEGREES
)

from .. import CONF_LD2460_ID, LD2460Component, ld2460_ns

DEPENDENCIES = ["ld2460"]

HeightNumber = ld2460_ns.class_("HeightNumber", number.Number)
AngleNumber = ld2460_ns.class_("AngleNumber", number.Number)
DetectDistanceNumber = ld2460_ns.class_("DetectDistanceNumber", number.Number)
DetectStartAngleNumber = ld2460_ns.class_("DetectStartAngleNumber", number.Number)
DetectEndAngleNumber = ld2460_ns.class_("DetectEndAngleNumber", number.Number)

CONF_DETECT_DISTANCE = "detect_distance"
CONF_DETECT_START_ANGLE = "detect_start_angle"
CONF_DETECT_END_ANGLE = "detect_end_angle"
ICON_ALPHA_Z_BOX_OUTLINE = "mdi:alpha-z-box-outline"
ICON_ALPHA_R_BOX_OUTLINE = "mdi:alpha-r-box-outline"
ICON_FORMAT_TEXT_ROTATION_ANGLE_UP = "mdi:format-text-rotation-angle-up"


CONFIG_SCHEMA = cv.Schema(
    {
        cv.GenerateID(CONF_LD2460_ID): cv.use_id(LD2460Component),
        cv.Optional(CONF_HEIGHT): number.number_schema(
            HeightNumber,
            unit_of_measurement=UNIT_METER,
            entity_category=ENTITY_CATEGORY_CONFIG,
            icon=ICON_ALPHA_Z_BOX_OUTLINE,
        ),
        cv.Optional(CONF_ANGLE): number.number_schema(
            AngleNumber,
            unit_of_measurement=UNIT_DEGREES,
            entity_category=ENTITY_CATEGORY_CONFIG,
            icon=ICON_FORMAT_TEXT_ROTATION_ANGLE_UP,
        ),
        cv.Optional(CONF_DETECT_DISTANCE): number.number_schema(
            DetectDistanceNumber,
            unit_of_measurement=UNIT_METER,
            entity_category=ENTITY_CATEGORY_CONFIG,
            icon=ICON_ALPHA_R_BOX_OUTLINE,
        ),
        cv.Optional(CONF_DETECT_START_ANGLE): number.number_schema(
            DetectStartAngleNumber,
            unit_of_measurement=UNIT_DEGREES,
            entity_category=ENTITY_CATEGORY_CONFIG,
            icon=ICON_FORMAT_TEXT_ROTATION_ANGLE_UP,
        ),
        cv.Optional(CONF_DETECT_END_ANGLE): number.number_schema(
            DetectEndAngleNumber,
            unit_of_measurement=UNIT_DEGREES,
            entity_category=ENTITY_CATEGORY_CONFIG,
            icon=ICON_FORMAT_TEXT_ROTATION_ANGLE_UP,
        ),
    }
)


async def to_code(config):
    ld2460_component = await cg.get_variable(config[CONF_LD2460_ID])

    if height_config := config.get(CONF_HEIGHT):
        n = await number.new_number(
            height_config,
            min_value=0,
            max_value=10,
            step=0.01,
        )
        await cg.register_parented(n, config[CONF_LD2460_ID])
        cg.add(ld2460_component.set_height_number(n))
    if angle_config := config.get(CONF_ANGLE):
        n = await number.new_number(
            angle_config,
            min_value=0,
            max_value=90,
            step=0.01,
        )
        await cg.register_parented(n, config[CONF_LD2460_ID])
        cg.add(ld2460_component.set_angle_number(n))
    if detect_distance_config := config.get(CONF_DETECT_DISTANCE):
        n = await number.new_number(
            detect_distance_config,
            min_value=0,
            max_value=6,
            step=0.1,
        )
        await cg.register_parented(n, config[CONF_LD2460_ID])
        cg.add(ld2460_component.set_detect_distance_number(n))
    if detect_start_angle_config := config.get(CONF_DETECT_START_ANGLE):
        n = await number.new_number(
            detect_start_angle_config,
            min_value=-360,
            max_value=360,
            step=1,
        )
        await cg.register_parented(n, config[CONF_LD2460_ID])
        cg.add(ld2460_component.set_detect_start_angle_number(n))
    if detect_end_angle_config := config.get(CONF_DETECT_END_ANGLE):
        n = await number.new_number(
            detect_end_angle_config,
            min_value=-360,
            max_value=360,
            step=1,
        )
        await cg.register_parented(n, config[CONF_LD2460_ID])
        cg.add(ld2460_component.set_detect_end_angle_number(n))
