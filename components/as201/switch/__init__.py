import esphome.codegen as cg
from esphome.components import switch
import esphome.config_validation as cv
from esphome.const import (
    DEVICE_CLASS_SWITCH,
    ENTITY_CATEGORY_CONFIG,
    ICON_CHIP,
)

from .. import CONF_AS201_ID, AS201Component, as201

DEPENDENCIES = ["as201"]

EnableUploadSwitch = as201.class_("EnableUploadSwitch", switch.Switch)

CONF_ENABLE_UPLOAD = "enable_upload"

CONFIG_SCHEMA = cv.Schema(
    {
        cv.GenerateID(CONF_AS201_ID): cv.use_id(AS201Component),
        cv.Optional(CONF_ENABLE_UPLOAD): switch.switch_schema(
            EnableUploadSwitch,
            device_class=DEVICE_CLASS_SWITCH,
            entity_category=ENTITY_CATEGORY_CONFIG,
            icon=ICON_CHIP,
        ),
    }
)

async def to_code(config):
    as201_component = await cg.get_variable(config[CONF_AS201_ID])

    if enable_upload_config := config.get(CONF_ENABLE_UPLOAD):
        s = await switch.new_switch(enable_upload_config)
        await cg.register_parented(s, config[CONF_AS201_ID])
        cg.add(as201_component.set_enable_upload_switch(s))
