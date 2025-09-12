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

from .. import CONF_LD2460_ID, LD2460Component, ld2460_ns

DEPENDENCIES = ["ld2460"]

FactoryResetButton = ld2460_ns.class_("FactoryResetButton", button.Button)
RestartButton = ld2460_ns.class_("RestartButton", button.Button)

CONFIG_SCHEMA = {
    cv.GenerateID(CONF_LD2460_ID): cv.use_id(LD2460Component),
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
}


async def to_code(config):
    ld2460_component = await cg.get_variable(config[CONF_LD2460_ID])

    if factory_reset_config := config.get(CONF_FACTORY_RESET):
        b = await button.new_button(factory_reset_config)
        await cg.register_parented(b, config[CONF_LD2460_ID])
        cg.add(ld2460_component.set_factory_reset_button(b))
    if restart_config := config.get(CONF_RESTART):
        b = await button.new_button(restart_config)
        await cg.register_parented(b, config[CONF_LD2460_ID])
        cg.add(ld2460_component.set_restart_button(b))
