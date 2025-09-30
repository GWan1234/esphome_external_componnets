import esphome.codegen as cg
from esphome.components import switch
import esphome.config_validation as cv
from esphome.const import (
    DEVICE_CLASS_SWITCH,
    ENTITY_CATEGORY_CONFIG,
    ICON_CHIP,
)

from .. import CONF_LD2460_ID, LD2460Component, ld2460_ns

DEPENDENCIES = ["ld2460"]

EnableUploadSwitch = ld2460_ns.class_("EnableUploadSwitch", switch.Switch)

CONF_ENABLE_UPLOAD = "enable_upload"

CONFIG_SCHEMA = cv.Schema(
    {
        cv.GenerateID(CONF_LD2460_ID): cv.use_id(LD2460Component),
        cv.Optional(CONF_ENABLE_UPLOAD): switch.switch_schema(
            EnableUploadSwitch,
            device_class=DEVICE_CLASS_SWITCH,
            entity_category=ENTITY_CATEGORY_CONFIG,
            icon=ICON_CHIP,
        ),
    }
)


async def to_code(config):
    ld2460_component = await cg.get_variable(config[CONF_LD2460_ID])

    if enable_upload_config := config.get(CONF_ENABLE_UPLOAD):
        s = await switch.new_switch(enable_upload_config)
        await cg.register_parented(s, config[CONF_LD2460_ID])
        cg.add(ld2460_component.set_enable_upload_switch(s))
