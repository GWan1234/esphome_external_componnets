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

from .. import CONF_ML307R_ID, ML307RComponent, ml307r_ns

DEPENDENCIES = ["ml307r"]

ShutdownButton = ml307r_ns.class_("ShutdownButton", button.Button)
RebootButton = ml307r_ns.class_("RebootButton", button.Button)

CONF_SOFT_SHUTDOWN = "soft_shutdown"
CONF_SAEV_SHUTDOWN = "save_shutdown"
CONF_SOFT_REBOOT = "soft_reboot"
CONF_HARD_REBOOT = "hard_reboot"

CONFIG_SCHEMA = cv.Schema({
    cv.GenerateID(CONF_ML307R_ID): cv.use_id(ML307RComponent),
    cv.Optional(CONF_SOFT_SHUTDOWN): button.button_schema(
        ShutdownButton,
        device_class=DEVICE_CLASS_RESTART,
        entity_category=ENTITY_CATEGORY_DIAGNOSTIC,
        icon=ICON_RESTART,
    ),
    cv.Optional(CONF_SAEV_SHUTDOWN): button.button_schema(
        ShutdownButton,
        device_class=DEVICE_CLASS_RESTART,
        entity_category=ENTITY_CATEGORY_DIAGNOSTIC,
        icon=ICON_RESTART,
    ),
    cv.Optional(CONF_SOFT_REBOOT): button.button_schema(
        RebootButton,
        device_class=DEVICE_CLASS_RESTART,
        entity_category=ENTITY_CATEGORY_DIAGNOSTIC,
        icon=ICON_RESTART,
    ),
    cv.Optional(CONF_HARD_REBOOT): button.button_schema(
        RebootButton,
        device_class=DEVICE_CLASS_RESTART,
        entity_category=ENTITY_CATEGORY_DIAGNOSTIC,
        icon=ICON_RESTART,
    ),
})


async def to_code(config):
    ml307r_component = await cg.get_variable(config[CONF_ML307R_ID])

    if soft_shutdown_config := config.get(CONF_SOFT_SHUTDOWN):
        b = await button.new_button(soft_shutdown_config, 0)
        await cg.register_parented(b, config[CONF_ML307R_ID])
        cg.add(ml307r_component.set_soft_shutdown_button(b))
    if save_shutdown_config := config.get(CONF_SAEV_SHUTDOWN):
        b = await button.new_button(save_shutdown_config, 1)
        await cg.register_parented(b, config[CONF_ML307R_ID])
        cg.add(ml307r_component.set_save_shutdown_button(b))
    if soft_reboot_config := config.get(CONF_SOFT_REBOOT):
        b = await button.new_button(soft_reboot_config, 0)
        await cg.register_parented(b, config[CONF_ML307R_ID])
        cg.add(ml307r_component.set_soft_reboot_button(b))
    if hard_reboot_config := config.get(CONF_HARD_REBOOT):
        b = await button.new_button(hard_reboot_config, 1)
        await cg.register_parented(b, config[CONF_ML307R_ID])
        cg.add(ml307r_component.set_hard_reboot_button(b))