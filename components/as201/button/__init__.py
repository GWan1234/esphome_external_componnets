import esphome.codegen as cg
from esphome.components import button
import esphome.config_validation as cv
from esphome.const import (
    CONF_FACTORY_RESET,
    CONF_RESTART,
    DEVICE_CLASS_RESTART,
    ENTITY_CATEGORY_CONFIG,
    ENTITY_CATEGORY_DIAGNOSTIC,
    ICON_RESTART,
    ICON_RESTART_ALERT,
)

from .. import CONF_AS201_ID, AS201Component, as201

DEPENDENCIES = ["as201"]

CONF_RESET_Z_AXIS = "reset_z_axis"
CONF_RESET_EULER = "reset_euler"

FactoryResetButton = as201.class_("FactoryResetButton", button.Button)
RestartButton = as201.class_("RestartButton", button.Button)
ResetZAxisButton = as201.class_("ResetZAxisButton", button.Button)
ResetEulerButton = as201.class_("ResetEulerButton", button.Button)

CONFIG_SCHEMA = {
    cv.GenerateID(CONF_AS201_ID): cv.use_id(AS201Component),
    cv.Optional(CONF_FACTORY_RESET): button.button_schema(
        FactoryResetButton,
        device_class=DEVICE_CLASS_RESTART,
        entity_category=ENTITY_CATEGORY_CONFIG,
        icon=ICON_RESTART_ALERT,
    ),
    cv.Optional(CONF_RESTART): button.button_schema(
        RestartButton,
        device_class=DEVICE_CLASS_RESTART,
        entity_category=ENTITY_CATEGORY_DIAGNOSTIC,
        icon=ICON_RESTART,
    ),
    cv.Optional(CONF_RESET_Z_AXIS): button.button_schema(
        ResetZAxisButton,
        device_class=DEVICE_CLASS_RESTART,
        entity_category=ENTITY_CATEGORY_DIAGNOSTIC,
        icon=ICON_RESTART,
    ),
    cv.Optional(CONF_RESET_EULER): button.button_schema(
        ResetEulerButton,
        device_class=DEVICE_CLASS_RESTART,
        entity_category=ENTITY_CATEGORY_DIAGNOSTIC,
        icon=ICON_RESTART,
    ),
}


async def to_code(config):
    as201_component = await cg.get_variable(config[CONF_AS201_ID])

    if factory_reset_config := config.get(CONF_FACTORY_RESET):
        b = await button.new_button(factory_reset_config)
        await cg.register_parented(b, config[CONF_AS201_ID])
        cg.add(as201_component.set_factory_reset_button(b))
    if restart_config := config.get(CONF_RESTART):
        b = await button.new_button(restart_config)
        await cg.register_parented(b, config[CONF_AS201_ID])
        cg.add(as201_component.set_restart_button(b))
    if reset_z_axis_config := config.get(CONF_RESET_Z_AXIS):
        b = await button.new_button(reset_z_axis_config)
        await cg.register_parented(b, config[CONF_AS201_ID])
        cg.add(as201_component.set_reset_z_axis_button(b))
    if reset_euler_config := config.get(CONF_RESET_EULER):
        b = await button.new_button(reset_euler_config)
        await cg.register_parented(b, config[CONF_AS201_ID])
        cg.add(as201_component.set_reset_euler_button(b))